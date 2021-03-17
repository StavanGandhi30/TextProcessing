from gensim.summarization import keywords
from rake_nltk import Rake

# os.system("! pip3 install rake-nltk")
# os.system("! pip3 install gensim")

class TextRankImpl:
    def __init__(self, text):
        self.text = text

    def getKeywords(self):
        return (keywords(self.text).split('\n'))

class RakeImpl:
    def __init__(self, text):
        self.text = text
        self.rake = Rake()

    def getKeywords(self):
        self.rake.extract_keywords_from_text(self.text)
        return self.rake.get_ranked_phrases()

class main:
    def __init__(self,text):
        self.text = text
    def keyExtractor(self):
        textRankImpl = TextRankImpl(self.text)
        print (textRankImpl.getKeywords()[:50])

        rakeImpl = RakeImpl(self.text)
        print (rakeImpl.getKeywords()[:0])

userInput = "Mohandas Karamchand Gandhi was an Indian lawyer, anti-colonial nationalist, and political ethicist, who employed nonviolent resistance to lead the successful campaign for India's independence from British rule, and in turn inspired movements for civil rights and freedom across the world."
x = main(userInput)
print(x.keyExtractor())