import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

#query and print the distinctive businesses with their name, address, zip code, and city
sql = """ SELECT DISTINCT facility_name, facility_address, facility_zip, facility_city
         FROM Inspections i, Violations v
         WHERE i.serial_number = v.serial_number
         ORDER BY facility_name;"""
cursor.execute(sql)
result = cursor.fetchall()
distinctive_businesses = []
for r in result:
    distinctive_businesses.append(r)
print(distinctive_businesses)

#create table PreviousViolations
cursor.execute("""DROP TABLE IF EXISTS PreviousViolations""")
sql = """CREATE TABLE PreviousViolations(
    facility_name VARCHAR(32),
    facility_address VARCHAR(32),
    facility_zip VARCHAR(20),
    facility_city VARCHAR(32));"""
cursor.execute(sql)

#insert data into PreviousViolations
for row in distinctive_businesses:
    format_str = """INSERT INTO PreviousViolations(
    facility_name,
    facility_address,
    facility_zip,
    facility_city)
    VALUES(
    "{facility_name}", 
    "{facility_address}", 
    "{facility_zip}", 
    "{facility_city}");"""
    sql = format_str.format(
    facility_name = row[0], 
    facility_address = row[1], 
    facility_zip = row[2], 
    facility_city = row[3])
    cursor.execute(sql)
    
connection.commit()