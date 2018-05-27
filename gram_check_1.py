import nltk
import enchant
import inflect


class SentenceSplitter:
    """Used for sentence boundary disambiguation"""
    def __init__(self):
        self.text = raw_input('Enter some text: ')

    def split(self):
        """ Splits the entered text into sentences"""
        return nltk.sent_tokenize(self.text)


class Tagger:
    """Used to tag the words with their part-of-speech"""
    def __init__(self):
        pass

    def tagText(self, tokens):
        """Assigns part-of-speech tag to every word of the sentence"""
        return nltk.pos_tag(tokens)

class Rules:
    """Performs spell-check, indefinite article and following word agreement check"""
    def __init__(self):
        pass

    def spell_check(self, sentence, tokens):
        """Takes sentence and tokens as input where sentence must be a string and tokens must be a list of strings.
        Checks the spelling of each word in the sentence and provides suggestions for the misspelled words and replaces
        the word with the one chosen from suggestions"""
        d = enchant.Dict("en_US")
        b = enchant.Broker()
        b.set_ordering("en_US", "aspell, myspell, ispell")  # Set the ordering of the dictionaries to be used while spell-check.
        d.add('ambivert')  # Add a word to your personal dictionary if you don't want it to be spell-checked.

        isCorrect = []
        self.spellSuggestions = []
        for token in tokens:
            if token.isalpha():
                isCorrect.append(d.check(token))
                if not d.check(token):
                    z = sentence.find(token)
                    self.spellSuggestions = d.suggest(token)
                    print "\nSuggestions: ", self.spellSuggestions
                    y = int(raw_input("\nWhich suggestion nos. did you find correct?\n"))
                    sentence = sentence.replace(sentence[z: z + len(token)], self.spellSuggestions[y - 1])
        return sentence

    def a_vs_an(self, tokens):
        """Checks whether the indefinite article and the following word agree with each other or not.
        Also replaces the wrong article with the correct one.
        Also is able to detect some exceptions like 'a European' and doesn't notify them as errors."""
        inflect1 = inflect.engine()
        # sentence = input('Please enter a sentence: ')
        # words = nltk.word_tokenize(sentence)
        # print(words)
        for i in range(len(tokens)):
            if tokens[i] == 'a' or tokens[i] == 'an':
                x = inflect1.a(tokens[i + 1])
                if tokens[i] == x.split(' ')[0]:
                    return 'There is a good agreement between indefinite article and following word.'
                else:
                    print "Did you mean \"{}\" instead of \"{}\"...".format(x, tokens[i] + ' ' + tokens[i + 1])
                    z = raw_input("Please type 'yes' or 'no': ")
                    if z == 'yes':
                        # lsentence = list(sentence)
                        x = x.split(' ')
                        tokens[i], tokens[i + 1] = x[0], x[1]
                        return " ".join(tokens[:-1])+'.'
                    elif z == 'no':
                        return 'Please give it a thought.'


# Multiple Inheritance
class TextChecker(SentenceSplitter, Tagger, Rules):
    def __init__(self):
        SentenceSplitter.__init__(self)
        Tagger.__init__(self)
        Rules.__init__(self)


t = TextChecker()
sents = t.split()

for sent in sents:
    tokens = nltk.word_tokenize(sent)
    # print tokens
    print "\nPERFORMING SPELL CHECK..."
    spellchecked = t.spell_check(sent, tokens)
    print "Corrected sentence: ", spellchecked
    print "---------------------------------------------------------------"

    print "\nCHECKING INDEFINITE ARTICLE AND FOLLOWING WORD AGREEMENT...\n"
    tokens1 = nltk.word_tokenize(spellchecked)
    a_vs_an_checked = t.a_vs_an(tokens1)
    if a_vs_an_checked is None:
        print 'There is no indefinite article in the sentence.'
    else:
        print "Corrected sentence: ", a_vs_an_checked
        print "---------------------------------------------------------------"
