bill_amount = float(input("What is the total bill amount? $"))
person_count = int(input("How many persons do you want to split the bill in? "))
tip_percentage = int(input("What percentage of tip would you like to give? "))

each_person_pay = bill_amount/person_count
net_each_person_pay = each_person_pay + (each_person_pay*(tip_percentage/100))

print(f"\nEach person pays ${net_each_person_pay}")