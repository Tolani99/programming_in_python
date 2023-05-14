"""
Python also has another condition called elif which helps when you have multiple conditions to satisfy. The light switch example is pretty straightforward in that you only have to check for the state of on or off - True or False. In certain conditions, it may not be that easy. Thankfully elif is here to help.

Let's say you want to give a certain discount to customers if they spend over $100. You will also provide an extra discount if that customer is part of a loyalty program. If the customer is not part of the loyalty program and did not spend over a $100, a service charge of 5% is applied.
"""
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))
