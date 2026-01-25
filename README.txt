This mini-project starts from some csv files in data folder regarding a car dealership, there are three tables (along with their columns):
cars.csv (cars inventory), columns: 
    Car_ID,Brand,Model,Year,Color,Engine_Type,Transmission,Price,Quantity_In_Stock,Status 
customers.csv, columns:
    Customer_ID,Name,Gender,Age,Phone,Email,City
sales.csv, columns:
    Sale_ID,Customer_ID,Car_ID,Sale_Date,Quantity,Sale_Price,Payment_Method,Salesperson
The content of these tables is loaded on a PostgreSql database by running loading_script.py, the database has been created beforehand with a CREATE DATABASE cars_db command.
Finally, the content of these tables has been analyzed and queried through pgadmin4, the content of the queries is inside queries.txt file.
It is worth noting how the query nr.2 has highlighted some inconsistencies in the data, in that the number returned is negative, which is not possible since it should represent the current number of cars in stock. 

Project structure:
my_project/
├─ data/
│ ├─ cars.csv
│ ├─ sales.csv
│ └─ customers.csv
├─ scripts/
│ └─ loading_script.py
├─ sql/
│ └─ queries.txt
└─ README.txt
