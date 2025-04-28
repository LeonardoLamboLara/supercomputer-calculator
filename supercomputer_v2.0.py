import math
def main():
    print("Welcome to the Supercomputer Calculator v2.0!")

    # Asks the user how many supercomputers they have.
    supercomputer = get_computers()

    print(f"You have {supercomputer} supercomputers")

    total_power = 0


    for computer in range(supercomputer):
        power = int(input(f"Enter power for supercomputer {computer + 1}: "))
        total_power += power

    print(f"Your total compute power is {total_power} petaflops!")

    if total_power >= 1000:
        print("You have a supercluster! Jensen Huang respects you!")
    elif total_power >= 500:
        print("You have a supercomputer! Your nation is proud of you!")
    else:
        print("Good start. Keep upgrading young man!")

    nation_info = [
        {"name": "USA", "fav_GPU": "Nvidia", "superclusters": "1000"},
        {"name": "China", "fav_GPU": "Huawei", "superclusters": "750"},
        {"name": "USA", "fav_GPU": "Sberbank", "superclusters": "250"}
    ]
    for nation in nation_info:
        print(nation["name"], nation["fav_GPU"], nation["superclusters"], sep=", ")

# Supercomputer function
def get_computers():
    while True:
        n = math.ceil(float(input("How many supercomputers do you have? ")))
        if n >= 0:
            break
        else:
            print("Invalid number. Try again!")
    return n    

main()