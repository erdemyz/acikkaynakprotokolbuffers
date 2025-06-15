# grpcurl Testleri

## BooksService.ListBooks  
### Komut  

grpcurl -plaintext localhost:50051 university.BooksService.ListBooks

Örnek Çıktı
```bash
{
  "books": []
}
StudentsService.CreateStudent 
```
### Komut

grpcurl -plaintext \
  -d '{ "student": { "name":"Ali Veli", "student_number":"20250001", "email":"ali.veli@example.com", "is_active": true } }' \
  localhost:50051 university.StudentsService.CreateStudent

Örnek Çıktı
```bash
{
  "id": "a6007d51-138d-448c-8203-4388c00e8be4",
  "name": "Ali Veli",
  "student_number": "20250001",
  "email": "ali.veli@example.com",
  "is_active": true
}
StudentsService.ListStudents
```
### Komut

grpcurl -plaintext \
  -d '{ "page_size": 10 }' \
  localhost:50051 university.StudentsService.ListStudents

Örnek Çıktı
```bash
{
  "students": [
    {
      "id": "a6007d51-138d-448c-8203-4388c00e8be4",
      "name": "Ali Veli",
      "student_number": "20250001",
      "email": "ali.veli@example.com",
      "is_active": true
    }
  ],
  "next_page_token": ""
}
LoansService.LoanBook
```
Komut

grpcurl -plaintext \
  -d '{ "student_id":"a6007d51-138d-448c-8203-4388c00e8be4", "book_id":"" }' \
  localhost:50051 university.LoansService.LoanBook

Örnek Çıktı
```bash
{
  "id": "50d4e4bd-5b59-42f2-bb9c-0f456abc1234",
  "student_id": "a6007d51-138d-448c-8203-4388c00e8be4",
  "book_id": "",
  "loan_date": "2025-06-15",
  "return_date": "",
  "status": "ONGOING"
}
BooksService.GetBook (Invalid ID)
```
Komut

grpcurl -plaintext \
  -d '{ "id": "invalid-id" }' \
  localhost:50051 university.BooksService.GetBook

Örnek Çıktı (Hata)
```bash
ERROR:
  Code: NotFound
  Message: Book not found
```


