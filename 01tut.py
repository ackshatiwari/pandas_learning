import pandas as pd

apartments = []


def apartmentHelper():
    isApartmentsPendingToAdd = True

    role = input("Are you a user or an apartment inputer(U/A)?")

    if role == "A":
        while isApartmentsPendingToAdd:
            apartment = input("Enter the apartment number(press q to quit): ")
            if apartment == "q":
                isApartmentsPendingToAdd = False
                series = pd.Series(apartments)

                print("Apartments below")
                print(series)  # Prints all apartments
                break
            else:
                isApartmentsPendingToAdd = True
                apartments.append(int(apartment))

    elif role == "U":
        userApartment = input("What apartment do you want to have?")
        apartmentFound = False
        for item in apartments:
            if int(userApartment) == item:
                print("You have entered the apartment number: ", item, " which is not taken")
                apartmentFound = True
                break

        if not apartmentFound:
            print("Apartment not found")



    print("----------------------------------------")
    print("----------------------------------------")


while input("Do you want to continue? (y/n)").lower() == "y":
    apartmentHelper()




