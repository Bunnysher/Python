# Import Libraries
import os
import collections
import numpy

# Imports weather data--------------------------------------------------------------------------------------------------------

# Setting the data folder
data = "C:\\Users\\Stergina\\Desktop\\Project\\lingspam_public"
files = os.listdir(data)

# Promts user to choose one of the data folders
choice = raw_input("Dataset Options:\nbare = 1\nlemm = 2\nlemm_stop = 3\nstop = 4\n\nYour choice: ")
 
# Promts user to choose if we should use Term Frequency-Inverse Document Frequency
IDF_option = raw_input("\nIDF Options:\nYes = 1\nNo = 2\n\nYour choice: ")
 
# Convert string to int type
choice = int(choice)
IDF_option = int(IDF_option)

# Based on user's input we choose the respective folder's data
if choice == 1:
    subf = data+"\\bare\\"
elif choice == 2:
    subf = data+"\\lemm\\"
elif choice == 3:
    subf = data+"\\lemm_stop\\"
elif choice == 4:
    subf = data+"\\stop\\"
else:
    print ("Invalid number. Try again..!")
    
# Chosen training and testing data's path
train_dir = subf + "train\\"
train_files = os.listdir(train_dir)
train_count = len(train_files)

test_dir = subf + "test\\"
test_files = os.listdir(test_dir)
test_count = len(test_files)

# Finds spam and ham emails in training datasets
ham = [] 
spam = []
for x in range(0,train_count):
    if 'spmsga' in train_files[x]:
        spam.append(train_files[x])
    else:
        ham.append(train_files[x])

# Finds the probability of having a ham and a spam email, respectively
PHam = float(len(ham))/float(train_count)
PSpam = float(len(spam))/float(train_count)     

# Reads and stores training data's words for all, spam and ham emails
all_dict = []
ham_dict = []
spam_dict = []

for x in range(0,train_count):
    with open(train_dir + train_files[x], 'r') as f:
       contents = f.readlines()
       words = str(contents).split()
       list_set = set(words) 
       words = (list(list_set)) 
       all_dict += words  
       if train_files[x] in ham:
           words = str(contents).split()
           list_set = set(words) 
           words = (list(list_set)) 
           ham_dict += words  
       elif train_files[x] in spam: 
           words = str(contents).split()
           list_set = set(words) 
           words = (list(list_set)) 
           spam_dict += words       
           
# Find's each word's frequency in all, ham and spam emails respectively
all_wordfreq = collections.Counter(all_dict)
ham_wordfreq = collections.Counter(ham_dict)
spam_wordfreq = collections.Counter(spam_dict)

# Reads each test dataset one by one and asseses if it is a spam or ham
false_neg = 0; # False negative are spam emails misclassified as hams
true_neg = 0; # True negative are ham emails classified as hams
false_pos = 0; # False positive are ham emails misclassified as spams
true_pos = 0; # True positive are spam emails classified as spams

# For loop
for i in range(0,test_count):
    
    # Initializations
    word_spam = []
    word_ham = []
    sub = []
    bayes = add = IDF = 0
        
    # Reads test text messages one by one and stores its unique words
    with open(test_dir + test_files[i], 'r') as f:
       contents = f.readlines()
       words = str(contents).split()
       list_set = set(words) 
       words = (list(list_set))    

       # Calculates the probability of a word being in ham or spam emails using Laplace's smoothing (a=1)
       for j in range(0,len(words)):
           
           # Calculates Term Frequency-Inverse Document Frequency based on user's input
           if IDF_option == 1:
               if all_wordfreq[words[j]] == 0:
                   IDF = 0
               else:
                   IDF = numpy.log10(len(train_files)/(all_wordfreq[words[j]]))
           else:
               IDF = 1
               
           # Calculates the probability of being ham or spam, respectively
           word_ham.append((ham_wordfreq[words[j]]/float(len(ham))) * IDF + 1)
           word_spam.append((spam_wordfreq[words[j]]/float(len(spam))) * IDF + 1)

       # Calculates naive Bayes
       word_ham = numpy.log10(word_ham)
       word_spam = numpy.log10(word_spam)
       sub = [x-y for x, y in zip(word_spam,word_ham)]
       add = reduce(lambda x, y: x+y, sub)
       bayes = numpy.log10(PSpam) - numpy.log10(PHam) + add
       
       # Finds if message is really spam or ham
       if (bayes <= 0 and 'spmsga' in test_files[i]):
           false_neg += 1
       elif (bayes <= 0 and 'spmsga' not in test_files[i]): 
           true_neg += 1   
       elif (bayes > 0 and 'spmsga' in test_files[i]): 
           true_pos += 1   
       elif (bayes > 0 and 'spmsga' not in test_files[i]):
            false_pos += 1     
       else:
           print("Something went wrong!")
           
# Prints the correct percentage
perc = round(float(true_neg + true_pos) / float(test_count),2)
print "Correct % :",perc