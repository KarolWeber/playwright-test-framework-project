import random

from faker import Faker

faker = Faker()


def create_user():
    birth_date = faker.date_of_birth(minimum_age=5, maximum_age=126)
    gender = random.choice(['Mr', 'Mrs'])
    first_name = faker.first_name_male() if gender == 'Mr' else faker.first_name_female()
    last_name = faker.last_name()
    return {
        "name": first_name,
        "email": f'{first_name.lower()}_{last_name.lower()}@test.com',
        "password": faker.password(length=6, special_chars=False),
        "gender": gender,
        "birth_day": str(birth_date.day),
        "birth_month": faker.month_name(),
        "birth_year": str(birth_date.year),
        "newsletter": True,
        "marketing": True,
        "first_name": first_name,
        "last_name": last_name,
        "company": faker.company(),
        "primary_address": faker.street_address(),
        "secondary_address": faker.street_address(),
        "country": random.choice(
            ['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']),
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.postcode(),
        "mobile_number": faker.numerify("#########"),
    }
