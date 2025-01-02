#------------Bai01-----------
print("-----Bai01: Chia kẹo -------")
# Nhập số kẹo cô có và số học sinh
N = int(input("Nhập số kẹo cô có: "))
M = int(input("Nhập số học sinh trong lớp: "))

# Kiểm tra xem có thể chia đều kẹo hay không
if N >= M:
    # Tính số kẹo mỗi học sinh được nhận
    so_keo_moi_hoc_sinh = N // M
    # Tính số kẹo còn lại
    so_keo_con_lai = N % M
    print("Mỗi học sinh được nhận", so_keo_moi_hoc_sinh, "cái kẹo.")
    print("Cô còn lại", so_keo_con_lai, "cái kẹo.")
else:
    print("Không đủ kẹo để chia đều cho tất cả học sinh.")

#------------Bai02-----------
print("-----")
print("-----")
print("-----Bai02: Tính tuổi -------")
# Nhập họ tên
ho_ten = input("Nhập họ tên: ")

# Nhập năm sinh
nam_sinh = int(input("Nhập năm sinh: "))

# Tính tuổi hiện tại (giả sử năm hiện tại là 2023)
nam_hien_tai = 2023
tuoi = nam_hien_tai - nam_sinh

# In kết quả
print("Bạn", ho_ten, "năm nay", tuoi, "tuổi.")

#------------Bai03-----------
print("-----")
print("-----")
print("-----Bai03: Cho biết số thỏ trong rừng -------")
# Nhập số tháng
x = int(input("Nhập số tháng: "))

# Khởi tạo số lượng thỏ ban đầu
so_tho = 1

# Tính số lượng thỏ sau x tháng (sử dụng vòng lặp for)
for _ in range(x):
    so_tho *= 2

# In kết quả
print("Trong rừng có:", so_tho, "con thỏ.")

#------------Bai04-----------
print("-----")
print("-----")
print("-----Bai04: Chuỗi văn bản -------")
text = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

# Đếm số ký tự
num_characters = len(text)
print("Số ký tự trong đoạn văn:", num_characters)

# Kiểm tra sự xuất hiện của từ "hồ chí minh" (không phân biệt chữ hoa chữ thường)
if "hồ chí minh" in text.lower():
    print("Đoạn văn có chứa cụm từ 'hồ chí minh'")

# Tách đoạn văn thành các câu (cách làm đơn giản, chưa xử lý các trường hợp phức tạp)
sentences = text.split('.')

# In các câu
for sentence in sentences:
    print(sentence)

# Thay thế từ "Việt Nam" bằng "VIỆTNAM"
new_text = text.replace("Việt Nam", "VIỆT NAM")
print(new_text)

#------------Bai05-----------
print("-----")
print("-----")
print("-----Bai05: Thống kê điểm Học viên -------")
diem_thi = ['A', 'B', 'C', 'F', 'A', 'B', 'D', 'F', 'C', 'B']

print("---------------TỔNG KẾT--------------------")
# 1. Số sinh viên
so_sinh_vien = len(diem_thi)
print("Số sinh viên trong lớp:", so_sinh_vien)

# 2. Số sinh viên phải học lại
so_sinh_vien_hoc_lai = diem_thi.count('F')
print("Số sinh viên phải học lại:", so_sinh_vien_hoc_lai)

# 3. Số sinh viên có điểm từ B trở lên
so_sinh_vien_tu_B_tro_len = diem_thi.count('B') + diem_thi.count('A')
print("Số sinh viên có điểm từ B trở lên:", so_sinh_vien_tu_B_tro_len)

# 4. Loại bỏ điểm của sinh viên đầu và cuối
diem_thi_moi = diem_thi[1:-1]
print("Danh sách điểm mới:", diem_thi_moi)