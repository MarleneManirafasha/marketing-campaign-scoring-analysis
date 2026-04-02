from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://username:password@localhost:5432/marketing_db"
)

df.to_sql("campaign_data", engine, if_exists="replace", index=False)