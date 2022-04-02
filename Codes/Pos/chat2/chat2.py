#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import functools
import numpy as np
from spellchecker import SpellChecker
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Embedding, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random 

#############################################################################################
#
# PREPARAÇÃO E TREINAMENTO DO MODELO
#
#############################################################################################

sp = SpellChecker(language="pt")

#Carregar perguntas e resspostas
qdf = pd.read_csv (r'/home/fabiocarlesso/Downloads/RedesNeurais/novo/chat/perguntas.csv',sep=",")
adf = pd.read_csv (r'/home/fabiocarlesso/Downloads/RedesNeurais/novo/chat/respostas.csv',sep=",")
fdf = pd.read_csv(r'/home/fabiocarlesso/Downloads/RedesNeurais/novo/chat/filmes.csv', sep=",")

#Verificar ortografia e colocar em minúsculas
def spck(sentences):
    checked_q = []
    for sentence in sentences:
        q = ""
        for word in sentence.lower().split():
          q = q+" "+sp.correction(word)
        checked_q.append(q)
    return checked_q

#Converter perguntas para minúsculas    
qdf.question = spck(qdf.question)

max_len = 50
max_words = 5000

#Tokenizar e codificar as perguntas
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(qdf.question)
sequences = tokenizer.texts_to_sequences(qdf.question)

#Criar inputs e labels
x_train = pad_sequences(sequences, maxlen=max_len)
y_train = to_categorical(qdf.answer_id)

#Criar o modelo
model = Sequential()
model.add(Embedding(960, 8, input_length= max_len))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(100))
model.add(Dense(adf.id.max()+1, activation = 'softmax'))

opt = optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss='binary_crossentropy',metrics=['acc'])

history = model.fit(x_train, y_train, epochs=1500, batch_size=len(x_train))
 
prediction = model(x_train)
print(prediction)
np.argmax(prediction, axis=1) 

categoria = None;
while(True):
    sentence = input("Você: ")
    sentence = tokenizer.texts_to_sequences([sentence.lower()])
    sentence = pad_sequences(sentence, maxlen=max_len)
    prediction = model(sentence)
    category = np.argmax(prediction, axis=1)[0]
    answer = adf.query('id=='+str(category)).to_numpy()
    print(answer[0][1])
    if answer[0][0] < 13:
        categoria = answer[0][1]
    if answer[0][0] == 20:
        if categoria == None:
            'pois bem, me descreva susintamente o tipo de filme que deseja assistir?'
        else:
            filmes = fdf[(fdf == categoria).any(axis=1)]
            filmes = list(filmes.Filme)
            print('     * ',filmes[random.randrange(0,len(filmes))])

#############################################################################################
#
# CAPTURA E RECONHECIMENTO DE VOZ E RESPOSTA
#
#############################################################################################
# =============================================================================
# 
# import speech_recognition as sr
# import win32com.client as wincl
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Rate=3
# 
# #Para MacOS e Linux
# # import os
# # os.system('say "'+answer+'"')
# 
# def recognize_speech_from_mic(recognizer, microphone):
#     transcription = ""
#     with microphone as source:
#         audio = recognizer.listen(source)
#         try:
#             transcription = recognizer.recognize_google(audio, language="pt-BR")
#         except sr.RequestError:
#             print("API unavailable")
#         except sr.UnknownValueError:
#             pass
#     return transcription  
# 
# recognizer = sr.Recognizer()
# microphone = sr.Microphone()
# 
# with microphone as source:
#     recognizer.adjust_for_ambient_noise(source)
# 
# speak.Speak("Olá, sou a Janaína, vamos começar?")
# while(True):
#     sentence = recognize_speech_from_mic(recognizer, microphone)
#     if(sentence==""): continue
#     print("Você: "+sentence)
#     sentence = tokenizer.texts_to_sequences(spck([sentence]))
#     sentence = pad_sequences(sentence, maxlen=max_len)
#     prediction = model(sentence)
#     category = np.argmax(prediction, axis=1)[0]
#     answer = adf.query('answer_id=='+str(category)).to_numpy()
#     print("Janaína: "+answer[0][1])
#     speak.Speak(answer[0][1])
# =============================================================================
