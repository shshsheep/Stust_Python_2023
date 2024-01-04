#第二題
class STUSTdrinkShop:
    class Employer:
        def __init__(self, name, Seniority, workinghour):
            # 初始化 Employer 物件的屬性
            self.name = name
            self.Seniority = Seniority
            self.workinghour = workinghour
            self.monthly_salary = ''

        def Inquire_name(self):
            # 查詢姓名
            return self.name

        def Inquire_Seniority(self):
            # 查詢年資
            return self.Seniority

        def Inquire_workinghour(self):
            # 查詢工作時數
            return self.workinghour

        def calculate_monthly_salary(self, day_salary):
            # 計算月薪
            self.monthly_salary = day_salary * self.workinghour * 30
            print(f"{self.name}的月薪是{self.monthly_salary}")

        def increase_working_hours(self, hours):
            # 增加工作時數
            self.workinghour += hours
            print(f"工時已被增加到{self.workinghour}小時")

        def increase_Seniority(self, year):
            # 增加年資
            self.Seniority += year
            print(f"年資已增加到{self.Seniority}年")

class Drink:
    def __init__(self, money, size, ingredient):
        # 初始化 Drink 物件的屬性
        self.money = money
        self.size = size
        self.ingredient = ingredient

    def change_name(self, new_name):
        # 修改飲料名稱
        self.name = new_name
        print(f"名稱已修改為 {self.name}")

    def change_sweetness(self, new_sweetness):
        # 調整甜度
        self.sweetness = new_sweetness
        print(f"甜度已調整為 {self.sweetness}")

    def change_price(self, new_price):
        # 調整價格
        self.money = new_price
        print(f"價錢已調整為 {self.money}")

class ColdDrink(Drink):
    def __init__(self, money, size, ingredient, name, iced, sweet):
        # 初始化 ColdDrink 物件的屬性
        super().__init__(money, size, ingredient)
        self.name = name
        self.iced = iced
        self.sweet = sweet
        self.sweetness = None

    def change_sweetness(self, new_sweetness):
        # 調整冷飲的甜度
        self.sweetness = new_sweetness
        print(f"{self.name}的甜度已調整為 {self.sweetness}")

class HotDrink(Drink):
    def __init__(self, money, size, ingredient, name, sweet):
        # 初始化 HotDrink 物件的屬性
        super().__init__(money, size, ingredient)
        self.name = name
        self.sweet = sweet

        
# 創建 STUSTdrinkShop 類別的實例
drink_shop_instance = STUSTdrinkShop()

# 創建 Employer 物件的實例
employer1 = drink_shop_instance.Employer(name="mike", Seniority=3, workinghour=8)
employer2 = drink_shop_instance.Employer(name="Jhon", Seniority=5, workinghour=6)
employer3 = drink_shop_instance.Employer(name="Andy", Seniority=2, workinghour=5)


# 使用副函式
employer1.calculate_monthly_salary(day_salary=168)
employer1.increase_working_hours(hours=2)
employer1.increase_Seniority(year=3)

employer2.calculate_monthly_salary(day_salary=178)
employer2.increase_working_hours(hours=1)
employer2.increase_Seniority(year=1)

employer3.calculate_monthly_salary(day_salary=186)
employer3.increase_working_hours(hours=4)
employer3.increase_Seniority(year=3)


# 創建 ColdDrink 物件的實例
cold_drink1 = ColdDrink(money=50, size="大杯", ingredient="可樂", name="可樂", iced=True, sweet=True)
cold_drink2 = ColdDrink(money=45, size="中杯", ingredient="檸檬汁", name="檸檬汁", iced=True, sweet=False)
cold_drink3 = ColdDrink(money=65, size="大杯", ingredient="橘子汽水", name="橘子汽水", iced=False, sweet=True)

# 使用副函式
cold_drink1.change_price(60)
cold_drink1.change_name("零卡可樂")
cold_drink1.change_sweetness("少糖")

cold_drink2.change_price(40)
cold_drink2.change_name("超水檸檬汁")
cold_drink2.change_sweetness("全糖")

cold_drink3.change_price(30)
cold_drink3.change_name("橘子汁")
cold_drink3.change_sweetness("半糖")

# 創建 HotDrink 物件的實例
hot_drink1 = HotDrink(money=25, size="中杯", ingredient="茶", name="紅茶", sweet=False)
hot_drink2 = HotDrink(money=30, size="小杯", ingredient="咖啡", name="美式", sweet=True)
hot_drink3 = HotDrink(money=50, size="大杯", ingredient="可可", name="熱可可", sweet=True)

# 使用副函式
hot_drink1.change_name("綠茶")
hot_drink1.change_price(20)
hot_drink1.change_sweetness("全糖")

hot_drink2.change_name("拿鐵")
hot_drink2.change_price(45)
hot_drink2.change_sweetness("無糖")

hot_drink3.change_name("90%可可")
hot_drink3.change_price(70)
hot_drink3.change_sweetness("無糖")
