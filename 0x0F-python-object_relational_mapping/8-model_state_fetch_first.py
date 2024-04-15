#!/usr/bin/python3
'''
fetches the first state object
and prints it
'''


def fetch_first_state():
    '''
    prints the first State object from the database hbtn_0e_6_usa
    '''

    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username, password, db_name = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
        )

    session = sessionmaker(bind=engine)
    session = session()
    result = session.query(State).order_by(State.id).first()

    if result:
        print(f'{result.id}: {result.name}')
    else:
        print('Nothing')


if __name__ == "__main__":
    fetch_first_state()
