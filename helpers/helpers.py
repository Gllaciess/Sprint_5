import random
import string


def generate_email():


   first_name = "ivan"
   last_name = "ivanov"
   number = "43"
   random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
  
   return f"{first_name}_{last_name}_{number}_{random_digits}@yandex.ru"


def generate_password(min_length=6):


   letters = string.ascii_letters
   digits = string.digits
   all_chars = letters + digits
  
   return ''.join(random.choice(all_chars) for _ in range(min_length))


def generate_name():


   names = ["Иван", "Петр", "Никита", "Анна", "Мария", "Елена", "Дмитрий", "Оксана"]
   random_digits = ''.join(random.choices(string.digits, k=2))
  
   return random.choice(names) + random_digits


