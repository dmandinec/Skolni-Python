import webbrowser

def open_website(choice):
    if choice == '1':
        webbrowser.open("https://www.youtube.com/watch?v=ADyLx_6m3TA&pp=ygUycmljayBhc3RsZXkgbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAgbmVjbyBhcmMgY292ZXI%3D")
        print("Otvárám Pornhub...")
    elif choice == '2':
        webbrowser.open('https://youtu.be/it7mUV-PwIY?si=8EL3JGAAWXWYf-KS&t=14')
        print("Otvárám Drsnej Svět...")
    else:
        print("Neplatná odpoveď! Zadajte 1 alebo 2.")
def main():
    while True:
        print("\nCursed Webový Prehliadač")
        print("1: Otvoriť Pornhub")
        print("2: Otvoriť Drsnej Svět")
        print("0: Žabit se")
        choice = input("Zadajte číslo: ")

        if choice == '0':
            print("Skapem...")
            break
        else:
            open_website(choice)

if __name__ == "__main__":
    main()
