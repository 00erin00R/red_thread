print("Welcome to my red thread project")
print("""This is a text based survival adventure game, you find yourself stranded far from civilisation after a sudden and mysterious disaster. With limited supplies and
no clear sence of what is beyond the tree line, every decision becomes a battle between instinct and uncertainty. You must explore the wilderness, scavenge for resources,
craft makeshift tools and uncover the truth behind your isolation. Danger is constant, help is scarce and your choices will determine wether you endure the unforgiving
wilds or become another forgotten story. """)

def main_menu():
    print("\n ############################################################################################################################################################")
    while True:
        print("What will u choose, 1-Play, 2-Overview, 3-Quit")

        try:
            choice = int(input("Enter your choice as a number: "))

            if choice == 1:
                print("Starting game...")
                break
            elif choice == 2:
                print("Lading overview...")
                break
            elif choice == 3:
                print("Quitting game...")
                quit()
            else:
                print("Please enter a valid number")
        
        except ValueError:
            print("Invalid input. Please enter a number")

main_menu()