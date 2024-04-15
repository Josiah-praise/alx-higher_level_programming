#!/usr/bin/python3
'''
prints all City objects from the database hbtn_0e_14_usa
'''


if __name__ == "__main__":

    import sys
    from model_city import City
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username, password, db_name = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
        )

    session = sessionmaker(engine)
    session = session()
    result = session.query(City).all()

    for row in result:
        print(f'{row.state.name}: ({row.id}) {row.name}')
