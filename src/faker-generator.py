from faker import Faker
import random

from accounts.models import User

password = "pbkdf2_sha256$120000$pV6AiYYjHTsw$O6JzrM72XMpRTkrtXx5Q0crJTZjNoMRSY/UMtaDVuBA="

factory = Faker()

for i in range(1, 20):
    user = User(username=factory.name(), email=factory.email(), gender="male", password=password,
                age=random.randint(18, 44))
    user.save()
