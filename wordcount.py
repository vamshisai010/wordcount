def count(text):#funtion used to count the words in sentence
    words = text.split()#Split the sentence into words
    return len(words) #print the length or count of the words
def checkinput():#checkinput function checks the input
    print("********************* Welcome to Word Counter! *********************")#print the heading of the program
    while True:
        text = input("Enter a sentence or paragraph (press Enter to quit): ")#User input the sentence or paragraph
        if not text:#Check for empty input to exit the program
            print("Exiting...")#if input is empty or stop the giving input then code prints exiting...
            break
        word_count = count(text)# Count words
        print(f"Word count: {word_count}\n")#Display word count
checkinput()
