n = input("Please enter your number:")
def normalize_phone(n):
    if "".join(s for s in n if s.isdigit()) == n:
        
        print("No changes")
    else:
        print("The number has been changed")

    return "".join(s for s in n if s.isdigit())

print(normalize_phone(n))

print("Thanks for using the service")
