import grpc
import university_pb2
import university_pb2_grpc
from google.protobuf import empty_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        books_stub = university_pb2_grpc.BooksServiceStub(channel)
        students_stub = university_pb2_grpc.StudentsServiceStub(channel)
        loans_stub = university_pb2_grpc.LoansServiceStub(channel)

        # Kitapları listele
        resp = books_stub.ListBooks(university_pb2.ListBooksRequest(page_size=10))
        print("Books:", resp.books)

        # Öğrenci oluştur
        new_student = university_pb2.Student(name="Ali Veli", student_number="20250001", email="ali.veli@example.com", is_active=True)
        created = students_stub.CreateStudent(university_pb2.CreateStudentRequest(student=new_student))
        print("Created Student:", created)

        # Ödünç alma (LoanBook)
        loan_req = university_pb2.LoanBookRequest(
        student_id=created.id,
        book_id=""  # buraya mevcut bir kitap ID’si ekleyin, örneğin stub veri
        )
        loan_resp = loans_stub.LoanBook(loan_req)
        print("Loaned:", loan_resp)

if __name__ == "__main__":
    run()
