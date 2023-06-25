

import string
from random import *

a = int(input("From: "))
b = int(input("To: "))

from_item = string.ascii_letters + string.digits + string.ascii_letters

p_key = "".join(choice(from_item) for x in range(randint(a,b)))
print(f"Your password is: {p_key}")


