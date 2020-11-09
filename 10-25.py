from datetime import datetime
'''
IDF 만드는법 

def exist(doc, word):
    for w in allWords(doc)
    if word == w:
        return True
    return False

def test():
    for word in allWords:
        word_idf=0
        for doc in allDocs:
            if exist(don, word):
'''

CheckResult =["d1","d3","d5"]
SearchResult=[["d1",23],["d3",34],["d5",32]]
commonResult = ["d1","d6"]
'''
query 짜는 법
userquery = {
    checkOption ={
        "나이" : 25
        "관심정책" : "창업"
    },
    searchOption = "개발 인공지능 빅데이터"
}
'''
def serachMain(userquery):

    CheckResult = getCheckResult(userquery[checkOption])


    SearchResult = getSearchResult{userquery[searchOption]}


    commonResult = getCommon(CheckResult,SearchResult)

for docId in commonResult:
    if ageCheck &dateCheck:
        add finalResult
if need sort(finalResult)
return finalResult
