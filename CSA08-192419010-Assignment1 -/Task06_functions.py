# Task 06 - Modular Functions Implementation

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(30.00 + (fat_steps * 0.40) + (snf_steps * 0.30), 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

if __name__ == "__main__":
    print("Payout:", payout(10, 3.5, 8.5))
