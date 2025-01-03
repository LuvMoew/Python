#
#
print('Bài 6: Xác định nguyên âm|Phụ âm')
ky_tu = input("Nhập một ký tự: ").lower()
if ky_tu in 'aeiou':
    print("Đây là nguyên âm!")
elif ky_tu.isalpha():
    print("Đây là phụ âm!")
else:
    print("Vui lòng nhập một ký tự chữ cái!")

#
#
print('Bài 7: Tính chỉ số BMI')
def tinh_bmi(chieu_cao, can_nang):
  """Tính chỉ số BMI

  Args:
    chieu_cao: Chiều cao của người (m)
    can_nang: Cân nặng của người (kg)

  Returns:
    Chỉ số BMI
  """
  bmi = can_nang / (chieu_cao ** 2)
  return bmi

def danh_gia_can_nang(bmi):
  """Đánh giá cân nặng dựa trên chỉ số BMI

  Args:
    bmi: Chỉ số BMI

  Returns:
    Chuỗi mô tả tình trạng cân nặng
  """
  if bmi < 18.5:
    return "Gầy"
  elif 18.5 <= bmi <= 24.9:
    return "Bình thường"
  elif 25 <= bmi <= 29.9:
    return "Thừa cân"
  else:
    return "Béo phì"

# Nhập liệu
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

# Tính toán BMI
bmi = tinh_bmi(chieu_cao, can_nang)

# Đánh giá cân nặng
ket_qua = danh_gia_can_nang(bmi)

# In kết quả
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
print(f"Bạn đang: {ket_qua}")

#
#
print('Bài 8: Xác định mùa trong năm')
def xac_dinh_mua(thang):
  """Hàm xác định mùa trong năm dựa vào tháng sinh

  Args:
    thang: Tháng sinh (số nguyên từ 1 đến 12)

  Returns:
    Chuỗi mô tả mùa tương ứng
  """

  if 1 <= thang <= 3:
    return "Mùa xuân"
  elif 4 <= thang <= 6:
    return "Mùa hạ"
  elif 7 <= thang <= 9:
    return "Mùa thu"
  elif 10 <= thang <= 12:
    return "Mùa đông"
  else:
    return "Tháng sinh không hợp lệ"

# Nhập tháng sinh
thang_sinh = int(input("Nhập tháng sinh của bạn (1-12): "))

# Gọi hàm xác định mùa và in kết quả
mua = xac_dinh_mua(thang_sinh)
print(f"Bạn sinh vào mùa {mua}")

#
#
print('Bài 9: Hiển thị bảng cửu chương')
def in_bang_cuu_chuong(so):
  """In bảng cửu chương của một số

  Args:
    so: Số cần in bảng cửu chương
  """

  for i in range(1, 11):
    print(f"{so} x {i} = {so * i}")

while True:
  try:
    so = int(input("Nhập vào bảng cửu chương muốn hiển thị (1-10): "))
    if 1 <= so <= 10:
      print(f"\nBẢNG CỬU CHƯƠNG {so}")
      in_bang_cuu_chuong(so)
      break
    else:
      print("Nhập sai, vui lòng nhập số từ 1 đến 10:")
  except ValueError:
    print("Vui lòng nhập một số nguyên!")
    
#
#
print('Bài 10: Tính điểm học tập của bạn')
def diem_chu(diem_10):
  """Chuyển đổi điểm số hệ 10 sang điểm chữ

  Args:
    diem_10: Điểm số hệ 10

  Returns:
    Điểm chữ tương ứng
  """

  if diem_10 >= 9.0:
      return 'A+'
  elif diem_10 >= 8.5:
      return 'A'
  elif diem_10 >= 8.0:
      return 'B+'
  elif diem_10 >= 7.0:
      return 'B'
  elif diem_10 >= 6.5:
      return 'C+'
  elif diem_10 >= 5.5:
      return 'C'
  elif diem_10 >= 5.0:
      return 'D+'
  elif diem_10 >= 4.0:
      return 'D'
  else:
      return 'F'

# Danh sách điểm số hệ 10
diem_10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]

# Tạo danh sách điểm chữ
diem_chu = [diem_chu(diem) for diem in diem_10]

# Tính điểm trung bình hệ 10
dtb_10 = sum(diem_10) / len(diem_10)

# Tính điểm trung bình hệ 4
dtb_4 = sum([diem_chu(diem) for diem in diem_10 if diem_chu(diem).isdigit()]) / len(diem_10)  # Chỉ tính trung bình cho các điểm có điểm chữ là số

print("Điểm hệ 10:", diem_10)
print("Điểm chữ tương ứng:", diem_chu)
print("Tổng số môn học:", len(diem_10))
print("ĐTB hệ 10:", dtb_10)
print("ĐTB hệ 4:", dtb_4)

#
#
print('Bài 11: Kiểm tra N có là số nguyên tố?')
import math

def is_prime(n):
  """Kiểm tra xem một số có phải là số nguyên tố hay không

  Args:
    n: Số nguyên dương cần kiểm tra

  Returns:
    True nếu n là số nguyên tố, False nếu không
  """

  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

# Nhập số nguyên dương N
n = int(input("Nhập vào một số nguyên dương N (N>1): "))

# Kiểm tra và in kết quả
if is_prime(n):
  print(f"Số {n} là số nguyên tố!")
else:
  print(f"Số {n} không phải là số nguyên tố!")

#
#
print('Bài 12: dãy số nguyên tố.')
import math

def is_prime(n):
  """Kiểm tra xem một số có phải là số nguyên tố hay không

  Args:
    n: Số nguyên dương cần kiểm tra

  Returns:
    True nếu n là số nguyên tố, False nếu không
  """

  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

# Nhập số nguyên dương N
n = int(input("Nhập vào một số nguyên dương N (N>1): "))

# Kiểm tra và in kết quả
if is_prime(n):
  print(f"Số {n} là số nguyên tố!")
else:
  print(f"Số {n} không phải là số nguyên tố!")

#
#
print('Bài 13: Đổi số từ thập phân sang nhị phân.')
def decimal_to_binary(n):
  """Chuyển đổi số thập phân sang nhị phân

  Args:
    n: Số thập phân cần chuyển đổi

  Returns:
    Chuỗi biểu diễn nhị phân
  """

  binary = ""
  while n > 0:
    binary = str(n % 2) + binary
    n //= 2
  return binary

# Nhập số từ người dùng
num = int(input("Nhập vào một số tự nhiên (N>0): "))

# Chuyển đổi và in kết quả
result = decimal_to_binary(num)
print(f"{num} (hệ 10) = {result} (hệ 2)")

#
#
print('Bài 14: Tìm số Max – Min - Mean. ')
def thong_ke_chieu_cao(chieu_cao):
  """Thực hiện các phép tính thống kê trên danh sách chiều cao

  Args:
    chieu_cao: Danh sách chiều cao của các sinh viên

  Returns:
    Một tuple chứa:
      - Chiều cao cao nhất
      - Chiều cao thấp nhất
      - Chiều cao trung bình
      - Số lượng sinh viên cao hơn hoặc bằng chiều cao trung bình
  """

  # Tìm chiều cao cao nhất và thấp nhất
  max_height = max(chieu_cao)
  min_height = min(chieu_cao)

  # Tính chiều cao trung bình
  avg_height = sum(chieu_cao) / len(chieu_cao)

  # Đếm số lượng sinh viên cao hơn hoặc bằng chiều cao trung bình
  count_above_avg = sum(1 for height in chieu_cao if height >= avg_height)

  return max_height, min_height, avg_height, count_above_avg

# Danh sách chiều cao ví dụ
chieu_cao_lop = [1.65, 1.7, 1.55, 1.64, 1.78, 1.67, 1.59, 1.62, 1.45, 1.8, 1.69, 1.5]

# Thực hiện thống kê
max_h, min_h, avg_h, count = thong_ke_chieu_cao(chieu_cao_lop)

# In kết quả
print("Chiều cao cao nhất:", max_h, "m")
print("Chiều cao thấp nhất:", min_h, "m")
print("Chiều cao trung bình:", avg_h, "m")
print("Số sinh viên cao hơn hoặc bằng chiều cao trung bình:", count)