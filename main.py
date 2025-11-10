import Notes_Manager.db_handler as db
from Notes_Manager.logger_setup import setup_logger


logger = setup_logger()


while True:
    print("=== Notes Manager ===\n1. Add a note\n2. View notes\n3. Delete a note\n4. Exit")
    user_choise = int(input("Enter your choice (1-4): "))

    try:
        if user_choise <= 0 or user_choise > 4:
            logger.error("Invalid choice! Please enter a number between 1 and 4.")
            continue

    except ValueError:
        logger.error("Invalid input for amount. Please enter a numeric value.")

    if user_choise == 1:
        verification = True
        notes = db.get_all_notes()
        user_title = input("Enter title: ")

        for i in range(len(notes)):
            if notes[i][1] == user_title:
                verification = False

        if verification:
            user_text = input("Enter text: ")
            db.add_note(user_title=user_title, user_text=user_text)
            logger.info("Note successfully added!")
        else:
            logger.error("This note title already exists!")

    elif user_choise == 2:
        notes = db.get_all_notes()
        print(notes)

    elif user_choise == 3:
        verification = True
        notes = db.get_all_notes()
        delete_choise = input("Enter a title to delete the note( * - delete all notes): ")

        if delete_choise == '*':
            db.delete_all_notes()
            logger.info("Notes successfully deleted!")
        else:
            for i in range(len(notes)):
                if notes[i][1] == delete_choise:
                    db.delete_note(delete_choise)
                    logger.info("Note successfully deleted!")
                    verification = False

            if verification:
                logger.error("Enter the title that appears in the notes!")

    elif user_choise == 4:
        break

