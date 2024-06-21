#รถไฟฟ้า ระบบ payment

payment =  int(input("กรุณาใส่ราคา : "))

ticket = int(input("ราคาตั๋ว : "))

change = (payment - ticket)

coin_10 = int(change // 10)
change %= 10

coin_5 = int(change // 5) 
change %= 5

coin_2 = int(change // 2) 
change %= 2

coin_1 = int(change // 1)

print(f'เงินทอนที่ได้รับ :{payment - ticket}บาท')

print(f'เหรียญ 10 ที่ได้รับ : ',coin_10,'เหรียญ')
print(f'เหรียญ 5 ที่ได้รับ : ',coin_5,'เหรียญ')
print(f'เหรียญ 2 ที่ได้รับ : ',coin_2,'เหรียญ')
print(f'เหรียญ 1 ที่ได้รับ : ',coin_1,'หรียญ')
