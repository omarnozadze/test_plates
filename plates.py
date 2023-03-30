def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if any(char.isdigit() for char in s[2:-2]):
        return False

    if s.isalnum() == False:
        return False 
       
    if len(s) < 2 or len(s) > 6 :
        return False

    for i in s:
        if s.find("0") == i:
            if s.find("0")<=i:
                return False
    return True   


if __name__ == "__main__":
    main()

    