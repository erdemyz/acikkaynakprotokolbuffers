# gRPC Uygulama Geliştirme Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri
- **Ad Soyad**: Erdem Yorulmaz  
- **Öğrenci Numarası**: 170422042
- **Kullanılan Programlama Dili**: Python

---

## 📦 GitHub Repo
**Link**: https://github.com/erdemyz/acikkaynakprotokolbuffers
**Açıklama**: Proje `.proto`, stub dosyaları, sunucu ve istemci kodları ile `README.md`, `grpcurl-tests.md`, `DELIVERY.md` dosyalarını içerir.

---

## 📄 `.proto` Dosyası Özeti
- **Dosya Adı**: `university.proto`
- **Servisler & RPC’ler**:  
  - *BooksService*: ListBooks, GetBook, CreateBook, UpdateBook, DeleteBook  
  - *StudentsService*: ListStudents, GetStudent, CreateStudent, UpdateStudent, DeleteStudent  
  - *LoansService*: ListLoans, GetLoan, LoanBook, ReturnBook  
- **Enum**: `LoanStatus` (ONGOING, RETURNED, LATE) `Loan` mesajında kullanıldı  
- **Dil**: Tüm tanımlamalar İngilizce yazıldı (servis, mesaj ve alan isimleri)

---

## 🧪 grpcurl Test Dokümantasyonu
Test komutları ve JSON çıktı örnekleri `grpcurl-tests.md` dosyası içinde mevcuttur.  
Örnek başlıklar:  
- `BooksService.ListBooks`  
- `StudentsService.CreateStudent`  
- `StudentsService.ListStudents`  
- `LoansService.LoanBook`  
- `BooksService.GetBook (Invalid ID)`

---

## 🛠️ Derleme & Çalıştırma Talimatları

```bash
# 1. Stub dosyalarını üretin
python -m grpc_tools.protoc -I. \
  --python_out=. \
  --grpc_python_out=. \
  university.proto

# 2. Sunucuyu çalıştırın
python src/server.py

# 3. İstemciyi çalıştırın
cd src
python client.py
**Alternatif:** `grpcurl` komutları ile testlere `grpcurl-tests.md` üzerinden erişilebilir.

---

✅ **Kontrol Listesi**
- Stub dosyaları GitHub’da değil (`.gitignore` kullanıldı)
- `grpcurl-tests.md` dosyasında test komutları mevcut
- Test çıktıları eklendi (JSON ve hata mesajları)
- Tüm servisler başarıyla çalışıyor
- `README.md` kurulumu ve kullanımını açıklıyor

---

📌 **Ek Açıklamalar**
- Sunucu mock veri kullanarak çalışıyor; gerçek DB bağlantısı mevcut değil
- `grpcurl` ile JSON formatlı nested mesajların doğrusu en zor adım oldu
- Gelecek planlar `README.md` içinde özetlenmiştir (TLS/JWT, Prometheus, DB)
