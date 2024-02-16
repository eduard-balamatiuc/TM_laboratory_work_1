define student_1 = Character("Student", color="#FFFFFF")
define student_2 = Character("Student", color="#FFFFFF")
define professor = Character("Character", color="#FFFFFF")
define dean = Character("Dean", color="#FFFFFF")


# The game starts here.

label start:

    scene bg_cab_118
    "It was a tough semester and really loaded with a lot of tasks and laboratory works. You have to present your final project and today is the deadline."
    "You received an email from the professor X a day before, where he mentioned that he will be at the university at 13:00 in 3-118 on the day of the deadline."
    scene bg_cab_118_inside
    "As you approach the cabinet you see it that is open, the professor is not there, but some of his things are still on the table, including his computer."

    show student_1 default
    label choices:
        menu:
                "What will you do now?"
                "Send a message to your collegues":
                    jump choices_message_collegues
                "Send an email to your professor":
                    jump choices_message_professor
                "Wait for the professor":
                    jump choices_wait

    label choices_message_collegues:
    show student_1 default
    student_1 "Hey guys. Have anyone seen professor X today? I have to present the lab today"
    show student_2 default
    student_2 "Yeah, I presented the lab today in 118,  he said he will be there"

    jump choises_common

    label choices_message_professor:
    student_1 "Hello, Mr. X.  I am in 118 waiting to present the lab. I wanted to ask if I still have the possibility to present the lab today?"

    jump choises_common

    label choices_wait:
    student_1 "Wait for the professor"

    jump choises_common

    label choises_common:
    "You waited for an hour already and no trace of the professor"
    "You got suspicious and bored and decided to go through his stuff"
    show student_1 default
    label choices_1:
        menu:
                "Where will you look for the next hint?"
                "Check his laptop":
                    jump choices_laptop
                "Look through the book on the table":
                    jump choices_book
                "Look through his research papers":
                    jump choices_papers
    label choices_laptop:
            menu:
                "What will you check now?"
                "Check emails":
                    jump choices_check_emails
                "Check his calendar":
                    jump choices_check_calendar

    label choices_check_emails:
    student_1 "You see your unread email, but also a lot of emails between the professor and a mysterious contact "
    student_1 "Look through his notes"
    student_1 "Read all the emails between the professor and mysterious contact"
    student_1 "Among the encrypted emails, you find coded references to a clandestine group known only as {b}The Illuminated Circle.{/b} The emails suggest that the professor was a member of this secret society and was involved in their esoteric pursuits. "

    label choices_2:
        menu:
            "Have you noticed anything or not ?!"
            "See a patern":
                jump choices_see_patern
            "Read through all the emails":
                jump choices_look_emails

    label choices_see_patern:
    student_1 "Each mail contain cryptic codenames referring to members of the secret society. Decipher the true identities of these individuals and uncover their roles within the organization."
    student_1 "You see that each mail has a characteristic name of the subject. All of them contain the same information in the following order: degrees, zodiac sign, coordonates."

    label choices_3:
        menu:
            "What's going on?"
            "Take one of the subjects name and google it":
                jump choices_google_it
            "Try to find a relation between all of them"
                jump choices_relation

    label choices_look_emails:
    student_1 "hi"

    label choices_check_calendar:
    student_1 "hi"


    jump choices_laptop_look

    label choices_book:
  
    student_1 "hi"

    label choices_papers:

    student_1 "hi"









    # These display lines of dialogue.

    student_1 "Did you change the name and save directory of the game in options.rpy?"
    

    $ answer = renpy.input("Did you change the values at the top of options.rpy?").strip().lower()

    if answer == "yes":
        "Good job"
    else:
        student_1 "If not, you should do so right away! Saves will not work properly until you do."

    $ renpy.notify("This is a notification")

    menu:
        "This is a sample choice menu"
        "Choice 1":
            pass
        "Choice 2":
            pass
    # This ends the game.
    student_1 "dsfhjaihdjhfidashfiasjdfh"
    return