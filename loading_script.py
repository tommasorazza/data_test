import pandas as pd
from sqlalchemy import create_engine

engine=create_engine('postgresql://postgres:new_postgres@localhost:5432/cars_db')

df=pd.read_csv('/home/razza/cars/cars.csv')

df.to_sql(
        name='cars',
        con=engine,
        index=False,
        if_exists='replace')

df=pd.read_csv('/home/razza/cars/customers.csv')

df.to_sql(
        name='customers',
        con=engine,
        index=False,
        if_exists='replace')

df=pd.read_csv('/home/razza/cars/sales.csv')

df.to_sql(
        name='sales',
        con=engine,
        index=False,
        if_exists='replace')

print('success')
