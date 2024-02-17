define student_1 = Character("Student", color="#FFFFFF")
define collegue = Character("Collegue", color="#FFFFFF")
define professor = Character("Professor", color="#FFFFFF")
define dean = Character("Dean", color="#FFFFFF")

# in game variables
default kindness = 10
default discoveries = 0
default sneakiness = 0

image professor:
    "professor.png"
image student:
    "student_1.png"
    zoom 1.5

image collegue:
    "collegue.png"
    zoom 2.2

image desktop:
    "desktop.png"
    zoom 2.1

image dean:
    "dean.png"
    zoom 0.6

style outline is text:
    color "#657CD5"
    size 40

# The game starts here.
screen stats():
    text "Kindness: [kindness]" align (0.05, 0.05) style "outline"
    text "Discoveries: [discoveries]" align (0.05, 0.1) style "outline"
    text "Sneakiness: [sneakiness]" align (0.05, 0.15) style "outline"

label start:

    play music "audio/backgroundmusic.mp3" volume 0.5
    
    scene bg_cab_118
    show screen stats()
    "It was a tough semester and really loaded with a lot of tasks and laboratory works. You have to present your final project and today is the deadline."
    show student with dissolve
    "You received an email from the professor X a day before, where he mentioned that he will be at the university at 13:00 in 3-118 on the day of the deadline."

    hide student with moveoutright

    scene bg_classroom
    show student at left with moveinleft
    "As you approach the cabinet you see that it is open, the professor is not there, but some of his things are still on the table, including his computer."
    $ discoveries += 1 # Increase discoveries as the player makes a new observation.
    show student
    
    label choices:
        menu:
            "What will you do now?"
            "Send a message to your collegues":
                $ kindness += 1 # Kindness increases as the student reaches out for help.
                jump choices_message_collegues
            "Send an email to your professor":
                $ kindness += 2 # Kindness increases more due to taking the formal and respectful route.
                jump choices_message_professor
            "Wait for the professor":
                $ sneakiness -= 1 # Sneakiness decreases as the student chooses to wait patiently.
                jump choices_wait

    label choices_message_collegues:
        show student
        show collegue:
            xalign 0.9 yalign 0.85
        with moveinright
        student_1 "Hey guys. Have anyone seen professor X today? I have to present the lab today"
        collegue "Yeah, I presented the lab today in 118,  he said he will be there"
        hide collegue with moveoutright
        $ discoveries += 1 # Increase discoveries as the student gains new information from the colleague.

        jump choices_common

    label choices_message_professor:
        student_1 "Hello, Mr. X.  I am in 118 waiting to present the lab. I wanted to ask if I still have the possibility to present the lab today?"
        $ discoveries += 1 # Increase discoveries as the student takes initiative to contact the professor directly.

        jump choices_common

    label choices_wait:
        student_1 "Wait for the professor"
        # This path does not directly lead to new discoveries or interactions that would adjust kindness or sneakiness.

        jump choices_common

    label choices_common:
        "You waited for an hour already and no trace of the professor"
        "You got suspicious and bored and decided to go through his stuff"
        $ sneakiness += 2 # Sneakiness increases as the student decides to snoop through the professor's belongings.
        $ discoveries += 1 # Increase discoveries as the situation progresses.

        scene bg_monitor_screen

        label choices_1:
            menu:
                "Where will you look for the next hint?"
                "Check his laptop":
                    $ sneakiness += 1 # Increasing sneakiness for choosing to snoop through personal items.
                    jump choices_laptop
                "Look through the book on the table":
                    $ discoveries += 1 # Increase discoveries for choosing to explore academic material.
                    jump choices_book
                "Look through his research papers":
                    $ discoveries += 1 # Increase discoveries for engaging with professional work.
                    jump choices_papers

    label choices_laptop:
        menu:
            "What will you check now?"
            "Check emails":
                $ sneakiness += 2 # Further increase in sneakiness for choosing to invade privacy.
                $ discoveries += 2 # Significant discovery made by choosing to check emails.
                jump choices_check_emails
            "Check his calendar":
                $ sneakiness += 1 # Less intrusive than emails, but still sneaky.
                $ discoveries += 1 # Gain insight into the professor's schedule.
                jump choices_check_calendar

    label choices_check_emails:
        show desktop:
            xalign 0.48 yalign 0.06
        "You see your unread email, but also a lot of emails between the professor and a mysterious contact."
        "Look through his notes."
        "Read all the emails between the professor and mysterious contact."
        "Among the encrypted emails, you find coded references to a clandestine group known only as {b}The Illuminated Circle.{/b} The emails suggest that the professor was a member of this secret society and was involved in their esoteric pursuits."
        $ discoveries += 3 # Major discovery made.
        $ sneakiness += 1 # Additional sneakiness for reading through private emails.

        label choices_2:
            menu:
                "Have you noticed anything or not ?!"
                "See a pattern":
                    $ kindness -= 1 # Slight decrease in kindness for exploiting the information.
                    $ discoveries += 2 # Additional discoveries made by noticing a pattern.
                    jump choices_see_pattern
                "Read through all the emails":
                    $ sneakiness += 2 # Further increase in sneakiness for thorough invasion of privacy.
                    $ discoveries += 2 # Additional discoveries from reading all emails.
                    jump choices_look_emails

    label choices_see_pattern:
        "Each mail contains cryptic codenames referring to members of the secret society. Decipher the true identities of these individuals and uncover their roles within the organization."
        "You see that each mail has a characteristic name of the subject. All of them contain the same information in the following order: degrees, zodiac sign, coordinates."
        $ discoveries += 2 # Further discoveries made by decoding the pattern.

        label choices_3:
            menu:
                "What's going on?"
                "Take one of the subjects' name and google it":
                    $ kindness += 1 # Kindness increases as the action is driven by curiosity rather than malice.
                    $ discoveries += 2 # Discoveries made by researching the subject.
                    jump choices_google_it
                "Try to find a relation between all of them":
                    $ discoveries += 2 # Intellectual curiosity leads to more discoveries.
                    jump choices_relation

    label choices_google_it:
        "It coincides with the position of the moon on the day before."
        $ discoveries += 1 # Discovery related to astronomical events.

        label choices_4:
            menu:
                "Hmm, what's this? ..."
                "Try to find the position of the moon for today and write an email to that mysterious person":
                    $ sneakiness += 3 # High sneakiness for pretending to be part of the secret society.
                    $ discoveries += 3 # Major discovery by connecting current events with the society.
                    jump choices_find_position
                "Google the name of the association":
                    $ kindness += 1 # Driven by curiosity, which is a more benign motive.
                    $ discoveries += 2 # Discoveries made by learning more about the association.
                    jump choices_google_name

    label choices_find_position:

