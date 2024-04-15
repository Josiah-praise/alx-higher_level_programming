#!/usr/bin/python3
'''
changes the name of a
State object from the database hbtn_0e_6_usa
'''


def delete_states(letter):
    '''
    delets all states with names containing
    letter
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
    session.query(State) \
        .filter(State.name.like(f'%{letter}%')) \
        .delete(synchronize_session=False)
    session.commit()


if __name__ == "__main__":
    delete_states("a")
