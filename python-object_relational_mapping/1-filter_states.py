#!/usr/bin/python3
"""
Module to list all states with a name starting with 'N' from the
database hbtn_0e_0_usa
using SQLAlchemy.
"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def list_states_starting_with_n(username, password, dbname):
    """
    Connects to the database and prints all states with names starting
    with 'N' sorted by id.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        dbname (str): The name of the MySQL database.

    """
    # Create a connection string and engine
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(conn_str)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and order by id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each state that starts with 'N'
    for state in states:
        if state.name.startswith('N'):
            print(f"({state.id}, '{state.name}')")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states_starting_with_n(username, password, dbname)