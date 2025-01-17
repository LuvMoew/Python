
# Yêu cầu: Tạo một vector gồm 30 phần tử, có giá trị tăng dần từ 1 đến 30. 
# Chỉ sử dụng các phương thức reshape, ravel, split…tách Vector a ở trên thành 3 vector con 
#bao gồm: 
# • a_lẻ: chứa các phần tử là số lẻ; 
# • a_chan: chứa các phần tử là số chẵn. 
# • a_3: chứa các phần tử chia hết cho 3 
import numpy as np

# Tạo vector gồm 30 phần tử tăng dần từ 1 đến 30
a = np.arange(1, 31)

a_reshaped = a.reshape(6, 5, order ='C') 
#1 2 3 4 5 6
#7 8 9 10 11 12

# 1 2 3 4 5 6 7 8 9 10 11 12
a_flattened = a_reshaped.ravel()

# tach a_flattened thanh 3 nhom 
split_vectors = np.split(a_flattened, 3)

# Tách các vector con 
a_lẻ = np.array([x for x in a_flattened if x % 2 != 0]).reshape(-1) #so chan
a_chan = np.array([x for x in a_flattened if x % 2 == 0]).reshape(-1) #so le
a_3 = np.array([x for x in a_flattened if x % 3 == 0]).reshape(-1) # chi het cho 3 

print("Vector a:", a)
print("a_lẻ:", a_lẻ)
print("a_chẵn:", a_chan)
print("a_3:", a_3)

#
#------------------------------------------------------
#
# File dữ liệu Data_BMI.txt lưu trữ thông tin chiều cao, cân nặng của 100 người.
import numpy as np

# Đọc dữ liệu từ file
file_path = 'C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt'
data = np.loadtxt(file_path)

# Tách chiều cao và cân nặng
heights_cm = data[:, 0]  # Cột 1: Chiều cao (cm)
weights_kg = data[:, 1]  # Cột 2: Cân nặng (kg)

# Chuyển đổi chiều cao từ cm sang mét
heights_m = heights_cm / 100.0

# Tính chỉ số BMI
bmi_values = weights_kg / (heights_m ** 2)

# Phân loại BMI
categories = []
for bmi in bmi_values:
    if bmi < 18.5:
        categories.append("Underweight")
    elif 18.5 <= bmi < 25:
        categories.append("Normal")
    elif 25 <= bmi < 30:
        categories.append("Overweight")
    elif 30 <= bmi < 35:
        categories.append("Obese")
    else:
        categories.append("Extremely Obese")

for i, (height, weight, bmi, category) in enumerate(zip(heights_cm, weights_kg, bmi_values, categories)):
    print(f"Person {i+1}: Height = {height} cm, Weight = {weight} kg, BMI = {bmi:.2f}, Category = {category}")
#
#
#-----------------------------------------------------------
#
import numpy as np

data = np.loadtxt("C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt")  # Đọc file, dữ liệu dạng ma trận
v_height = data[:, 0] 

v_height_m = v_height / 100

v_height_m2 = v_height_m ** 2

print("Chiều cao (m):", v_height_m)
print("Chiều cao bình phương (m^2):", v_height_m2)
#
#
#----------------------------------------------------
#
import numpy as np

# Đọc dữ liệu từ file Data_BMI.txt
data = np.loadtxt('C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt')

# Tách dữ liệu chiều cao (Height) và cân nặng (Weight)
v_height = data[:, 0] / 100  # Chuyển đổi chiều cao từ cm sang m
v_weight = data[:, 1]       # Cân nặng (kg)

# Tính chỉ số BMI
v_bmi = np.round(v_weight / np.square(v_height), 1)  # Làm tròn tới 1 chữ số

# In kết quả
print("Vector BMI:", v_bmi)

#
#--------------------------------------
#
#
def calculate_bmi(height, weight):
    height_m = height / 100
    return weight / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Extremely Obese"

bmi_categories = {
    "Underweight": 0,
    "Normal": 0, 
    "Overweight": 0,
    "Obese": 0,
    "Extremely Obese": 0
}

try:
    with open('C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt', 'r') as file:
        for line in file:
            height, weight = map(float, line.strip().split())
            bmi = calculate_bmi(height, weight)
            category = classify_bmi(bmi)
            bmi_categories[category] += 1
            
    total = sum(bmi_categories.values())
    print(f"Tổng số: {total}")
    print("-" * 40)
    for i, (category, count) in enumerate(bmi_categories.items(), 1):
        print(f"{i}. {category:<15}: {count}")

except FileNotFoundError:
    print("Error: File Data_BMI.txt not found")
except Exception as e:
    print(f"Error occurred: {e}")