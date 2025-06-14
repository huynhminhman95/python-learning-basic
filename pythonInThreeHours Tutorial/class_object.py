# Class và Object

# Class bao gôm như 1 bản thiêt ke gom cac: thuoc tính, phuong thuc
# Object : doi tuong

class Car:
    # all func class luon co func init
    def __init__(self, parameterName, parameterBrand, parameterColor):
        self.name = parameterName # thuoc tinh self.name la thuoc tính class Car
        self.brand = parameterBrand
        self.color = parameterColor

    def drive(self):
        print(f"Ban dang lai chiec xe {self.name} mau {self.color} cua hang xe {self.brand}")

# tao 1 doi tuong. dat ten cho doi tuong. goi func class.truyen vao tham so
kiaMorning = Car("KIA Morning", "KIA", "xanh duong")
kiaMorning.drive()

ferrariTributo = Car("Ferrari F8 Tributo", "Ferrari", "mau do")
ferrariTributo.drive()