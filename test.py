from models import session, Document, User


def test_database():

    docs = session.query(Document).all()
    for doc in docs:
        print(f"Document ID: {doc.id}, Title: {doc.title}, Content: {doc.content}")

    users = session.query(User).all()
    for user in users:
        print(f"Serial No.-> {user.id}, User ID (user_id)-> {user.user_id}")


if __name__ == '__main__':
    test_database()
