import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

#query the number of each business's zip code has at least 1 violation sorted by violations 
# sql = """ SELECT facility_zip, count(v.serial_number), strftime('%Y%m', activity_date)
#          FROM Inspections i, Violations v
#          WHERE i.serial_number = v.serial_number
#          GROUP BY facility_zip, strftime('%Y%m', activity_date)
#          ORDER BY count(v.serial_number);"""
# cursor.execute(sql)
# zip_violations = cursor.fetchall()
# print(zip_violations)

sql = """   SELECT facility_zip, count(v.serial_number), count(distinct strftime('%Y%m', activity_date))
            FROM Inspections i, Violations v
            WHERE i.serial_number = v.serial_number
            GROUP BY facility_zip
            HAVING count(distinct strftime('%Y%m', activity_date))=30
            ORDER BY count(v.serial_number);"""
cursor.execute(sql)
zip_violations = cursor.fetchall()
# print(zip_violations)

#the postcode with the highest total violations is the last tuple in zip_violations
#the postcode with the lowest total violations is the first tuple in zip_violations
highest_zip = zip_violations[-1][0]
lowest_zip = zip_violations[0][0]
# print(highest_zip)
# print(lowest_zip)

#query the number of violations per month for the postcode with the highest total violations
sql = """ SELECT facility_zip, count(*), strftime('%Y%m', activity_date)
          FROM Inspections i, Violations v
          WHERE i.serial_number = v.serial_number and facility_zip ='"""+highest_zip+"""'
          GROUP BY facility_zip, strftime('%Y%m', activity_date);"""
cursor.execute(sql)
highest_zip_month_violations = cursor.fetchall()
# print(highest_zip_month_violations)

#query the number of violations per month for the postcode with the lowest total violations
sql = """ SELECT facility_zip, count(*), strftime('%Y%m', activity_date)
          FROM Inspections i, Violations v
          WHERE i.serial_number = v.serial_number and facility_zip = '"""+lowest_zip+"""'
          GROUP BY facility_zip, strftime('%Y%m', activity_date);"""
cursor.execute(sql)   
lowest_zip_month_violations = cursor.fetchall()
# print(lowest_zip_month_violations)

#loop highest_zip_month_violations to get the time and the highest number of violations each month in two lists
highest_time = []
highest_values = []
for data in highest_zip_month_violations: # [('91748', 377, '201507'),()...]
    highest_time.append(data[2])
    highest_values.append(data[1])

# plt.plot(highest_time, highest_values)
# plt.show()


#loop lowest_zip_month_violations to get the time and the lowest number of violations each month in two lists
# lowest_time = [] 
# lowest_values = []
# for data in lowest_zip_month_violations:
#     time = data[2]
#     value = data[1]
# for j in highest_time:
#     if j not in lowest_time:
#         lowest_time.append(j)
#         if j == time:
#             lowest_values.append(value)
#         else:
#             lowest_values.append(0)
# print(lowest_values)
lowest_time = []
lowest_values = []
for data in lowest_zip_month_violations: # [('90089', 9, '201507'),('90089', 4, '201508')...]
    lowest_time.append(data[2])
    lowest_values.append(data[1])

# plt.plot(lowest_time, lowest_values)
# plt.show()

#query the the number of distinct postcode and the total violations
sql = """ SELECT strftime('%Y%m', activity_date), count(DISTINCT facility_zip), count(*)
          FROM Inspections i, Violations v
          WHERE i.serial_number = v.serial_number and facility_state = 'CA'
          GROUP BY strftime('%Y%m', activity_date)
          ORDER BY activity_date;"""
cursor.execute(sql)
ca_month_violations = cursor.fetchall()

#loop ca_month_violations to get the time and the average number of violations each month in two lists
avg_time = []
avg_values = []
for data in ca_month_violations:
    avg_time.append(data[0])
    avg_values.append(data[2]//data[1])

# plt.plot(avg_time, avg_values)
# plt.show()

#plot two lines that the highest total violations and the average number of violations each month
# fig, ax1 = plt.subplots() 
# ax1.plot(highest_time, highest_values,'r-', label = 'Highest')
# ax1.plot(avg_time, avg_values, 'g-', label = 'Average')
# ax1.legend()
# plt.xticks(rotation=90)
# plt.xlabel('Time')
# plt.ylabel('Violations')
# # 设置数字标签
# for a, b in zip(highest_time, highest_values):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
# for a, b in zip(avg_time, avg_values):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
# plt.show()

#plot two lines that the lowest total violations and the average number of violations each month
# fig, ax2 = plt.subplots() 
# ax2.plot(lowest_time, lowest_values, 'b-', label = 'Lowest')
# ax2.plot(avg_time, avg_values, 'g-', label = 'Average')
# ax2.legend()
# plt.xticks(rotation=90)
# plt.xlabel('Time')
# plt.ylabel('Violations')
# # 设置数字标签
# for a, b in zip(lowest_time, lowest_values):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
# for a, b in zip(avg_time, avg_values):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
# plt.show()

connection = sqlite3.connect('company.db')
cursor = connection.cursor()

#query the distinct id and the total number of violations for all McDonalds
sql = """ SELECT strftime('%Y%m', activity_date), count(DISTINCT facility_id), count(*)
          FROM Inspections i, Violations v
          WHERE i.serial_number = v.serial_number and facility_name LIKE '%McDonald%'
          GROUP BY strftime('%Y%m', activity_date)
          ORDER BY activity_date;"""
cursor.execute(sql)
mc_month_violations = cursor.fetchall()

#query the distinct id and the total number of violations for all Burger Kings
sql = """ SELECT strftime('%Y%m', activity_date), count(DISTINCT facility_id), count(*)
          FROM Inspections i, Violations v
          WHERE i.serial_number = v.serial_number and facility_name LIKE '%Burger King%'
          GROUP BY strftime('%Y%m', activity_date)
          ORDER BY activity_date;"""
cursor.execute(sql)
bk_month_violations = cursor.fetchall()

#loop mc_month_violations to get the time and the average number of violations per month for all McDonalds 
mc_time = []
mc_values = []
for data in mc_month_violations:
    mc_time.append(data[0])
    mc_values.append(data[2]//data[1])

#loop bk_month_violations to get the time and the average number of violations per month for all Burger Kings     
bk_time = []
bk_values = []
for data in bk_month_violations:
    bk_time.append(data[0])
    bk_values.append(data[2]//data[1])

#plot two lines that the McDonalds average violations and the Burger Kings average violations each month    
fig, ax3 = plt.subplots() 
ax3.plot(mc_time, mc_values,'r-', label = 'McDonald')
ax3.plot(bk_time, bk_values, 'b-', label = 'Burger King')
ax3.legend()
plt.xticks(rotation=90)
plt.xlabel('Time')
plt.ylabel('Violations')
# 设置数字标签
for a, b in zip(mc_time, mc_values):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
for a, b in zip(bk_time, bk_values):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
fig.tight_layout()
plt.show()

# Query the Violations table and retrieve all distinct violation codes and descriptions
sql = """ SELECT distinct v.violation_code, v.violation_description
          FROM Violations v
          ORDER BY v.violation_code;"""
cursor.execute(sql)
violation_code_desc = cursor.fetchall()
# print(violation_code_desc)

import re

result = []
for i in range(len(violation_code_desc)):
    if re.search('food', violation_code_desc[i][1]) != None:
        result.append(violation_code_desc[i])
print(result)