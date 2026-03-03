import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()
names = re.findall(r'\d+\.\n(.*?)\n', text)
prices = re.findall(r'Стоимость\n([\d\s,]+)', text)

total_3 = 0.0
count = 0 

print("СПИСОК:")
for i in range(len(prices)):
    if count == 3:
        break
        
    price_raw = prices[i].split('\n')[0].strip()
    clean_num = price_raw.replace(' ', '').replace(',', '.')
    
    if clean_num:
        name = names[i].strip()
        print(f"- {name}: {price_raw} тг")
        
        total_3 += float(clean_num)
        count += 1

print("-" * 20)
print(f"ИТОГО ЗА 3 ТОВАРА: {total_3} тг")
