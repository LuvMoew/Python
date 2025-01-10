#Trang13
import numpy as np

# Tạo mảng 1 chiều (1D) - row
a = np.array([1, 2, 5, 7, 0, 8])

print(a)
print("Loại dữ liệu của biến a:", type(a))
print("Kiểu dữ liệu của phần tử trong mảng a:", a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:", a.size)
print("Số chiều của mảng a:", a.ndim)
#
#-------------------------------------------------
#Trang14
import numpy as np

# Tạo mảng 2 chiều (2D - Ma trận)
b = np.array([(4, 5, 6.0), (1, 2, 3.5)])

print(b)
print("Loại dữ liệu của biến b:", type(b))

print("Kiểu dữ liệu của phần tử trong mảng b:", b.dtype)
print("Kích thước của mảng b:", b.shape)

print("Số phần tử của mảng b:", b.size)
print("Số chiều của mảng b:", b.ndim)
#
#---------------------------------------------------
#Trang15
import numpy as np

c = np.array([[(2,4,0,6), (4,7,5,6)],
              [(0,3,2,1), (9,4,5,6)],
              [(5,8,6,4), (1,4,6,8)]]) #mảng 3 chiều (3D)

print(c)
print("Phần tử đầu tiên của mảng c:", c[0,0,0])
print("Kiểu dữ liệu của phần tử trong mảng c:", c.dtype)
print("Kích thước của mảng c:", c.shape)
print("Số phần tử của mảng c:", c.size)
print("Số chiều của mảng c:", c.ndim)
#
#---------------------------------------------------
#Trang18
import numpy as np

array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)
#--------
import numpy as np

array_one = np.ones((3, 5), dtype=np.int)

print(array_one)
print("Kiểu dữ liệu trong mảng array_one:", array_one.dtype)
print("Kích thước của mảng array_one:", array_one.shape)
print("Số phần tử của mảng array_one:", array_one.size)
print("Số chiều của mảng array_one:", array_one.ndim)
#
#---------------------------------------------------
#Trang19
import numpy as np

array_eye = np.eye(5)

print(array_eye)
print("Kiểu dữ liệu của phần tử trong mảng array_eye:", array_eye.dtype)
print("Kích thước của mảng array_eye:", array_eye.shape)
print("Số phần tử của mảng array_eye:", array_eye.size)
print("Số chiều của mảng array_eye:", array_eye.ndim)
#
#---------------------------------------------------
#Trang20
import numpy as np

array_random = np.random.random((7, 5))

print(array_random)
print("Kiểu dữ liệu của phần tử trong mảng array_random:", array_random.dtype)
print("Kích thước của mảng array_random:", array_random.shape)
print("Số phần tử của mảng array_random:", array_random.size)
print("Số chiều của mảng array_random:", array_random.ndim)
#
#---------------------------------------------------
#Trang21
import numpy as np

# Tạo một vector gồm 10 số nguyên ngẫu nhiên trong khoảng từ 1 đến 10
vector = np.random.randint(1, 11, size=10)
print(vector)

# Tạo một ma trận 3x4 với các phần tử là số nguyên ngẫu nhiên từ -5 đến 5
matrix = np.random.randint(-5, 6, size=(3, 4))
print(matrix)
#
#---------------------------------------------------
#Trang22
import matplotlib.pyplot as plt

# Tạo một vector x với 100 phần tử từ 0 đến 10
x = np.linspace(0, 10, 100)

# Tính giá trị hàm sin tại các điểm trong vector x
y = np.sin(x)

# Vẽ đồ thị hàm sin
plt.plot(x, y)
plt.show()
#
#---------------------------------------------------
#Trang28
a_float = np.linspace(0,15,11)
print(a_float)
print('Kiểu Dữ liệu: ', a_float.dtype)

a_int = a_float.astype(np.int16)
print(a_int)
print('Dữ liệu sau khi chuyển: ', a_int.dtype)
#----------
# Chuyển từ kiểu float --> int
a_str = a_int.astype(np.str)
print(a_str)
print('Dữ liệu sau khi chuyển: ', a_str.dtype)

# Chuyển từ kiểu float --> boolean
a_bol = a_int.astype(np.bool)
print(a_bol)
print('Dữ liệu sau khi chuyển:', a_bool.dtype)
#
#---------------------------------------------------
#Trang31
import numpy as np

# Tạo một mảng NumPy
a = np.array([3, 5, 10, 19, 8, 1, 9, 8, 3, 1])
# In ra các phần tử của mảng
print("Các phần tử của vector 'a':\n", a)
# Truy cập phần tử đầu tiên
print("Phần tử đầu tiên:", a[0])
# Truy cập phần tử thứ 3 (vị trí index là 2)
print("Phần tử thứ 3:", a[2])
# Truy cập phần tử cuối cùng
print("Phần tử cuối cùng:", a[-1])

#-------------

# Truy cập nhiều phần tử của vector 'a'
print("Các phần tử của vector 'a':\n", a)
# 3 phần tử đầu tiên
print("3 phần tử đầu tiên:", a[:3])
# Từ phần tử thứ 5 tới hết
print("Từ phần tử thứ 5 tới hết:", a[5:])
# Từ phần tử thứ 2 đến phần tử thứ 6 (không bao gồm phần tử thứ 6)
print("Từ phần tử thứ 2 đến phần tử thứ 6 của vector:", a[2:6])
#
#---------------------------------------------------
#Trang32
# Truy cập tới 1 phần tử của ma trận (2D): a[index_row, index_col]
print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0,0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[2,1])
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1,-1])
print()

print('Bảng điểm lớp 2A:\n', diem_2a)
#
#---------------------------------------------------
#Trang33
# Truy cập tới nhiều phần tử trong ma trận: a[index_row1:index_row2, index_col1:index_col2]
# Lấy điểm tất cả các môn (tất cả các hàng) của học sinh 5:
diem_hs5 = diem_2a[:, 5]
print("Điểm các môn của học sinh 5:", diem_hs5)
# Lấy điểm môn học cuối cùng của tất cả học sinh (tất cả các cột)
diem_mon = diem_2a[-1, :]
print("Điểm môn học cuối cùng của tất cả học sinh: \n", diem_mon)
# Lấy điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = diem_2a[:5, :10]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp: \n", diem5_hs10)
#
#---------------------------------------------------