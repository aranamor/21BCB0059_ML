from models import session, Document, User
from faker import Faker
import random

fake = Faker()


def add_sample_data():  # Adding sample documents
    documents = []
    for i in range(500):
        doc = Document(
            title=f"Document {i + 1}: {fake.catch_phrase()}",
            content='\n'.join(fake.paragraphs(nb=random.randint(1, 5)))
        )
        documents.append(doc)

    users = []  # Adding sample users
    for i in range(30):
        user = User(user_id=fake.name())
        users.append(user)

    session.add_all(documents)
    session.add_all(users)

    session.commit()  # Commiting the changes

    return len(documents), len(users)


if __name__ == '__main__':
    num_docs, num_users = add_sample_data()
    print(f"{num_docs} documents and {num_users} users are added to the database.")
