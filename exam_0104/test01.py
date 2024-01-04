#第一題
class frychicken : 
    def __init__(self, name, head, leg, wing, chest, hreat) :
        #建立五個屬性and建構子
        self.name = name #顧客名稱
        self.head = head #部位 頭
        self.leg = leg  #部位 腳
        self.wing = wing    #部位 翅膀
        self.chest = chest  #部位 胸
        self.hreat = hreat  #部位 雞心
        self.oilpot = {}
    #建立三個副函式
    def Fry_chicken(self, chicken, time) :
        # 檢查部位是否有效
        if chicken.strip() != "" and chicken in [self.head, self.leg, self.wing, self.chest, self.hreat]:
            # 檢查部位是否已經在油鍋中
            if chicken not in self.oilpot:
                self.oilpot[chicken] = time
                print(f"{self.name} {chicken} 以下油鍋  所需時間 :{time}分鐘")
            else :
                print(f"{self.name} {chicken} 已經在炸了 所需時間 : {time}分鐘")
        else : 
            print(f"{self.name} 你沒有點這部位")

    def Eat_chicken(self, chicken) :
         # 檢查部位是否有效
        if chicken.strip() != "" and chicken in [self.head, self.leg, self.wing, self.chest, self.hreat]:
            # 檢查部位是否已經在油鍋中
            if chicken in self.oilpot:
                del self.oilpot[chicken]
                print(f"{self.name} {chicken} 已經被你吃掉了")
            else :
                print(f"{self.name} {chicken} 沒有這個部位了")
        else : 
            print(f"{self.name} 你沒有點這部位")

    def Inquire(self, chicken) : 
         # 檢查部位是否有效
        if chicken.strip() != "" and chicken in [self.head, self.leg, self.wing, self.chest, self.hreat]:
            # 檢查部位是否已經在油鍋中
            if chicken in self.oilpot:
                print(f"{self.name} {chicken} 在炸了 需要 {self.oilpot[chicken]} 分鐘")
            else :
                print(f"{self.name} {chicken} 你沒有炸這個部位")
        else :
            print(f"{self.name} 你沒有點這部位")

# 創建顧客物件
chickenshop_customer1 = frychicken("顧客1" ," 頭 ", " 腳 ", " 翅膀 ", " 雞胸 ", " 雞心 ")
chickenshop_customer2 = frychicken("顧客2"," 頭 ", "腳", "翅膀", "雞胸", "雞心")
chickenshop_customer3 = frychicken("顧客3","頭", "腳", "翅膀", "雞胸", "雞心")
chickenshop_customer4 = frychicken("顧客4","頭", "腳", "翅膀", "雞胸", "雞心")

# 顧客1的操作
chickenshop_customer1.Fry_chicken(chickenshop_customer1.head, 20)
chickenshop_customer1.Inquire(chickenshop_customer1.wing)
chickenshop_customer1.Eat_chicken(chickenshop_customer1.head)
chickenshop_customer1.Eat_chicken(chickenshop_customer1.leg)

# 顧客2的操作
chickenshop_customer2.Fry_chicken(chickenshop_customer2.chest, 14)
chickenshop_customer2.Inquire(chickenshop_customer2.wing)
chickenshop_customer2.Eat_chicken(chickenshop_customer2.chest)
chickenshop_customer2.Eat_chicken(chickenshop_customer2.leg)

# 顧客3的操作
chickenshop_customer3.Fry_chicken(chickenshop_customer3.wing, 10)
chickenshop_customer3.Inquire(chickenshop_customer3.wing)
chickenshop_customer3.Eat_chicken(chickenshop_customer3.wing)
chickenshop_customer3.Inquire(chickenshop_customer3.wing)

# 顧客4的操作
chickenshop_customer4.Fry_chicken(chickenshop_customer4.hreat, 60)
chickenshop_customer4.Inquire(chickenshop_customer4.wing)
chickenshop_customer4.Eat_chicken(chickenshop_customer4.hreat)
chickenshop_customer4.Eat_chicken(chickenshop_customer4.leg)

