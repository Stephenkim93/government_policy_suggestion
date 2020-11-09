from datetime import datetime

doc1_search_field1_words = ['청년', '청년', '정책']
doc1_search_field2_words = ['청년', '창업']

doc2_search_field1_words = ['여성', '정책']
doc2_search_field2_words = ['경단년', '정책']






def makeTFIDFInfoJson(totalDocPostaggingWordsInfo, saveJsonFileName):
    ## tf-idf-info example
    # [
    #     {
    #         "docID": "document_id_1",
    #         "tfidfInfo": {
    #             "maxTF": 3,
    #             "keyInfo": [
    #                 {
    #                     "keyWord": '청년',
    #                     "tf": 3,
    #                     "idf": 1
    #                 },
    #                 {
    #                     "keyWord": '정책',
    #                     "tf": 1,
    #                     "idf": 2
    #                 },
    #                 {
    #                     "keyWord": '창업',
    #                     "tf": 1,
    #                     "idf": 1
    #                 },
    #             ]
    #         }
    #     },
    #     {
    #
    #     }
    # ]
    pass

def makeSearchKeywordIndexing(totalDocPostaggingWordsInfo, saveJsonFileName):
    # [
    #     {
    #         "keyWord": '청년',
    #         "DocIDList" : ['doc1']
    #     },
    #     {
    #         "keyWord": '정책',
    #         "DocIDList": ['doc1', 'doc2']
    #     }
    # ]
    pass

def makeSearchKeywordIndexing_tfidf(totalDocPostaggingWordsInfo, saveJsonFileName):
    # [
    #     {
    #         "keyWord": '청년',
    #         "DocList" : [
    #             {"id": 'doc1',
    #              "tfidf": 0.15}
    #         ]
    #     },
    #     {
    #         "keyWord": '정책',
    #         "DocList": [
    #             {"id": 'doc1',
    #              "tfidf": 0.2},
    #             {"id": 'doc2',
    #              "tfidf": 0.3}
    #         ]
    #     }
    # ]
    pass


doc1_check_field1_words = ['대졸']
doc1_check_field2_words = ['컴공']

doc2_check_field1_words = ['대졸']
doc2_check_field2_words = ['경영']

def makeCheckWordIndex(totalDocCheckFieldAndWordInfo, saveJsonFileName):
    # [
    #     {
    #         'fieldName': '학력',
    #         'indexingInfo': [
    #             {
    #                 'checkWord': "대졸",
    #                 "DocIDList": ['doc1', 'doc2']
    #             }
    #         ]
    #     },
    #     {
    #         'fieldName': '전공',
    #         'indexingInfo': [
    #             {
    #                 'checkWord': "컴공",
    #                 "DocIDList": ['doc1']
    #             },
    #             {
    #                 'checkWord': "경영",
    #                 "DocIDList": ['doc2']
    #             }
    #         ]
    #     }
    # ]

    pass


def getPostaggingFromDoc(doc):
    totalDocPostaggingWordsInfo = []

    # totalDocPostaggingWordsInfo = [
    #     {
    #         "field": "title",
    #         "words": ['청년', '청년', '정책']
    #     },
    #     {
    #         "field": "summary",
    #         "words": ['청년', '창업']
    #     }
    # ]

    return totalDocPostaggingWordsInfo;

def getCheckInfoFromDoc(doc):
    totalDocCheckFieldAndWordInfo = []

    # totalDocCheckFieldAndWordInfo = [
    #     {
    #         "field": "학력",
    #         "words": ['대졸']
    #     },
    #     {
    #         "field": "전공",
    #         "words": ['컨공']
    #     }
    # ]

    return totalDocCheckFieldAndWordInfo;

def preprocessing():
    totalDocPostaggingWordsInfo = []
    totalDocCheckFieldAndWordInfo = []

    allDoc = []

    for doc in allDoc:
        totalDocPostaggingWordsInfo = getPostaggingFromDoc(doc)
        # makeTFIDFInfoJson(totalDocPostaggingWordsInfo, "./tfidfInfoJason.json")
        # makeSearchKeywordIndexing(totalDocPostaggingWordsInfo, "./searchKeywordIndexing.json")
        makeSearchKeywordIndexing_tfidf(totalDocPostaggingWordsInfo, "./searchKeywordIndexing_tdidf.json")

        totalDocCheckFieldAndWordInfo = getCheckInfoFromDoc(doc)
        makeCheckWordIndex(totalDocCheckFieldAndWordInfo, "./checkFieldWordIndexing.json")


def exist(doc, word):
    for w in allWords(doc) 몇십개
        if word == w:
            return True
    return False



def test():
    for word in allWords:   5000
        word_idf = 0
        for doc in allDocs:   1300
            if exist(doc, word):
                word_idf = word_idf + 1





###########################################################
# main execution
if __name__ == "__main__":
    print("[" + str(datetime.now()) + "] PreProcessing is Started..")
    preprocessing()
    print("[" + str(datetime.now()) + "] PreProcessing is Finished..")
