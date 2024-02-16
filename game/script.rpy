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
            "Try to find a relation between all of them":
                jump choices_relation

    label choices_google_it:
    student_1 "It coincides with the position of the moon on the day before"

    label choices_4:
        menu:
            "Hmm, what's this? ..."
            "Try to find the position of the moon for today and write an email to the that mysterious person":
                jump choices_find_position
            "Google the name of the association":
                jump choices_google_name

    label choices_find_position:
    student_1 "You found the code for the current day, but you still think it is a really bad idea to engage in such strange things"
    jump choices_4_common

    label choices_google_name:
    student_1 "You discover just few sites which explain that this is a really old society that is involved in some rituals"
    jump choices_4_common

    label choices_4_common:
    student_1 "Go to dean's office and announce him that you think something strange is happening with the professor and he is missing for too long"
    "It's been 2 days and you are reading in the local news that this professor was found dead in weird circumstances. You are haunted by this situation for your whole life "

    label choices_relation:
        label choices_5:
            menu:
                "What should I do?"
                "You thought about the planets and remembered about the planetarium near university.":
                    jump choices_5_common
                "You have a friend that is pasisonate of planets and astrological things. Write them a message":
                    jump choices_ask_friend

        label choices_ask_friend:
        student_1 "sent a photo"
        student_1 "Do you have an idea what are those?"
        student_2 "eah, they seem like some planet's position"
        jump choices_5_common

        label choices_5_common:
        student_1 "Visit the planetarium."
        student_1 "It is already late and you think the planetarium might be closed."
        label choices_6:
            menu:
                "What should I do?"
                "Check the door and see if is closed":
                    jump choices_check_door
                "Check the panels besides the planetarium":
                    jump choices_6_common
        label choices_check_door:
        student_1 "You checked the door and the planetarium is closed"
        jump choices_6_common

        label choices_6_common:
        student_1 "You see some text written over the panel"

        label choices_7:
            menu:
                "What will be my next step?"
                "Find your phone's flashlight and check the text":
                    jump choices_check_phone
                "Go back to university":
                    jump choices_go_to_university
        label choices_check_phone:
        student_1 "You see {b}REDRUM{/b} written all over the panel"
        jump choices_4_common

        label choices_go_to_university:
        student_1 "It is already late and the professor is nowhere to be seen"
        jump choices_4_common

    label choices_look_emails:
    student_1 "See a suspicious link and press Access the link"
    student_1 "You've been redirected to  Rick Astley - Never Gonna Give You Up and a note from the professor that you can find him in FAFCAB"
    student_1 "You find the professor in FAFCAB"
    professor "Finally, you are here, It took you longer than I expected. Sorry for the rick roll, it became quite boring around here"
    student_1 "You presented your final lab and you finally finished your semester"

    label choices_check_calendar:
    student_1 "You find a strange name of the  event that takes place right now"
    student_1 "Decrypt the name of the event"
    student_1 "You found out that is actually a meeting of an association"
    student_1 "Google the association"

    label choices_8:
        menu:
            "You found a site, but you cannot enter it since it requires a special password"
            "Go through professor's notes and maybe find the password":
                jump choices_look_notes
            "Click on {b}Cannot remember password?{/b}":
                jump choices_click_password

    label choices_look_notes:
        label choices_look_notes_decision:
            menu:
                "You found some notes in another language"
                "Try to translate all of them one by one":
                    jump choices_translate
                "Look through the rest of the notes":
                    jump choices_find_document

        label choices_translate:
        student_1 "You find some weird messages and you decide that it is not your business to look through all of them"
        student_1 "Look through the rest of the notes"
        jump choices_find_document

        label choices_find_document:
        student_1 "You find a document where the professor keeps all a of your marks"

        label choices_9:
            menu:
                "How should I be? How can I do it correctly?"
                "Take advantage of this and write in the document the mark for your final laboratory work":
                    jump choices_advantage
                "Be an honest student and wait for the professor":
                    jump choices_9_common

        label choices_advantage:
        "Finally, after 2 hours the professor came. He had an unexpected meeting at the dean's office and is sorry that you had to wait for so long."
        "He is checking his document with all the marks and sees that you already have one. He thinks he must have forgotten that you already had had a mark and is sorry that you had been waiting for so long"

        label choices_9_common:
        "Finally, after 2 hours the professor came. He had an unexpected meeting at the dean's office and is sorry that you had to wait for so long. He is ready to put a bonus point to your laboratory work"

        label choices_click_password:
        "A clue appears on the screen. It seems like a cipher that you are familiar with. The message hidden was {b}THE SHINING {/b}"

        label choice_10:
            menu:
                "You finally enter the site and there is an actual board where you can see your professor."
                "Close the website":
                    jump choices_9_common
                "Read more":
                    jump choices_read_more

        label choices_read_more:
        student_1 "You see that is an actual site for some professors that are experts in the AI domain. You assume that maybe they are doing a research paper based on AI. You decided to close the website"
        jump choices_9_common

    label choices_book:
        label choices_11:
            menu:
                "You observe that there is an underlined word on almost each page "
                "Write the words on a paper ":
                    jump choices_11_common
                "Continue to analyze the book":
                    jump choices_analyze_book

        label choices_analyze_book:
        student_1 "You discover nothing else and decided to analyze the words"
        jump choices_11_common

        label choices_11_common:
        student_1 "The message hidden was {b}Find me in 310.{/b}"
        student_1 "You find the professor in 310."
        professor "I hope you found the quizzes fun. You can have a bonus point for that"
        jump choices_12_common

    label choices_papers:
        label choices_12:
            menu:
                "You see nothing interesting. Some boring papers abour Machine learning and AI"
                "Wait for the professor a little bit more":
                    jump choices_wait_professor
                "Write him another mail and ask him if there is a possibility to present the laboratory work tomorrow":
                    jump choices_present_lab

        label choices_wait_professor:
        student_1 "You are ready to send the email"
        jump choices_present_lab

        label choices_present_lab:
        "The professor finally came. He was stuck at a conference that had taken place at 13:00."
        jump choices_12_common

        label choices_12_common:
        student_1 "You presented the laboratory work and got the highest mark possible"





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