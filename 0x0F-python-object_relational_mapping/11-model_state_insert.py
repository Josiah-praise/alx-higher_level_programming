#!/usr/bin/python3
'''
creates a state with the name `Louisiana`
'''


def create_state(state_name):
    '''
    creates a new state in the database
    hbtn_0e_6_usa
    '''

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    username, password, db_name = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    session = sessionmaker(bind=engine)
    session = session()
    new_state_record = State(name=state_name)
    session.add(new_state_record)
    session.commit()
    print(new_state_record.id)


if __name__ == "__main__":
    create_state('Louisiana')
