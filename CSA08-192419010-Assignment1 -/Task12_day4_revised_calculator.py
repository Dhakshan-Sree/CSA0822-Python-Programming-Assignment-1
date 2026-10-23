"""Day-4 Design Challenge - Revised Milk Payment Calculator."""

def revised_rate_per_litre(fat, snf, season="normal"):
    base_rate = 32.00 if season == "summer" else 30.00
    fat_step = 0.45 if season == "summer" else 0.40
    snf_step = 0.30
    
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    
    rate = base_rate + (fat_steps * fat_step) + (snf_steps * snf_step)
    return round(rate, 2)

def revised_payout(litres, fat, snf, ten_day_total_litres=0, season="normal"):
    rate = revised_rate_per_litre(fat, snf, season)
    if ten_day_total_litres > 500:
        rate += 0.50  # Volume bonus per litre
    amount = litres * rate
    return round(amount, 2)

if __name__ == "__main__":
    print("=== Revised Milk Payment Calculator Testing ===")
    p1 = revised_payout(50, 4.25, 8.72, ten_day_total_litres=600, season="summer")
    p2 = revised_payout(50, 4.25, 8.72, ten_day_total_litres=400, season="normal")
    print(f"Summer Season + High Volume Bonus (>500L) Payout: Rs.{p1}")
    print(f"Normal Season Standard Payout                   : Rs.{p2}")
