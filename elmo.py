import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
#!python -m spacy download en_core_web_md #you will need to install this on first load
import spacy
#from spacy.lang.en import English
nlp = spacy.load('en_core_web_md')
#from IPython.display import HTML
import logging
logging.getLogger('tensorflow').disabled = True #OPTIONAL - to disable outputs from Tensorflow
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

class ELmo():
    def __init__(self,file,search):
        pdf = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        pg = pdfReader.getNumPages()
        text = ""

        for i in range(0, pg):
            PageObj = pdfReader.getPage(i)
            text += PageObj.extractText()

        text = text.lower().replace('\n', ' ').replace('\t', ' ').replace('\xa0', ' ')  # get rid of problem chars
        text = ' '.join(text.split())  # a quick way of removing excess whitespace
        doc = nlp(text)

        sentences = []
        for i in doc.sents:
            if len(i) > 1:
                sentences.append(i.text.strip())  # tokenize into sentences
        url = "https://tfhub.dev/google/elmo/2"
        embed = hub.Module(url)

        embeddings = embed(
            sentences,
            signature="default",
            as_dict=True)["default"]
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.tables_initializer())
            x = sess.run(embeddings)
        #question
        search_string = search
        embeddings2 = embed(
            [search_string],
            signature="default",
            as_dict=True)["default"]

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.tables_initializer())
            search_vect = sess.run(embeddings2)
        cosine_similarities = pd.Series(cosine_similarity(search_vect, x).flatten())
        output = ""
        #print(cosine_similarities)

        for i, j in cosine_similarities.nlargest(3).iteritems():
            output += ''
            for i in sentences[i].split():
                output += " " + str(i)
                """if i.lower() in search_string:
                    output += "\n" + str(i) + "\n"
                else:
                    output += " " +str(i)"""
            output += "\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
        print(output)