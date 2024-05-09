#Python code to demonstrate the usage of functions

print("Welcome to the City Descriptor!!!!")

def main():
    inp1 = input("Please enter the city name: ")
    match inp1:
        case "Guwahati":
            print ("Also known as Pragjyotishpur")
        case "Kolkata":
            print("Also known as City of Joy")
        case "Siliguri":
            print("Also known as Gateway of Northeast")            
        case _:
            print("Unknown city")


if __name__ == "__main__":
    main()

