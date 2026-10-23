# Task 08 - Algorithm Design and Pseudocode
# Algorithmic problem solving: Understand, Plan, Write, Test

def calculate_payout_pseudocode_demo(litres, fat, snf):
    if not (2.0 <= fat <= 7.0) or snf < 0 or litres < 0:
        return None, "Invalid Entry"
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30.00 + (fat_steps * 0.40) + (snf_steps * 0.30)
    return round(litres * rate, 2), "Success"

if __name__ == "__main__":
    payout, status = calculate_payout_pseudocode_demo(10, 4.2, 8.7)
    print("Demo Execution:", payout, status)
