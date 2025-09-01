import random

import random

random.seed(42)  # so the example output is repeatable

code_3 = [random.randint(0, 9) for _ in range(3)]   # 0–9
code_4 = [random.randint(1, 6) for _ in range(4)]   # 1–6

print("3-digit lock code:", "".join(str(d) for d in code_3))
print("4-digit lock code:", "".join(str(d) for d in code_4))
