# 📄 CV Extractor

**CV Extractor** là một ứng dụng trích xuất thông tin quan trọng từ file CV (PDF), bao gồm:
- Họ tên
- Email
- Số điện thoại
- Địa chỉ
- Giới tính
- Trường đại học

Giúp tiết kiệm thời gian xử lý hồ sơ tuyển dụng.

## 🚀 Trải nghiệm ngay
👉 [Dùng thử ứng dụng tại đây](https://cv-extractor-ctzmei8jtxohsrpxzjxkyq.streamlit.app/)

## 🖼️ Giao diện demo
![image](https://github.com/user-attachments/assets/6d52bcc7-4e52-411a-ae16-2a40f6f1104c)

## 🧠 Công nghệ sử dụng
- `Streamlit` - Giao diện web nhanh chóng cho Python
- `pdfplumber` - Trích xuất nội dung từ file PDF
- `re` (Regular Expressions) - Nhận diện mẫu dữ liệu như email, số điện thoại
- `PyMuPDF` / `pdfminer` (tuỳ chọn) - Các giải pháp thay thế để nâng cao độ chính xác

## 🛠️ Cách chạy local

```bash
# 1. Clone project
git clone https://github.com/your-username/CV_Extractor.git
cd CV_Extractor

# 2. Cài đặt thư viện
pip install -r requirements.txt

# 3. Chạy app
streamlit run src/app.py
