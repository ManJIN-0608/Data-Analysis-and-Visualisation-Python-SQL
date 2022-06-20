# Data-Analysis-and-Visualisation-Python-SQL
This prohect use **python** to interact with **databases**, **excel workbooks**, perform data analysis using **NumPy**, and use **matplotlib** to generate graphs. 

As more and more industries are becoming data driven, being able to process a large volume of raw data and produce a concise and insightful summary is becoming more and more important. As a data consultant for a government agency, you are tasked with processing some food inspection and health violation data and producing a report summarising some of the information.

The raw data is provided in 2 excel spreadsheets: (A) Inspections.xlsx and (B) Violations.xlsx. They will need to be stored in a database.

## Task 1 – Access the workbooks and create a database
Create a Python script (db_create.py) to perform the following tasks:
- Open the excel files.
- Create a SQLite database with two tables, one for each excel file. Each column in the excelfiles should correspond to a column in the tables. Make sensible decisions for attribute types.
- Import the data from the excel files to the corresponding tables in the database.

## Task 2 – Query the database
Create a Python script (sql_food.py) to perform the following tasks:
- List the distinctive businesses that have had at least 1 violation ordered alphabetically to theconsole and then write their name, address, zip code and city into a new database table called “Previous Violations”.
- Print a count of the violations for each business that has at least 1 violation to the consolealong with their name ordered by the number of violations. *SQL Hint: Group By*

## Task 3 – Excel via Python
Create a Python script (excel_food.py) to perform the following tasks:
- Create a new workbook named “ViolationTypes.xlsx”.
- Create a sheet named “Violations Types”.
- Query the database and calculate the number of each type of violation based on violationcode.
- Write the relevant data into the worksheet you created. This should show the total numberof violations, then list how that is broken down by violation code, including the descriptionof the violation code. For example:

## Task 4 – Numpy in Python
In this task, we are interested in analysing the data points over the time period cocered. You will need to create a Python script (numpy_food.py) to perform the following tasks:
- Use MatPlotLib to plot the follow data over time:
    * The number of violations per month for the postcode with the highest total violations
    * The number of violations per month for the postcode with the lowest total violations
    * The average number of violations per month for ALL of California (ALL postcodes combined). For example, If postcode 1111 has 5 violations during July, 2222 has 4 violations during July, and 3333 has 3 violations for July, then the average violations in July is 4 (12 violations/3 postcodes)
    * The average number of violations per month for all McDonalds compared with the average for all Burger Kings. This will require a new query as it is not grouped by postal code. If there were 3 McDonalds stores with 4, 5 and 9 violations for July, then the average for July would be 6 ((4+5+9)/3 stores)
    * Query the Violations table and retrieve all distinct violation codes and descriptions
    * Using Regular Expressions (NOT SQL), filter the resulting data to print out a list of all violation codes and descriptions that involve the word ‘food’.