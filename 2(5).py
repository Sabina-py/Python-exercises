import math

# 1 talent = 20 pounds, 1 pound = 32 lots, 1 lot = 13.3 grams
talents = 3.0
pounds = 9.0
lots = 13.5

grams_total = (
    talents * 20 * 32 * 13.3
    + pounds * 32 * 13.3
    + lots * 13.3
)

kilograms = int(grams_total // 1000)
grams_remainder = grams_total % 1000

print("Input:")
print(f"  talents = {talents}, pounds = {pounds}, lots = {lots}")
print("The weight in modern units:")
print(f"  {kilograms} kilograms and {grams_remainder:.2f} grams.")
