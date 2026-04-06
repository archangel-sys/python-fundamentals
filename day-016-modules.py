import math
print(math.sqrt(25))
print(math.pi)
print(math.pow(2, 10))

from math import sqrt, pi
print(sqrt(25))
print(pi)

import random
print(random.randint(1, 100))
print(random.choice(["Korea", "Canada", "China", "Spain", "Japan"]))

from datetime import datetime
now=datetime.now()
print(f"Today {now.year}-{now.month}-{now.day}")
print(f"Time: {now.hour}:{now.minute}")