# CNA 335 W21
# T.J. Dewey, tjdewey@student.rtc.edu
# code provided by justin ellis
# requires mysql-connector (no import)

from sqlalchemy import create_engine
import pandas



hostname="127.0.0.1"
uname="root"
pwd=""
dbname="zipcodes"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r"C:\Users\Dewey\Desktop\School\CNA Prog&Scripting\zip_code_database.csv")


connection=engine.connect()
tables.to_sql('zipcodes',con = engine, if_exists = 'replace')
connection.close()
print(tables)