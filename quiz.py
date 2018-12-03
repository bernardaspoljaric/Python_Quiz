from random import shuffle
from collections import defaultdict
print "Enter your name: "
name = raw_input()
while True:
    print "------------------------------------------------------"
    print "Hello "+ str(name)
    option = raw_input("Do you want to: \n1.Play Game -- play \n2.Add new questions -- newQuestions\n3.See rang list -- rangList\n4.Exit Game -- exit\nYour answer: ")
    print "------------------------------------------------------"
    if(option == '1' or option == 'play'):
        with open("questions.txt") as file:
            lines = file.readlines()
        shuffle(lines)
        Correct = 0
        Inccorrect = 0
        for line in lines[:20]:
            question , rightAnswer = line.split("-")
            rightAnswer = rightAnswer.strip()
            answer = raw_input(question + ' ')
            if answer.lower() == rightAnswer:
                print "Correct!"
                Correct += 1
            else:
                print "Inccorrect!"
                Inccorrect +=1
        print " Your final score is: " + str(Correct) +" correct answers and " + str(Inccorrect) + " incorrect answers."
        file = open("ranglist.txt", "a")
        file.write("\n" + name + " " + str(Correct))
        file.close()
        
    elif(option == '2' or option == 'newQuestions'):
        print "Please enter your question in form: question-right answer(right answer must be lower case)."
        print "How many questions would you like to add?"
        num = int(raw_input())
        file = open("questions.txt", "a")
        i = 0
        while i != num:
            print "Enter question: "
            newQuestion = raw_input()
            file.write("\n" + newQuestion)
            i += 1
        file.close()
        
    elif(option == '3' or option == 'rangList'):
        print " TOP 10: "
        result = defaultdict(int)
        with open('ranglist.txt', 'r') as f:
            for line in f:
                key, value = line.rsplit(' ', 1)
                result[key] += int(value.strip())
        i = 0
        for key, value in result.iteritems():
            if i < 10:
                print key, value
                i += 1
    elif(option == '4' or option == 'exit'):
        break