import math
import requests
from django.conf import settings

def num_prime(number):
    # check if number is a prime number

   if number < 2:
      return False
   for num in range(2, int(math.sqrt(number)) +1):
      if number % num == 0:
         return  False
   return True

def num_perfect(number):
   #check if number is perfect
   return sum(num for num in range(1, number // 2 + 1) if number % num == 0 ) == number

def num_properties(number):
   #return properties of number given
   properties = []

   #armstrong number

   str_num = str(number)
   num = len(str_num)
   total = sum(int(digit) ** num for digit in str_num)

   if total == number:
      properties.append("armstrong")

   # check odd or even number
   properties.append("even" if number % 2 == 0 else "odd")

   return properties

def sum_of_digits(number):
   #sum digits of number
   return sum(int(digit) for digit in str(number))


def get_funfact_for_number(number):
    """Retrieves funfacts of number using external api"""

    url = f"{settings.NUMBERAPI}/{number}/math"
    try:
        res = requests.get(url, timeout=5) # timeout to avoid long wait
        res.raise_for_status() #raise exception if status code 4xx/5xx
        return res.text
    except (requests.ConnectionError, requests.Timeout):
        return "No Internet connection, unable to fetch funfact"
    except requests.RequestException:
        return "Failed to retrieve funfact"