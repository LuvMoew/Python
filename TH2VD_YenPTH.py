#----Trang 5----
# Các toán tử so sánh trong Python:
a = 10
b = 8
# --Kết quả của phép so sánh có kiểu dữ liệu Boolean---
print('1) Lớn hơn (a > b):', a>b)
print('2) Nhỏ hơn (a < b):', a<b)
print('3) Bằng (a == b):', a==b)
print('4) Lớn hơn hoặc bằng (a>=b):',a>=b)
print('5) Nhỏ hơn hoặc bằng (a<=b):',a<=b)
print('6) Khác (a!=b):',a!=b)
#--

#Trang 8
print('-------')
print('---Trang 8----')
# Các toán tử Logic trong Python:
x = 15
y = True
# 
kt = (x>3) and (x<10) # hoặc: kt = (x>3) & (x<10)
kt2 = (x>3) or (x<10) # hoặc: kt2 = (x>3) | (x<10)
kt3 = not y
#
print('1) Phép toán AND:', kt)
print('2) Phép toán OR:', kt2)
print('3) Phép toán NOT:', kt3)

#Trang 9
print('-------')
print('---Trang 9----')
# Câu lệnh điều kiện
so_tien = input('Nhập vào số tiền bạn có: ')
so_tien = int(so_tien)
if (so_tien >= 1000000000):
    print('Bạn đã là một tỷ phú!')
else:
    print('Bạn còn phải kiếm nhiều tiền hơn!')

#Trang 11
print('-------')
print('---Trang 11----')
N = int(input("Nhập vào một số nguyên N: "))

if N % 2 == 0:
  print(N, "là số chẵn.")
else:
  print(N, "là số lẻ.")

#Trang 10
print('-------')
print('---Trang 10----')
# In [2]:
num = 3
if num > 0:
  print(num, "là số dương.")
print("Thông điệp này luôn được in.")

# In [3]:
num = -1
if num > 0:
  print(num, "là số dương.")
print("Thông điệp này luôn được in.")

#Trang 12
print('-------')
print('---Trang 12----')
# In [5]:
num = 3
if num >= 0:
  print("Số dương")
else:
  print("Số âm")

# In [6]:
num = -1
if num >= 0:
  print("Số dương")
else:
  print("Số âm")

#Trang 13
print('-------')
print('---Trang 13----')
N = int(input("Nhập vào một số nguyên N: "))

if N % 2 == 0:
  print("Đây là số chẵn!")
else:
  print("Đây là số lẻ!")

#Trang 14
print('-------')
print('---Trang 14----')
number = float(input("Nhập vào một số: "))

if number > 0:
  print("Số dương")
elif number < 0:
  print("Số âm")
else:
  print("Số bằng 0")

#Trang 15
print('-------')
print('---Trang 15----')
gioi_tinh = int(input("Nhập giới tính (0-Nam | 1-Nữ): "))

if gioi_tinh == 0:
  print("Chào anh đẹp trai!")
elif gioi_tinh == 1:
  print("Chào chị xinh gái!")
else:
  print("Cảnh báo: Giới tính không xác định!")

#Trang 17
print('-------')
print('---Trang 17----')
num = float(input("Nhập một số: "))

if num >= 0:
  if num == 0:
    print("Số Không")
  else:
    print("Số dương")
else:
  print("Số âm")
#
#
print('Trang 25')
n = 20
i = 1
while (i < n):
  i = i + 1
  if (i % 3 == 0):
    continue
    # Bỏ qua các câu lệnh phía sau nếu không chia hết cho 3
  print(i)
# Câu lệnh lặp ngoài vòng lặp while
print('-----------------HUNG-----------------')
#
#
print('Trang 26')
# chỉ cho phép nhập tháng sinh 1 - 12
while True:
    n = int(input('Em sinh tháng mấy? '))
    if (1 <= n <= 12):
        # Tháng sinh nhập vào hợp lệ!
        break
    print('Tháng không đúng, vui lòng nhập lại')
# Câu lệnh ngoài vòng lặp while
print('Chào em cô gái tháng ', n)
#
#
print('Trang 27')
# Tính 10! = 1*2*3*4*5*6*7*8*9*10
# Tổng 10 = 1+2+3+4+5+6+7+8+9+10

n = 10
tich = 1
tong = 0

for i in range(1, n+1):
    # Mỗi lần lặp biến i tăng lên 1
    tich = tich * i
    tong = tong + i

print('10! = ', tich)
print('10+ = ', tong)
#
#
print('Trang 28')
# Đếm số ký tự M trong chuỗi
st = 'HUMG IN MY MIND'
dem = 0

for i in st:
    if (i == 'M'):
        dem = dem + 1

print('Số ký tự M có trong chuỗi là: ', dem)
#
#
print('Trang 29')
# Vòng lặp for với danh sách
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 
            'Nguyễn Lan Anh', 'Mai Phương Thúy',
            'Trần Thanh Thủy', 'Kiều Thành Công']

print('Danh sách học sinh bao gồm:')

tt = 1
for i in hoc_sinh:
    print(tt, ')', i)
    tt = tt + 1
#
#
print('Trang 30')
# Lệnh for với range()
for i in range(5):
    # Giá trị khởi đầu mặc định = 0
    # Bước nhảy mặc định = 1
    print(i)

#
#
print('Trang 31')
# Lệnh for với range(m, n)
for i in range(5, 10):
    # Giá trị khởi đầu m = 5
    # Giá trị kết thúc n = 10
    # Bước nhảy mặc định = 1
    print(i)
#
#
print('Trang 33')
# Lệnh for với range(m, n, d)
for i in range(2, 11, 2):
    # Giá trị khởi đầu m = 2
    # Giá trị kết thúc n = 11
    # Bước nhảy d = 2
    print(i)
#
#
print('Trang 34')
# Hiển thị bảng cửu chương từ 2 -> 9
for i in range(2, 10):
  print("Bảng cửu chương:", i)
  for j in range(1, 11):
    print(i, "x", j, "=", i*j)
  print("-" * 30)