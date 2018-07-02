from googlesearch.googlesearch import GoogleSearch
from bing import Bing
from threading import *
class Simsearch(Thread):
    global process
    def __init__(self,threadID,name,counter,process,search_term):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.process=process
        self.search_term = search_term
    #     self.bing=[]
    #     self.google=[]
    #
    # def runner(self):
    #     if self.process==1:
    #         self.bing = self.run1()
    #     else:
    #         self.google = self.run2()

    def run1(self):
        s=Bing.search(self.search_term)
        return s
        # for re in s:
        #     if re=='results':
        #         for url in s[re]:
        #             print url['link']
    def run2(self):
        res = []
        # a=raw_input("Enter the term to Search")
        response = GoogleSearch().search(self.search_term)
        for result in response.results:
            res.append(result.url)
        return res
#
# if __name__=="__main__":
#     s1=Simsearch(001,"google",0,1)
#     s2=Simsearch(002,"bing",1,2)
#     s1.start()
#     s2.start()
#     s1.join()
#     s2.join()
