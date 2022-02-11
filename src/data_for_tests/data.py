from faker import Faker



class Data:
    faker = Faker()

    title = faker.word()
    body = faker.word()
    userId = faker.numerify('####')