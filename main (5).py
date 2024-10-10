score = 0

questions=\
  {
    "Rosa Parks":"She sat on a bus when they asked her to move",
    "Spain":"Madrid",
    "France":"Paris",
    "Portugal":"Lisbon",
    "New Zealand":"Wellington",
    "the Netherlands":"Amsterdam",
    "Madagascar":"Antananarivo",
    "Germany":"Berlin",
    "Switzerland":"Bern",
    "China":"Beijing",
    "Serbia":"Belgrade",
    "South Africa":"Cape Town",
    "Thailand":"Bangkok",
    "Iraq":"Baghdad"
    #add more Qs here
}

for question, answer in questions.items():
    response = input("What did %s do in the civil rights movement?\n--->" % question)
    if response.capitalize() != answer:
        print("No, %s %s." % (question, answer))
    else:
        print("Yes, that's correct!")
        score += 1

print("You got %d out of %d!" % (score, len(questions)))

if score < len(questions)/3:
   print("better luck next time")
else:
 print("Well Done!")