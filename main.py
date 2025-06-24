from astronauts import fetch_astronauts
from iss_tracker import track_iss
from news_or_stock import fetch_news_or_stock

def main_menu():
    while True:
        print("\n🛰️ LIVE DATA REPORTER 🛰️")
        print("=="*15)
        print("1. View astronauts currently in space.")
        print("2. Track the ISS in real-time.")
        print("3. View news headlines or stock data.")
        print("4. Exit application.")
        print("=="*15)
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            fetch_astronauts()
        elif choice == "2":
            track_iss()
        elif choice == "3":
            fetch_news_or_stock()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()

