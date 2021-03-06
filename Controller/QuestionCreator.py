import nltk
import sys
import nltk
import re
import time
from gingerit.gingerit import GingerIt

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import random,time
from Controller import vik_test_codes
from Controller  import ConnectionToNeo4j,TextToSpeechConverter,QuestionCreator,NestedQuestionCreator,vari,test,AudioRecorder,SpeachToText

sys.path.insert(0, '../Database')
from Database import NonTechnicalQuestionDirectory
from nltk.stem import WordNetLemmatizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
a={}
b=[]
train_text = state_union.raw("2005-GWBush.txt")
# keywords ="Object oriented programming"


question = ""

# l1 = ['NNP','JJ','NNS']
# l2 = ["NN","PRP"]
# l3 = ["PRP$","NNS"]
# l4 = ["PRP$","JJ","NN"]
# l5 = ["JJ","NNS"]


# def gen_Question():
#     # if type(sentence) is str
#     db = "CV"
#     node_Count = ConnectionToNeo4j.getNodeCount(db)
#     lang = 'en'
#     q_list = []
#     for id in range(1,node_Count+1):
#         q_list.append(str(id))
#     print(q_list)
#
#     # process_content()
#     # print((word, tag)for word, tag in sentence if tag in ('NN', 'JJ'))
#
#



def gen_Question(keywords,qno):
    typo = "nonested"
    typo2 = "nontechnical"
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(keywords)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            # gen_Question(namedEnt)
            # namedEnt.draw()


        key, words = zip(*tagged)
        compare = list(words)
        #print(key)
        print(words)
        a = dict(zip(key, words))
        b= dict(zip(words, key))

        print(a)
        print("hey")
        print([b for b, v in a.items() if v in NonTechnicalQuestionDirectory.l1])

    except Exception as e:
        print(str(e))


    if compare == NonTechnicalQuestionDirectory.l1:
        question = "What "+ b['NNP']
        # print(question)
    elif compare == NonTechnicalQuestionDirectory.l2:
        question = "Why should we " +b['NN']+" "+ b['PRP']+"?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l3:
        question = "What are " + b['PRP$'] + " " + b['NNS'] + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l4:
        question = "Tell about " + b['PRP'] + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l5:
        question = "What are your " + b['JJ'] + " " + b['NNS']  + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l6:
        question = "What is  " + b['PRP$'] + " " + b['JJ'] +" "+b['NN'] + "?"
        # print(question)
    else:
        question = "Explain about your " + keywords+" and its technologies?"
        # print(question)


    parser = GingerIt()
    grammer_corrected_question_list = parser.parse(question)
    grammer_corrected_question = grammer_corrected_question_list.get("result")
    print(grammer_corrected_question)
    print(vik_test_codes.question(grammer_corrected_question, qno))
    voice_record = AudioRecorder.audio_recorder(qno)
    answer_validity = SpeachToText.validation("", typo2, typo, "question" + str(qno))[0]



    return question


# gen_Question(keywords)