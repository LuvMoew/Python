#40
print('Điểm cao nhất của lớp:', diem_2a.max())
print('Điểm thấp nhất của lớp:', diem_2a.min())
#----------------
for i in range(0, diem_2a.shape[0]):
    print('Môn', i, ': Điểm Max:', diem_2a[i,:].max(),
          'Điểm Min:', diem_2a[i,:].min())
#---------------
for i in range(0, diem_2a.shape[1]):
    print('Học sinh', i, ': Điểm Max:', diem_2a[:,i].max(),
          'Điểm Min:', diem_2a[:,i].min())
#41
#Sum: Tính tổng các phần tử trong mảng
print('Tổng tất cả các điểm trong của lớp 2A:', diem_2a.sum())
print('--------------------------------')

#Tính tổng điểm của từng học sinh:
for i in range(0, diem_2a.shape[1]):
    print('Tổng điểm các môn của học sinh', i, ':', diem_2a[:,i].sum())

#43
# a.mean(): Giá trị trung bình của mảng a
print('Điểm trung bình của cả lớp 2A:', diem_2a.mean())
print('')
#Tính điểm trung bình của các học sinh trong lớp:
#CÁCH 1:
for i in range(0, diem_2a.shape[1]):
    print('Điểm trung bình của học sinh', i, ':', diem_2a[:,i].mean())
#----------------
#Tính điểm trung bình của các học sinh trong lớp:
#CÁCH 2:
mean_2a = diem_2a.mean(axis=0)
#axis = 0: theo hàng
#axis = 1: theo cột
for i in range(0,mean_2a.size):
    print('Điểm trung bình của học sinh', i, ':', mean_2a[i])

#44
# median(): Giá trị trung vị trong một tập hợp các phần tử.
# Trường hợp số phần tử trong mảng là lẻ
a = diem_2a[1:15]

print('Mảng a ban đầu: \n', a)
print('Số phần tử trong mảng a: ', a.size)
print('Mảng a đã sắp xếp: \n', np.sort(a))
print('Giá trị trung bình mean:', np.mean(a))
print('Giá trị trung vị median:', np.median(a))

#45
# C): Mode: là giá trị xuất hiện nhiều nhất trong tập hợp.
# Trong trường hợp không có giá trị nào được lặp lại thì không có Mode.
# Liệt kê điểm xuất hiện nhiều nhất theo từng môn học

from scipy import stats as sp  # sử dụng thư viện scipy để dùng hàm mode

for i in range(0, diem_2a.shape[0]):
    a = sp.mode(diem_2a[i,:])
    print('Môn', i, ': Điểm xuất hiện nhiều nhất: ', a[0], ', số lần: ', a[1])
    print(type(a))

#46
# D): Range: là sự khác biệt, khoảng cách giữa phần tử dưới và phần tử trên,
# giữa giá trị nhỏ nhất (Min) với giá trị lớn nhất (Max) trong tập hợp.
# Xác định độ chênh điểm max - min của từng học sinh

for i in range(0, diem_2a.shape[1]):
    print('Độ chênh điểm của học sinh', i, ':', 
          diem_2a[i,:].max() - diem_2a[i,:].min())

#47
# E) Std: Tính độ lệch chuẩn
a = np.array([10, 1, 1, 9, 12, 1, 9, 12, 10])
print('Phần tử của mảng a:', a)
print('Giá trị trung bình:', a.mean())
print('Độ lệch chuẩn:', a.std())

print('--------------------------------')

b = np.array([7, 7, 8, 7, 8, 7, 7, 7, 7])
print('Phần tử của mảng b:', b)
print('Giá trị trung bình:', b.mean())
print('Độ lệch chuẩn:', b.std())