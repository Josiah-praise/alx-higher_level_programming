#!/usr/bin/python3
'''
lists all objects that contain letter a from
hbtn_0e_6_usa database
'''


def fetch_state():
    '''
    print state that contain letter `a` from
    the database hbtn_0e_6_usa
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
    result = session.query(State).filter(State.name.like('%a%'))

    for row in result:
        print(f'{row.id}: {row.name}')


if __name__ == "__main__":
    fetch_state()
