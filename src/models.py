from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text
import sqlalchemy as db


Base = declarative_base()
engine = db.create_engine('postgresql://admin:secret@host.docker.internal/parse_db')


class Ads(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    title = Column(Text)
    date = Column(Date)
    location = Column(String)
    bedrooms = Column(String)
    description = Column(Text)
    price = Column(String)
    currency = Column(String)

    def __repr__(self):
        return "<Ads(title='{}', date='{}', location={}, bedrooms={})>" \
            .format(self.title, self.date, self.location, self.bedrooms)


table_objects = [Ads.__table__]
Base.metadata.create_all(engine, tables=table_objects)
conn = engine.connect()
conn.execute("SET DateStyle='SQL, DMY'")
