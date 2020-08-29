import textract
import nltk
from nltk.corpus import stopwords
from collections import defaultdict, Counter
import glob
import csv
import pandas as pd

#A program to create a csv of words/lines spoken by each person in the podcast

stop_words = stopwords.words("english") #list of insignificant words like "a", "the", etc.
additional_stopwords = ["thats", "im", "laughs", "laughing", "laughter", "youre", "gon", "na", "would", "dont", "could", "theres", \
    "one", "two", "three", "get", "got", "audience", "cheers", "go", "know", "say", "make", "heres", "didnt", "hes", "let", "says", "wasnt", \
        "lets", "theyre", "us", "right", "think", "good", "okay", "time", "much", "cant", "something"] #can add other words you don't want in the analysis
for word in additional_stopwords:
    stop_words.append(word)



boy_words = {} #dictionary where we'll store the lists of words spoken

speakers = ["justin", "travis", "griffin"] #three main hosts




#Change this to your directory where you have the PDFs of the transcripts stored
files = glob.glob(r"C:\Users\arnav\OneDrive - OnTheHub - The University of Oxford\Documents\Coding, Summer 2020\McElroy Code\Transcripts\*.pdf")



i=442 #earliest episode in your directory

boy_words_lines = defaultdict(list) #dictionary with {speaker: [list of lines]}

for filename in files[:]:

    print("Currently transcribing episode number: " + str(i))


    # Read text of the transcript file
    text = textract.process(filename)
    text = text.decode("utf-8") #convert to normal string



    #Clean up the text
    text = text.split("MBMB", 1)[1] #this is where the actual podcast starts
    text = text.lower() #all lowercase
    mypunc = r"!\"#$%&\'()*+,-./;<=>?@[\\]^_`{|}~…‗–‖‘—’”“‟„" #define punctuation you don't want
    text = text.translate(str.maketrans("", "", mypunc)) #remove punctuation
    text = text.replace("―", " ") #remove en-dashes
    text = text.replace("\x0c", "") #remove this other random puctuation that wasn't going away



    #Organise all the text
    lines = text.split("\r\n") #split all the different lines
    lines = [line for line in lines if line != ""] #remove all empty list elements


    


    #Sort all the speech by speaker

    current_speaker = None #running variable of who the speaker is

    for line in lines: #loop through all the lines
        if ":" in line:
            speak = line.split(":", 1) #separate speaker from speech
            current_speaker = speak[0] #set the current speaker
            boy_words_lines[current_speaker].append(speak[1]) #add their speech to the dictionary
        else:
            boy_words_lines[current_speaker].append(line)

    i = i+1 #move to next episode




    #At this point, we have a dictionary with {speaker: [list of all the different lines said by them]}
    #We need to change that to a list of individual words
        

    #For a list of individual words, uncomment everything between the *** signs

    #***UNCOMMENT BELOW FOR LIST OF WORDS***


    for speech in boy_words_lines.items(): #loop through all the tuples (speaker, [list of lines])
        speaker = speech[0] #set speaker
        list_of_lines = speech[1] #set list of lines

        new_list = [] #list to which individual words will be added

        for phrase in list_of_lines: #loop through all the lines
            words = nltk.word_tokenize(phrase) #separate that line into the different words

            for word in words:
                if word == "fucking": #change all instances of "fucking" to "fuckin" (for cleaner results)
                    word = "fuckin"
                    new_list.append(word) #add to new_list
                else:
                    new_list.append(word) #add all the individual words to new_list
        
        new_list = [word for word in new_list if not word in stop_words] #remove all the unimportant words

        if speaker in boy_words.keys(): #check if the speaker was in previous transcribed episodes too
            for word in new_list:
                boy_words[speaker].append(word) #add words to speaker's dictionary entry
        else:
            boy_words[speaker] = new_list #if new speaker, create their list



#Only keep words spoken by one of the three main hosts

boy_words = {speaker: boy_words[speaker] for speaker in speakers}


#We now have a dictionary with {speaker: [list of individual words]}


df = pd.DataFrame.from_dict(boy_words, orient="index").transpose()


#Create csv based on individual word percentages:

#Get lists/series of the boys' words, and remove NaN values
justin = df["justin"].dropna()
travis = df["travis"].dropna()
griffin = df["griffin"].dropna()

#Make dictionaries with the different words and their frequencies
g = Counter(griffin)
t = Counter(travis)
j = Counter(justin)

boy_words_2 = {} #final DataFrame

#Get relative uses of the words
for (k, lst) in boy_words.items():
    for word in lst: #go through each word
        #pick out the frequencies for that word
        g1 = g[word]
        t1 = t[word]
        j1 = j[word]
        tot = g1 + t1 + j1

        if tot==0:
            gp, tp, jp = 0, 0, 0 #if none of them have said it
        else:
            #gp, tp, jp are the percentages
            gp = (g1/tot)*100
            tp = (t1/tot)*100
            jp = (j1/tot)*100

        #Comment out one or the other below, depdending on what you want

        #if (gp > 42 or gp < 24) or (tp > 42 or tp < 24) or (jp > 42 or jp < 24): #"sufficiently unique" (defined in terms of percentages)

        if True: #if you want all words
            if k in boy_words_2.keys():
                boy_words_2[k].append(word)
            else:
                boy_words_2[k] = []
        else:
            pass


        
#***UNCOMMENT ABOVE FOR LIST OF WORDS***

boy_words_lines = {speaker: boy_words_lines[speaker] for speaker in speakers}



#Final DataFrame:


#Set argument as "boy_words_lines" if you want lines spoken, otherwise "boy_words_2"
df = pd.DataFrame.from_dict(boy_words_2, orient="index").transpose()


#Save csv (check whether it's a list of words or lines)

df.to_csv(r"C:\Users\arnav\OneDrive - OnTheHub - The University of Oxford\Documents\Coding, Summer 2020\McElroy Code\Datasets\words_70.csv")