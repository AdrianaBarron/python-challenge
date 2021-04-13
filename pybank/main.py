import os
import csv


file_to_load = os.path.join('Resources', 'budget_data.csv')
month_list = []


with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)

    for row in reader:
        month_list.append(row)


print (month_list)
num_months = 0
sum_revenue = 0




# loop through month_list
# add one to nums_month in each loop iteration
for i in range(len(month_list)):
    num_months += 1

    month_info =  month_list[i]

    month = month_info[0]
    month_rev = month_info[1]
    sum_revenue += int(month_rev)


print (sum_revenue)

print (num_months)




total_profit_per_month = []

#print(total_profit_per_month)


#Don't compare 1st month
for i in range(len(month_list)):
    if i != 0:
        curr_month_profit = float(month_list[i][1])
        prev_month_profit = float(month_list[i-1][1])
        
        #subtract current month from previous month profit
        diff_month_profit = curr_month_profit - prev_month_profit
        total_profit_per_month.append(diff_month_profit)

print(sum(total_profit_per_month) / num_months)

'''current_profit_loss = int(row[1])
total_profit_loss += current_profit_loss

if (num_months == 1):
        previous_profit_loss = current_profit_loss

else:
        profit_change = current_profit_loss - previous_profit_loss

        months.append(row[0])

        profit_change.append(profit_change)

        previous_profit_loss = current_profit_loss


#Assign variables for profits'''




