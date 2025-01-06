print("Bài 15_a: Viết hàm cho các bài đã thực hiện")

# 1) Hàm greeting(): Trả về câu chào với họ tên và năm sinh
def greeting(name, birth_year):
    """
    Trả về câu chào với họ tên và năm sinh.

    Args:
        name (str): Họ tên.
        birth_year (int): Năm sinh.

    Returns:
        str: Câu chào.
    """
    current_year = 2025  # Năm hiện tại
    age = current_year - birth_year
    return f"Xin chào {name}, năm nay bạn {age} tuổi!"

# 2) Hàm rabbit_count(): Tính số thỏ trong rừng sau số tháng cho trước
def rabbit_count(months):
    """
    Tính số thỏ trong rừng sau số tháng cho trước.

    Args:
        months (int): Số tháng.

    Returns:
        int: Số thỏ trong rừng.
    """
    if months <= 0:
        return 0
    elif months == 1 or months == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, months + 1):
        a, b = b, a + b
    return b

# 3) Hàm count_mark(): Trả về số sinh viên học lại và tổng số sinh viên
def count_mark(marks):
    """
    Tính số sinh viên học lại và tổng số sinh viên trong lớp.

    Args:
        marks (list): Danh sách điểm của sinh viên.

    Returns:
        tuple: (Số sinh viên học lại, Tổng số sinh viên).
    """
    total_students = len(marks)
    failed_students = sum(1 for mark in marks if mark < 5.0)
    return failed_students, total_students

# Chương trình chính
if __name__ == "__main__":
    # 1) Greeting
    print("\n1) Greeting:")
    name = input("Nhập họ tên của bạn: ")
    birth_year = int(input("Nhập năm sinh của bạn: "))
    print(greeting(name, birth_year))

    # 2) Rabbit count
    print("\n2) Rabbit Count:")
    months = int(input("Nhập số tháng: "))
    print(f"Số thỏ trong rừng sau {months} tháng là {rabbit_count(months)}.")

    # 3) Count mark
    print("\n3) Count Mark:")
    marks_input = input("Nhập danh sách điểm của sinh viên (cách nhau bởi dấu phẩy): ")
    marks = [float(mark.strip()) for mark in marks_input.split(",")]
    failed, total = count_mark(marks)
    print(f"Số sinh viên học lại: {failed}")
    print(f"Tổng số sinh viên: {total}")
#
#---
#---------------------------------
print("Bài 15_b: Viết hàm cho các bài đã thực hiện")
# 4) Hàm bmi_show(): Nhận xét dựa trên chỉ số BMI
def bmi_show(weight, height):
    """
    Trả về nhận xét dựa trên chỉ số BMI.

    Args:
        weight (float): Cân nặng (kg).
        height (float): Chiều cao (m).

    Returns:
        str: Nhận xét dựa trên chỉ số BMI.
    """
    if height <= 0:
        return "Chiều cao không hợp lệ!"
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"BMI = {bmi:.2f}: Bạn gầy."
    elif bmi < 25:
        return f"BMI = {bmi:.2f}: Bạn bình thường."
    elif bmi < 30:
        return f"BMI = {bmi:.2f}: Bạn thừa cân."
    else:
        return f"BMI = {bmi:.2f}: Bạn béo phì."

# 5) Hàm cal_point(): Tính điểm trung bình hệ 10 và hệ 4
def cal_point(scores):
    """
    Tính điểm trung bình hệ 10 và hệ 4 từ danh sách điểm.

    Args:
        scores (list): Danh sách điểm (hệ 10).

    Returns:
        tuple: (Điểm trung bình hệ 10, Điểm trung bình hệ 4).
    """
    def to_gpa(score):
        if score >= 9.0:
            return 4.0
        elif score >= 8.0:
            return 3.5
        elif score >= 7.0:
            return 3.0
        elif score >= 6.0:
            return 2.5
        elif score >= 5.0:
            return 2.0
        elif score >= 4.0:
            return 1.0
        else:
            return 0.0

    total_students = len(scores)
    avg_10 = sum(scores) / total_students
    avg_4 = sum(to_gpa(score) for score in scores) / total_students
    return avg_10, avg_4

# 6) Hàm list_prime(): Danh sách các số nguyên tố từ 1 đến n
def list_prime(n):
    """
    Trả về danh sách các số nguyên tố trong khoảng từ 1 đến n.

    Args:
        n (int): Số nguyên dương lớn nhất trong khoảng.

    Returns:
        list: Danh sách các số nguyên tố từ 1 đến n.
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    return [i for i in range(1, n + 1) if is_prime(i)]

# Chương trình chính
if __name__ == "__main__":
    # 4) BMI Show
    print("\n4) BMI Show:")
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))
    print(bmi_show(weight, height))

    # 5) Tính điểm trung bình
    print("\n5) Tính điểm trung bình:")
    scores_input = input("Nhập danh sách điểm hệ 10 của học sinh (cách nhau bởi dấu phẩy): ")
    scores = [float(score.strip()) for score in scores_input.split(",")]
    avg_10, avg_4 = cal_point(scores)
    print(f"Điểm trung bình hệ 10: {avg_10:.2f}")
    print(f"Điểm trung bình hệ 4: {avg_4:.2f}")

    # 6) Danh sách số nguyên tố
    print("\n6) Danh sách số nguyên tố:")
    n = int(input("Nhập số nguyên dương n: "))
    primes = list_prime(n)
    print(f"Các số nguyên tố từ 1 đến {n} là: {primes}")
#
#---------
#--------------------------------------------------
print("Bài 16: Xây dựng lớp Person")
class Person:
    """
    Lớp Person mô tả thông tin cá nhân.

    Attributes:
        name (str): Họ tên của người.
        height (float): Chiều cao (m).
        weight (float): Cân nặng (kg).

    Methods:
        greeting(): Hiển thị thông tin cá nhân.
        bmi(): Tính toán và trả về chỉ số BMI.
    """
    def __init__(self, name="Nguyễn Văn A", height=1.7, weight=65):
        """
        Khởi tạo đối tượng Person với giá trị mặc định.

        Args:
            name (str): Họ tên. Mặc định là "Nguyễn Văn A".
            height (float): Chiều cao (m). Mặc định là 1.7.
            weight (float): Cân nặng (kg). Mặc định là 65.
        """
        self.name = name
        self.height = height
        self.weight = weight

    def greeting(self):
        """Hiển thị thông tin của Person."""
        print(f"Họ tên: {self.name}")
        print(f"Chiều cao: {self.height:.2f} m")
        print(f"Cân nặng: {self.weight:.2f} kg")

    def bmi(self):
        """
        Tính toán và trả về chỉ số BMI của Person.

        Returns:
            str: Chỉ số BMI và nhận xét sức khỏe.
        """
        if self.height <= 0:
            return "Chiều cao không hợp lệ!"
        bmi = self.weight / (self.height ** 2)
        if bmi < 18.5:
            return f"BMI = {bmi:.2f}: Bạn gầy."
        elif bmi < 25:
            return f"BMI = {bmi:.2f}: Bạn bình thường."
        elif bmi < 30:
            return f"BMI = {bmi:.2f}: Bạn thừa cân."
        else:
            return f"BMI = {bmi:.2f}: Bạn béo phì."

# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin từ người dùng
    print("Nhập thông tin cho Person:")
    name = input("Nhập họ tên: ")
    height = float(input("Nhập chiều cao (m): "))
    weight = float(input("Nhập cân nặng (kg): "))

    # Khởi tạo đối tượng Person mới với thông tin người dùng nhập
    person = Person(name, height, weight)

    # Hiển thị thông tin và tính chỉ số BMI cho đối tượng mới
    print("\nThông tin cá nhân:")
    person.greeting()

    print("\nChỉ số BMI:")
    print(person.bmi())
#
#
#---------------------------------------------------------------
def swap_largest_and_smallest(filename_in, filename_out):
    try:
        # Đọc dữ liệu từ file dayso1_bai17.txt
        with open(filename_in, 'r') as file:
            # Đọc dãy số từ file và chuyển thành danh sách số nguyên
            data = file.read().strip().split()
            
            # Kiểm tra dữ liệu có phải là số nguyên không
            if not all(item.isdigit() for item in data):
                raise ValueError("File chứa dữ liệu không phải là số nguyên.")
            
            numbers = [int(num) for num in data]

        # Kiểm tra nếu dãy số quá ngắn (chỉ có 1 phần tử)
        if len(numbers) < 2:
            raise ValueError("Dãy số trong file quá ngắn, không thể đổi chỗ phần tử.")

        # Tìm phần tử lớn nhất và nhỏ nhất trong dãy
        max_num = max(numbers)
        min_num = min(numbers)

        # Tìm vị trí của phần tử lớn nhất và nhỏ nhất đầu tiên
        max_index = numbers.index(max_num)
        min_index = numbers.index(min_num)

        # Đổi chỗ phần tử lớn nhất và nhỏ nhất
        numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

        # Ghi dãy mới vào file dayso2_bai17.txt
        with open(filename_out, 'w') as file:
            file.write(' '.join(map(str, numbers)))
        
        print("Đã đổi chỗ phần tử lớn nhất và nhỏ nhất thành công!")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filename_in}.")
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm để thực hiện yêu cầu
swap_largest_and_smallest('dayso1_bai17.txt', 'dayso2_bai17.txt')
