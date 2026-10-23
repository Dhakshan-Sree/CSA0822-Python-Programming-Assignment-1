# Task 01 - Problem Analysis and Requirements Identification
# Farmer ID: String, Milk Quantity: Float, Fat/SNF: Float, Shift: String

def display_requirements():
    inputs = ["farmer_id", "litres", "fat_pct", "snf_pct", "shift"]
    outputs = ["rate_per_litre", "payout_amount", "ten_day_total"]
    constants = {"BASE_RATE": 30.00, "FAT_STEP_VALUE": 0.40, "SNF_STEP_VALUE": 0.30}
    print("Inputs:", inputs)
    print("Outputs:", outputs)
    print("Constants:", constants)

if __name__ == "__main__":
    display_requirements()
