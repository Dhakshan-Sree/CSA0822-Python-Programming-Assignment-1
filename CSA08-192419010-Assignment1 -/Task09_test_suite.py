# Task 09 - Automated Test Suite
import milkrate

def test_calculator():
    assert milkrate.rate_per_litre(3.5, 8.5) == 30.00
    assert milkrate.payout(10, 3.5, 8.5) == 300.00
    assert milkrate.rate_per_litre(4.2, 8.7) == 33.40
    print("All assert tests passed successfully!")

if __name__ == "__main__":
    test_calculator()
