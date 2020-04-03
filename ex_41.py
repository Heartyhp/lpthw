import sys
import random
from urllib.request import urlopen
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
           "class %%%(%%%):":
              "make a class named %%% that is-a %%%",
           "class %%%(object):\n\tdef __init__(self, ***)" :
           "class %%% has a __init__ that takes self and *** params.",
            "class %%%(object): \n\tdef ***(self,@@@)":
            "class a has a function *** that takes self and @@@ as parameters.",
            "*** = %%%()":
            "*** is set to an instance of class",
            "***.*** = '***'" :
            "from *** get the attribute ***and set it to '***'",
            "***.***(@@@)`":
            "from *** get the funnction *** call it with parameters self,@@@"
          }

#do they want to drill phrases first

if len(sys.argv) == 2 and sys.argv[1] == "English" :
   PHRASE_FIRST = True
else :
     PHRASE_FIRST = False


#load up the words from website 

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in randomm.sample(WORDS, snippet.count("%%%"))]
    other_names = random.samples(WORDS, snippet.count("***"))
    results =[]
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]


#fake class name
        for word in class_names:
           result = result.replace("%%%", word, 1)


#fake other names 
        for word in other_names:
           result = result.replace("***", word, 1)

# fake parameter lists
        for word in param_names:
          result = result.replace("@@@" , word, 1)


        results.append(results)

    return results


# keep going until they hit CTRL-D

try:
    while True:
       snippets = list(PHRASES.keys())
       random.shuffle(snippets)
       for snippet in snippets:
           phrase = PHRASES[snipppets]
           question, answer = convert(snippet, phrase)
           if PHRASE_FIRST:
            question, answer = answer, question
           print(question)

           input(">")
           print(f"answer`: {answer}\n\n")
except EOFError:
     print("\nBye")
