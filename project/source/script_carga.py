import pandas as pd
import sqlalchemy as sqlal
from sqlalchemy import create_engine


def trata_data(dataframe, columns):
    """dataframe: pandas dataframe,

       columns: lista com os nomes das colunas para converter para datetime"""
    df_treated = dataframe.copy()

    for column_name in columns:
        for column in dataframe.columns:
            if column.find(column_name) != -1:
                df_treated[column] = pd.to_datetime(df_treated[column])

    return df_treated


def trata_precos(dataframe):
    df_treated = dataframe.copy()

    for column in df_treated.columns:
        if column.find('price') != -1:
            df_treated[column] = (df_treated[column].str.replace("$", "")).str.replace(",", "").astype("float")

    return df_treated


def trata_strings(dataframe):
    df_treated = dataframe.copy()

    for column in df_treated.columns:
        if df_treated[column].dtype == 'object':
            df_treated[column] = (df_treated[column].str.replace("\r<br/>", "")).astype("string")

    return df_treated


# Carga dos dados
df_calendar = pd.read_csv("../data/calendar.csv")
df_listings = pd.read_csv("../data/listings.csv")
df_reviews = pd.read_csv("../data/reviews.csv")

# Conversão de alguns tipos
df_listings = trata_data(df_listings, ['last_scraped', 'host_since', 'calendar_last_scraped',
                                       'calendar_last_scraped', 'first_review', 'last_review'])
df_listings = trata_precos(df_listings)

df_reviews = trata_data(df_reviews,['date'])
df_reviews = trata_precos(df_reviews)
df_reviews = trata_strings(df_reviews)

df_calendar = trata_data(df_calendar, ['date'])
df_calendar = trata_precos(df_calendar)
df_calendar = df_calendar[0:50000]


# Criação do DB


db_name = "AE_ADA"

conn_string = f"postgresql://postgres:552277@localhost:5432/{db_name}"
engine = create_engine(conn_string)
metadata = sqlal.MetaData()



# Criação das tabelas e carga dos dados no db
# Criação da tabela listings...
listings_table = sqlal.Table('bronze_listings', metadata,
                             sqlal.Column('id', sqlal.types.BIGINT(), primary_key=True,
                                          autoincrement=False),
                             sqlal.Column('listing_url', sqlal.types.VARCHAR(length=200)),
                             sqlal.Column('scrape_id', sqlal.types.BIGINT()),
                             sqlal.Column('last_scraped', sqlal.DateTime()),
                             sqlal.Column('source', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('name', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('description', sqlal.types.TEXT()),
                             sqlal.Column('neighborhood_overview', sqlal.types.TEXT()),
                             sqlal.Column('picture_url', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_id', sqlal.types.BigInteger()),
                             sqlal.Column('host_url', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_name', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_since', sqlal.DateTime()),
                             sqlal.Column('host_location', sqlal.types.VARCHAR(length=200)),
                             sqlal.Column('host_about', sqlal.types.TEXT()),
                             sqlal.Column('host_response_time', sqlal.types.VARCHAR(length=50)),
                             sqlal.Column('host_response_rate', sqlal.types.VARCHAR(length=10)),
                             sqlal.Column('host_acceptance_rate', sqlal.types.VARCHAR(length=10)),
                             sqlal.Column('host_is_superhost', sqlal.types.VARCHAR(length=10)),
                             sqlal.Column('host_thumbnail_url', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_picture_url', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_neighbourhood', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_listings_count', sqlal.types.INTEGER()),
                             sqlal.Column('host_total_listings_count', sqlal.types.INTEGER()),
                             sqlal.Column('host_verifications', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_has_profile_pic', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('host_identity_verified', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('neighbourhood', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('neighbourhood_cleansed', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('neighbourhood_group_cleansed', sqlal.types.VARCHAR(length=500)),
                             sqlal.Column('latitude', sqlal.types.Float()),
                             sqlal.Column('longitude', sqlal.types.Float()),
                             sqlal.Column('property_type', sqlal.types.VARCHAR(length=100)),
                             sqlal.Column('room_type', sqlal.types.VARCHAR(length=100)),
                             sqlal.Column('accommodates', sqlal.types.INTEGER()),
                             sqlal.Column('bathrooms', sqlal.types.Float()),
                             sqlal.Column('bathrooms_text', sqlal.types.VARCHAR(length=50)),
                             sqlal.Column('bedrooms', sqlal.types.INTEGER()),
                             sqlal.Column('beds', sqlal.types.INTEGER()),
                             sqlal.Column('amenities', sqlal.types.TEXT()),
                             sqlal.Column('price', sqlal.types.Float()),
                             sqlal.Column('minimum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('maximum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('minimum_minimum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('maximum_minimum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('minimum_maximum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('maximum_maximum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('minimum_nights_avg_ntm', sqlal.types.Float()),
                             sqlal.Column('maximum_nights_avg_ntm', sqlal.types.Float()),
                             sqlal.Column('calendar_updated', sqlal.DateTime()),
                             sqlal.Column('has_availability', sqlal.types.VARCHAR(length=100)),
                             sqlal.Column('availability_30', sqlal.types.INTEGER()),
                             sqlal.Column('availability_60', sqlal.types.INTEGER()),
                             sqlal.Column('availability_90', sqlal.types.INTEGER()),
                             sqlal.Column('availability_365', sqlal.types.INTEGER()),
                             sqlal.Column('calendar_last_scraped', sqlal.DateTime()),
                             sqlal.Column('number_of_reviews', sqlal.types.INTEGER()),
                             sqlal.Column('number_of_reviews_ltm', sqlal.types.INTEGER()),
                             sqlal.Column('number_of_reviews_l30d', sqlal.types.INTEGER()),
                             sqlal.Column('first_review', sqlal.DateTime()),
                             sqlal.Column('last_review', sqlal.DateTime()),
                             sqlal.Column('review_scores_rating', sqlal.types.REAL()),
                             sqlal.Column('review_scores_accuracy', sqlal.types.REAL()),
                             sqlal.Column('review_scores_cleanliness', sqlal.types.REAL()),
                             sqlal.Column('review_scores_checkin', sqlal.types.REAL()),
                             sqlal.Column('review_scores_communication', sqlal.types.REAL()),
                             sqlal.Column('review_scores_location', sqlal.types.REAL()),
                             sqlal.Column('review_scores_value', sqlal.types.REAL()),
                             sqlal.Column('license', sqlal.types.VARCHAR(length=1000)),
                             sqlal.Column('instant_bookable', sqlal.types.VARCHAR(length=1000)),
                             sqlal.Column('calculated_host_listings_count', sqlal.types.INTEGER()),
                             sqlal.Column('calculated_host_listings_count_entire_homes', sqlal.types.INTEGER()),
                             sqlal.Column('calculated_host_listings_count_private_rooms', sqlal.types.INTEGER()),
                             sqlal.Column('calculated_host_listings_count_shared_rooms', sqlal.types.INTEGER()),
                             sqlal.Column('reviews_per_month', sqlal.types.REAL()),
                             schema='bronze'

                             )

calendar_table = sqlal.Table('bronze_calendar', metadata,
                             sqlal.Column('listing_id', sqlal.types.BigInteger(),
                                          sqlal.ForeignKey('bronze.bronze_listings.id')),
                             sqlal.Column('date', sqlal.DateTime()),
                             sqlal.Column('available', sqlal.types.VARCHAR(length=5)),
                             sqlal.Column('price', sqlal.types.REAL()),
                             sqlal.Column('adjusted_price', sqlal.types.REAL()),
                             sqlal.Column('minimum_nights', sqlal.types.INTEGER()),
                             sqlal.Column('maximum_nights', sqlal.types.INTEGER()),
                             schema='bronze')

reviews_table = sqlal.Table('bronze_reviews', metadata,
                            sqlal.Column('id', sqlal.types.BigInteger(), primary_key=True,
                                         autoincrement=False),
                            sqlal.Column('listing_id', sqlal.types.BigInteger(),
                                         sqlal.ForeignKey('bronze.bronze_listings.id')),
                            sqlal.Column('date', sqlal.DateTime()),
                            sqlal.Column('reviewer_id', sqlal.types.BigInteger()),
                            sqlal.Column('reviewer_name', sqlal.types.VARCHAR(length=100)),
                            sqlal.Column('comments', sqlal.types.VARCHAR(length=10000)),
                            schema='bronze')

# listings_table.create(engine)
# calendar_table.create(engine)
# reviews_table.create(engine)
metadata.create_all(engine)
df_listings.to_sql('bronze_listings', engine, schema='bronze', if_exists='append', index=False, chunksize=100000)
df_calendar.to_sql('bronze_calendar', engine, schema='bronze', if_exists='append', index=False, chunksize=100000)
df_reviews.to_sql('bronze_reviews', engine, schema='bronze', if_exists='append', index=False, chunksize=100000)

engine.dispose()

print("Deu tudo certo, pode relçaxar =)")
