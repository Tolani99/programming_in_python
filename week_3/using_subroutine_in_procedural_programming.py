def calculate_tax(percent, bill_total):
    return round((percent * bill_total) / 100.0, 2)
Food_bill = {
        1: 3.99, 
        2: 4.55,
        3: 11.99,
        4: 22.00,
        5: 2.00
        }
food_total = bill_total(food_bill)
tax_total = calculate_tax(15, food_total)

print('Overall:', food_total + total_total)
