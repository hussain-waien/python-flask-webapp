from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db_connecton_string = os.getenv('DATABASE_URL')

engine = create_engine(db_connecton_string,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })
def display_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
        return jobs