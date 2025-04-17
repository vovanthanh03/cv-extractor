import streamlit as st
from extract_info import extract_info
import os

st.set_page_config(page_title="Trích xuất thông tin CV", page_icon="📄", layout="centered")

st.title("📄 Trích xuất thông tin từ CV (PDF)")

uploaded_file = st.file_uploader("Chọn file PDF", type="pdf")

if uploaded_file is not None:
    # Lưu file tạm
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Trích xuất thông tin
    result = extract_info("temp.pdf")

    # Hiển thị kết quả
    if result:
        st.success("✅ Trích xuất thành công!")
        st.markdown(f"**👤 Họ tên:** {result['Họ tên']}")
        st.markdown(f"**⚧️ Giới Tính:** {result['Giới Tính']}")
        st.markdown(f"**📞 Số điện thoại:** {result['Số điện thoại']}")
        st.markdown(f"**🏠 Địa Chỉ:** {result['Địa Chỉ']}")
        st.markdown(f"**📧 Email:** {result['Email']}")
        st.markdown(f"**🎓 Trường:** {result['Trường']}")
    else:
        st.error("Không thể trích xuất thông tin từ file PDF.")

# Xoá file tạm nếu cần
if os.path.exists("temp.pdf"):
    os.remove("temp.pdf")
