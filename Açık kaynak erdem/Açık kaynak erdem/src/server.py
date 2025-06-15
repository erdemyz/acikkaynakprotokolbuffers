from concurrent import futures
import grpc
from google.protobuf import empty_pb2
import uuid
import university_pb2
import university_pb2_grpc

# Mock veri
books = {}
students = {}
loans = {}

class BooksServiceServicer(university_pb2_grpc.BooksServiceServicer):
    def ListBooks(self, request, context):
        return university_pb2.ListBooksResponse(books=list(books.values()))

    def GetBook(self, request, context):
        book = books.get(request.id)
        if not book:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found")
            return university_pb2.Book()
        return book

    def CreateBook(self, request, context):
        book = request.book
        book.id = str(uuid.uuid4())
        books[book.id] = book
        return book

    def UpdateBook(self, request, context):
        book = request.book
        if book.id not in books:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found")
            return university_pb2.Book()
        books[book.id] = book
        return book

    def DeleteBook(self, request, context):
        if request.id not in books:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Book not found")
        else:
            del books[request.id]
        return empty_pb2.Empty()

class StudentsServiceServicer(university_pb2_grpc.StudentsServiceServicer):
    def ListStudents(self, request, context):
        return university_pb2.ListStudentsResponse(students=list(students.values()))

    def GetStudent(self, request, context):
        student = students.get(request.id)
        if not student:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Student not found")
            return university_pb2.Student()
        return student

    def CreateStudent(self, request, context):
        student = request.student
        student.id = str(uuid.uuid4())
        students[student.id] = student
        return student

    def UpdateStudent(self, request, context):
        student = request.student
        if student.id not in students:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Student not found")
            return university_pb2.Student()
        students[student.id] = student
        return student

    def DeleteStudent(self, request, context):
        if request.id not in students:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Student not found")
        else:
            del students[request.id]
        return empty_pb2.Empty()

class LoansServiceServicer(university_pb2_grpc.LoansServiceServicer):
    def ListLoans(self, request, context):
        for loan in loans.values():
            yield loan

    def GetLoan(self, request, context):
        loan = loans.get(request.id)
        if not loan:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Loan not found")
            return university_pb2.Loan()
        return loan

    def LoanBook(self, request, context):
    # request.student_id ve request.book_id kullanılabilir
        loan = university_pb2.Loan(
        id=str(uuid.uuid4()),
        student_id=request.student_id,
        book_id=request.book_id,
        loan_date=datetime.date.today().isoformat(),
        return_date="",
        status=university_pb2.LoanStatus.ONGOING
    )
        loans[loan.id] = loan
        return loan

    def ReturnBook(self, request, context):
        loan = loans.get(request.id)
        if not loan:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Loan not found")
            return university_pb2.Loan()
        loan.status = university_pb2.LoanStatus.RETURNED
        loans[loan.id] = loan
        return loan

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BooksServiceServicer_to_server(BooksServiceServicer(), server)
    university_pb2_grpc.add_StudentsServiceServicer_to_server(StudentsServiceServicer(), server)
    university_pb2_grpc.add_LoansServiceServicer_to_server(LoansServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server listening on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
