#!/usr/bin/python3
'''
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
'''


def get_state():
    '''
    prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
    '''

    import sys
    from sqlalchemy.exc import NoResultFound
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    username, password, db_name, state_arg = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
        )

    session = sessionmaker(bind=engine)
    session = session()
    result = session.query(State.id).filter(State.name == state_arg)

    try:
        result.one()
        for row in result:
            print(row.id)
    except NoResultFound:
        print('Not found')


if __name__ == "__main__":
    get_state()
