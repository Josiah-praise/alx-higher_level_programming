#!/usr/bin/python3
'''
changes the name of a
State object from the database hbtn_0e_6_usa
'''


def update_state(state_name):
    '''
    change the name of the state where id = 2
    to new mexico
    '''

    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username, password, db_name = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.get(State, 2)
    if result:
        result.name = state_name
        session.commit()


if __name__ == "__main__":
    update_state("New Mexico")
