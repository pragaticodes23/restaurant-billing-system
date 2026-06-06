print("======RESTAURANT BILL & DISCOUNT SYSTEM======")
customer_name=input("Enter customer name:")
membership_status=input("Are you a member?").lower()
weekend_status=input("Is it a weekend?").lower()
bill_amount=float(input("Enter total bill amount:"))
bill_discount=0
member_discount=0
weekend_discount=0

if bill_amount<=1000:
    print("No discount")
    
elif bill_amount>1000 and bill_amount<=4999:
    bill_discount=bill_amount*10/100
    print("10% discount available")
    
else:
    bill_discount=bill_amount*15/100
    print("15% discount available")
    
if membership_status=="yes":
    member_discount=bill_amount*5/100
    print("Extra 5% discount to members")
    
else:
    print(" No membership discount")
    
if weekend_status=="yes":
    weekend_discount=bill_amount*5/100
    print("Extra 5% discount available on weekend")
    
else:
    print("No weekend discount")
    
total_discount=bill_discount+member_discount+weekend_discount
final_bill=bill_amount-total_discount

print('Bill discount:',bill_discount)
print('Membership discount:',member_discount)
print('Weekend_discount:',weekend_discount)
print('The total discount is:',total_discount)
print(customer_name,'The final bill amount is:',final_bill)
print('Thank you for visiting us.Visit soon!!')
    
