# storing the three events
events = {
    "A": {"name": "Dance Event", "status": "Not Participated"},
    "B": {"name": "Cricket Event", "status": "Not Participated"},
    "C": {"name": "Poem Writing Event", "status": "Not Participated"}
}


# function to add participation
def add_participation():
    print("\n--- Add Participation ---")
    print("A - Dance Event")
    print("B - Cricket Event")
    print("C - Poem Writing Event")

    choice = input("Enter event (A/B/C): ").upper()

    # checking if the entered event is valid
    if choice in events:
        events[choice]["status"] = "Participated"
        print(events[choice]["name"], "participation recorded!")
    else:
        print("Invalid event choice.")


# function to search an event
def search_event():
    print("\n--- Search Event ---")
    choice = input("Enter event (A/B/C): ").upper()

    # checking the event
    if choice in events:
        print("\nEvent Found!")
        print("Code:", choice)
        print("Name:", events[choice]["name"])
        print("Status:", events[choice]["status"])
    else:
        print("Event not found.")


# function to show participation summary
def activity_summary():
    print("\n--- Activity Summary ---")

    participated = 0
    not_participated = 0

    # counting participated events
    for event in events.values():
        if event["status"] == "Participated":
            participated += 1
        else:
            not_participated += 1

    print("Total Events:", len(events))
    print("Events Participated:", participated)
    print("Events Not Participated:", not_participated)


# function to reset participation
def reset_participation():
    print("\n--- Reset Participation ---")
    choice = input("Enter event (A/B/C): ").upper()

    if choice in events:
        events[choice]["status"] = "Not Participated"
        print("Participation reset successfully!")
    else:
        print("Invalid event choice.")


# main menu of the program
def main():
    # keeping the menu running
    while True:
        print("\n==============================")
        print("     CAMPUS EVENT TRACKER")
        print("==============================")
        print("A - Dance Event")
        print("B - Cricket Event")
        print("C - Poem Writing Event")
        print("------------------------------")
        print("1. Add Participation")
        print("2. Search Event")
        print("3. Activity Summary")
        print("4. Reset Participation")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # selecting the option
        if choice == "1":
            add_participation()

        elif choice == "2":
            search_event()

        elif choice == "3":
            activity_summary()

        elif choice == "4":
            reset_participation()

        elif choice == "5":
            print("\nThank you for using Campus Event Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()