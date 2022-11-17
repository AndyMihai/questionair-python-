print("If you think your life is in danger please call 999 or to direct to A&E")
print("Let's start knowing eachother by taking so details from you")

name = str(input("Can you please tell me your name? "))

print("Hello " +name+ " nice to meet you")

age = int(input("How old are you " +name))

address = str(input(name+ " Can you please tell us your address?"))

print("Now that we establish who you are we need know we need to know the reaason for")

reason = str(input("So in a one word why is the reason you contacted us today?"))

pain = str(input("Are you in pain?"))

pain_score = int(input("How would you score you pain score form 1-10, 1 the lowest and 10 the highest?"))

allergies = str(input("Do you have any allergies?"))

medication = str(input("Are you taking any regular medication?"))



new_reason_1 = "headache";
new_reason_2 = "chest pain";
new_reason_3 = "migraine";
new_reason_4 = "Bleeding";
new_reason_5 = "Abdominl pain";
new_reason_6 = "UTI";


answer_1 = "yes";
answer_2 = "no";

question_1 = "did that help?";

new_answer_1 = "Do not excede 6gr a day!";
question_2 = "If it did not help?";
new_answer_2 = "Let's try to book you in!";



med_1 = "paracetamol";
med_2 = "ibuprofen";
med_3 = "odansetron";
med_4 = "gaviscon";
med_5 = "imodium";
med_6 = "amitryptilin";

if reason == new_reason_1:
       new_medication = str(input("Have you took any medication?"))
       if new_medication == answer_1:
        new_medication_1 = str(input("What medication did you took?"))
        if new_medication == med_1:
            print(question_1)
            if question_1 == answer_1:
                print(new_answer_1)
                if  question_1 == answer_2:
                    print(new_answer_2)
elif reason == new_reason_2:
     input(pain)
     if pain == answer_1:
        input(pain_score)
        if pain_score >= 7:
            print("Attend A&E")
else:
    print(new_answer_2)