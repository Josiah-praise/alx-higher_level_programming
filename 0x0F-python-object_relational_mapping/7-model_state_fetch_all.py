#!/usr/bin/python3
'''
lists all State objects
'''


def list_states():
    '''
    lists all State objects from the database hbtn_0e_6_usa
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
    result = session.query(State).all()
    for row in result:
        print(f'{row.id}: {row.name}')


if __name__ == '__main__':
    list_states()
