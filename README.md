# Podcast-text-classifier
Extracting and cleaning text data from transcripts of the podcast "My Brother, My Brother and Me" to build a text-classification/prediction model.

## About
This project's aim is to build a text classifier that predicts which one of the three podcast hosts—Griffin, Justin, or Travis McElroy—is most likely to have said a certain piece of text. 

I started by extracting the data from PDF transcripts of podcast episodes. I then used some classic natural-language-processing (NLP) techniques to clean and format the data, to make it usable and to analyse it. I then did a preliminary analysis of the textual data to understand how it *behaves*, and to look for any possible patterns and trends. This included looking at the most common words and wordclouds of each speaker, seeing if the data was skewed in any way, and looking at the proportions of use for different words.

Finally, I used the data to train and test a multiclass text-classification model. (This is done in *McElroy ML.ipynb*.) This process included testing different algorithms for classification, looking at learning curves to observe any potential bias/variance in the model, analysing the precision/recall of the model, creating confusion matrices, and looking at the misclassified training samples to try and understand what the model might be looking for.

## Files
* *McElroy ML.ipynb*: This is the main Jupyter notebook for the machine-learning part of the project. It contains detailed descriptions of the methods, the results, and a final analysis of the model. (Note: The file *McElroy ML, Report.pdf* is a PDF version of this notebook.)

* *McElroy Analysis.ipynb*: This is the notebook I used for the preliminary analysis of the data (word frequencies, wordclouds, etc.).

* *get_text.py*: This is the Python program that I used to extract and clean up the text data. (I mainly used the libraries `textract` and `nltk` for this.)

The figures and datasets I used can also be found in the repository.
