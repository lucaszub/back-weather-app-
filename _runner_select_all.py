from sqlalchemy.orm import Session
from database_singleton import DatabaseSingleton
from sqlalchemy import MetaData, Table

# Create a new session
db = DatabaseSingleton().session

# Get the engine
engine = DatabaseSingleton().engine

# Perform the SELECT ALL query with a limit of 10
#results = db.query(Temperature).limit(10).all()
metadata = MetaData()

table = Table("temperature", metadata, autoload_with=engine)
# Display the results

# Print the column names
for column in table.columns:
    print(column.name)