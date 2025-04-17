import re
import pdfplumber
import unicodedata

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

def extract_info(pdf_path):
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
        full_text = re.sub(r'\(cid:[^\)]+\)', '', full_text)
        lines = full_text.strip().split('\n')

        ho_pho_bien = [
            "Nguyen", "Tran", "Le", "Pham", "Huynh", "Hoang", "Phan", "Vu", "Vo", "Dang",
            "Bui", "Do", "Ho", "Ngo", "Duong", "Ly", "Dinh", "Ha", "Doan", "Cao", "Mai",
            "Trinh", "Ta", "Thai", "To", "Vuong", "Quach", "Chau", "La", "Kieu"
        ]

        ho_ten = "..."
        for line in lines:
            line_clean = remove_accents(line).strip()
            for ho in ho_pho_bien:
                if line_clean.startswith(ho):
                    ho_ten = line.strip()
                    break
            if ho_ten != "...":
                break

        # email_match = re.search(r'[\w\.-]+\s*@\s*gmail\.com', full_text)
        # email = email_match.group(0).replace(" ", "") if email_match else "..."
        email_match = re.search(r'[\w\.-]+\s*@\s*gmail\.com', full_text)
        if email_match:
            email = email_match.group(0).replace(" ", "")  
        else:
            email = "..."

        phone_match = re.search(r'0\d{2,3}[\s\.\-]?\d{3}[\s\.\-]?\d{3,4}', full_text)
        phone = phone_match.group(0) if phone_match else "..."

        university = "..."
        for line in lines:
            if "cao đẳng" in line.lower() or "đại học" in line.lower():
                university = line.strip()
                break

        gender_match = re.search(r'\b(Nam|Nữ)\b', full_text, re.IGNORECASE)
        gender = gender_match.group(0) if gender_match else "..."

        add = ['Phuong', 'Quan', 'Q.', 'Tp.', 'TP.HCM', 'Ho Ch Minh', 'Ha Noi', 'City']
        address = "..."
        for line in lines:
            line_clean = remove_accents(line)
            if line.count(',') >= 1 and any(kw in line for kw in add):
                address = line
                break

        return {
            "Họ tên": ho_ten,
            "Giới Tính": gender,
            "Số điện thoại": phone,
            "Địa Chỉ": address,
            "Email": email,
            "Trường": university
        }
    except Exception as e:
        return None