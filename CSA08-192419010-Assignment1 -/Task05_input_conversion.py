# Task 05 - Input Handling and Conversion

def parse_input(val_str):
    try:
        val = float(val_str)
        return val
    except ValueError:
        print(f"Error: '{val_str}' is not a valid floating-point number.")
        return None

if __name__ == "__main__":
    print("Parsed 12.5:", parse_input("12.5"))
    print("Parsed abc :", parse_input("abc"))
