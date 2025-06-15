# University gRPC Library System

A mock university library system implemented with Protocol Buffers and gRPC in **Python**.

---

## 📚 Project Structure

/
├── university.proto
├── university_pb2.py
├── university_pb2_grpc.py
├── src/
│   ├── server.py
│   └── client.py
├── grpcurl-tests.md
└── DELIVERY.md

- `university.proto` – Protobuf tanımı  
- `university_pb2*.py` – `protoc` ile üretilen stub dosyaları  
- `src/server.py` – Sunucu uygulaması  
- `src/client.py` – İstemci uygulaması  
- `grpcurl-tests.md` – gRPC test komutları ve çıktıları  
- `DELIVERY.md` – Classroom teslim raporu

---


## 🔧 Kurulum Adımları

1. Gerekli paketleri yükleyin: `pip install grpcio grpcio-tools protobuf`  
2. Stub dosyalarını oluşturun:  
   `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto`

---

## ▶️ Sunucu ve İstemci Nasıl Çalıştırılır

### Sunucu’yu başlatın:
`python src/server.py`  
**Çıktı:** `Server listening on port 50051`

---

### Başka bir terminalde istemciyi çalıştırın:
`cd src`  
`python client.py`  
**Örnek çıktı:**  
`Books: []`  
`Created Student: id: "xxxx-..." name: "Ali Veli" ...`  
`Loaned: id: "yyyy-..." student_id: "xxxx-..." ...`

## 🧪 grpcurl Test Kullanımı

Test komutları ve örnek çıktılarını görmek için `grpcurl-tests.md` dosyasına bakabilirsiniz.  
Bu araçla direkt gRPC servisleri test edebilirsiniz.

---

## 💡 Bonus Özellikler

- **Pagination**: `page_size` ve `page_token` alanları destekleniyor.  
- **Validation & Error Handling**:  
  - Geçersiz ID → `NOT_FOUND`  
  - Format hataları → `INVALID_ARGUMENT`

---

## 🚀 Gelecek Planlar

- TLS veya JWT tabanlı kimlik doğrulama  
- Prometheus metric takibi  
- Gerçek veritabanı entegrasyonu

---

## 📝 Notlar

- Şu anda sunucu mock veri kullanarak çalışıyor; gerçek DB bağlantısı mevcut değil.  
- `grpcurl-tests.md` ve `DELIVERY.md` proje belgelerini içerir.
