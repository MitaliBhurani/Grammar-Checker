# Grammar-Checker
An effort to make a grammar checker using rule-based approach. I am an NLP enthusiast and have done research on AI-powered text proofreaders. You can find the documentation of my research work here: https://docs.google.com/document/d/1e_nczZTnwadzrACvH-z9ykf-0y_7bhzbNdg3AZySd40/edit?usp=sharing 

After doing a considerable research, I have attempted to start with the implementation using the pre-existing libraries like inflect, pyenchant and nltk.

Things I have worked on:

1. Sentence Boundary Detection: Here I have used nltk's sent_tokenize to split the text into sentences. But the issue I faced is that the sent_tokenize doesn't recognise the sentence boundary correctly if there is a period after two consequent abbreviations.

2. Part-of-speech Tagging: Here I have used nltk's pos_tag to assign pos tags to each word of the sentence. This will be used for subject-verb agreement and I am currently working on it.  

3. Spell Check: Here I have used pyenchant. The spell checker here checks spelling, we can also add to personal dictionary, the word that we don't want to be spell checked. 

4. Indefinite Article and following word agreement: Here I have used inflect which also considers exceptions like "a European" is correct and not "an European" and hence is perfect for this purpose.

Future Enhancements:

For Sentence Boundary Detection, https://code.google.com/p/splitta/ is a better option to choose.

For Part-of-speech Tagging, Brill's tagger (built using Transformation Based Learning) can be trained on corpora like Pen TreeBank corpus, Brown corpus etc. This will help obtain better pos tags.

For subject-verb agreement (not included yet in the code), Recurrent Neural Network can be used. One of the works so far includes https://github.com/TalLinzen/rnn_agreement

Usage:

```python
Enter some text: It is a awsome weekand. Sitting at the window, I can see abird chirping.

PERFORMING SPELL CHECK...

Suggestions:  ['awesome', 'aw some', 'twosome', 'winsome', 'someway', 'fearsome']

Which suggestion no. did you find correct?
1

Suggestions:  ['weekend', 'week and', 'weekday', 'weeknight', 'weekly', 'Weeks']

Which suggestion no. did you find correct?
1
Corrected sentence:  It is a awesome weekend.
---------------------------------------------------------------

CHECKING INDEFINITE ARTICLE AND FOLLOWING WORD AGREEMENT...

Did you mean "an awesome" instead of "a awesome"...
Please type 'yes' or 'no': yes
Corrected sentence:  It is an awesome weekend.
---------------------------------------------------------------

PERFORMING SPELL CHECK...

Suggestions:  ['bird', 'rabid', 'a bird']

Which suggestion no. did you find correct?
3
Corrected sentence:  Sitting at the window, I can see a bird chirping.
---------------------------------------------------------------

CHECKING INDEFINITE ARTICLE AND FOLLOWING WORD AGREEMENT...

Corrected sentence:  There is a good agreement between indefinite article and following word.
---------------------------------------------------------------
```





