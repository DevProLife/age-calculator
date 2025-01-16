from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    # Check if birthday has occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def main():
    print("Welcome to the Age Calculator!")
    while True:
        try:
            print("\nEnter your birthdate:")
            day = int(input("Day (1-31): "))
            month = int(input("Month (1-12): "))
            year = int(input("Year (e.g., 2000): "))
            
            # Validate and create a birthdate object
            birth_date = datetime(year, month, day)
            age = calculate_age(birth_date)
            
            print(f"\nYou are {age} years old.")
            
        except ValueError:
            print("\nInvalid date. Please try again.")
        
        # Ask if user wants to calculate another age
        choice = input("\nDo you want to calculate another age? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()