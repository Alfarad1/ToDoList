# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import users as User

# conn_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"

# def get_all_users():
#     with Session(autoflush=False, bind=engine) as session:
#         people = session.query(User).all()
#         return people 

# def get_user(user_id: int) -> User | None:
#     with Session(autoflush=False, bind=engine) as session:
#         return session.get(User, user_id)

# def create_user(user: User):
#     with Session(autoflush=False, bind=engine) as session:
#         session.add(user)
#         session.commit()
#         return user
    
# def delete_user(user_id: int):
#     with Session(autoflush=False, bind=engine) as session:
#         session.delete(User, user_id)
#         session.commit()
#         return

# if __name__ == "__main__":

#     engine = create_engine(conn_string, echo=True)

#     # engine.connect()

#     Session = sessionmaker(autoflush=False, bind=engine)

#     with Session(autoflush=False, bind=engine) as session:
#         user = session.get(User, 10)
#         print(user)
# else:
#     engine = create_engine(conn_string)
#     Session = sessionmaker(autoflush=False, bind=engine)