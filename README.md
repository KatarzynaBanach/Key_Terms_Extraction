##  Key Terms Extraction
The program helps to quickly get the meaning of a text. It takes a xml file and n - number of most common words, and displays titles of particular articles and n keywords. Created while doing a course on hyperskill.org, based on general schema and guidelines provided by course author (solutions designed on my own) but with some modifications. 
This challanging project was great opportunity to get to know and implement crucial text preprocessing stages, tokenization and lemmatization, use NLTK - an essential NLP library and work with XML files.

**Technologies used:**
- python
- libraries: **_lxml, nltk (tokenize, stem, corpus), sklearn (TfidfVectorizer)_**

Required format of file - example:
![obraz](https://user-images.githubusercontent.com/102869680/192741947-01e64e8e-bc95-4c7e-a169-3b2c28f84073.png)

Result for this example (n = 5):
![obraz](https://user-images.githubusercontent.com/102869680/192742437-45b668ed-b6a8-4178-9545-f681eb798848.png)


