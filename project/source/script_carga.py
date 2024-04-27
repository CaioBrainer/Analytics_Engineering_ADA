import pandas as pd
from sqlalchemy import create_engine


# Carga dos dados
df_calendar_raw = pd.read_csv("../data/calendar.csv")
df_listings_raw = pd.read_csv("../data/listings.csv")
df_reviews_raw = pd.read_csv("../data/reviews.csv")


db_name = "analytics_engineering_ada"
conn_string = f"postgresql://postgres:552277@localhost:5432/{db_name}"
engine = create_engine(conn_string)

df_listings_raw.to_sql('listings_raw', engine, schema='public', if_exists='append', index=False, chunksize=100000)
df_calendar_raw.to_sql('calendar_raw', engine, schema='public', if_exists='append', index=False, chunksize=100000)
df_reviews_raw.to_sql('reviews_raw', engine, schema='public', if_exists='append', index=False, chunksize=100000)

engine.dispose()

print("Deu tudo certo, pode relaxar =)")
