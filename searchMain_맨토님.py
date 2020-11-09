from datetime import datetime
import json



def getPOSTaggingResult(queryStr):

    result = ['개발', '인공지능', '빅데이터']
    return result


def loadSearchInfo():
    f = open("./final.json", 'r')
    readLine = ""
    while True:
        line = f.readline()
        if not line: break

        readLine = readLine + line.strip()

    f.close()
    initDict4Search = json.loads(readLine)
    searchDataList = initDict4Search['data4search']

    return searchDataList




def getSearchResult(searchQuery):
    search4Word_DB_list = loadSearchInfo()
    print("[" + str(datetime.now()) + "] Database(List) for Word based Searching is loaded: Total {0} words..".format(len(search4Word_DB_list)))

    qWordList = getPOSTaggingResult(searchQuery)
    print("[" + str(datetime.now()) + "] Words in User Query: {0}".format(searchQuery), "->", str(qWordList))


    searchDocDict = {}
    for db_dict in search4Word_DB_list:
        for qWord in qWordList:
            isExist = False
            addCnt = 0
            if db_dict['keyWord'] == qWord:
                isExist = True
                for doc_dict in db_dict['DocList']:
                    if searchDocDict.get(str(doc_dict['doc_id'])) == None:
                        searchDocDict[str(doc_dict['doc_id'])] = doc_dict['tfidf']
                    else:
                        searchDocDict[str(doc_dict['doc_id'])] = searchDocDict.get(str(doc_dict['doc_id'])) + doc_dict['tfidf']
                    addCnt = addCnt + 1
            if isExist:
                print("[" + str(datetime.now()) + "] '{0}' word Search Success. {1} results".format(qWord, addCnt))

    print("[" + str(datetime.now()) + "] Total Search Result Count: {0}".format(len(searchDocDict)))
    searchDocDict_sorted = sorted(searchDocDict.items(), key=(lambda x: x[1]), reverse = True)

    return searchDocDict_sorted







def searchMain(userQuery):

    # checkResult = getCheckResult(userQuery[checkOption])
    # checkResult = ["d1", "d3", "d6"]

    searchResult = getSearchResult(userQuery['searchOption'])
    print("[" + str(datetime.now()) + "] Search Info: ", searchResult)
    # searchResult = [["d1", 0.7], ["d4", 0.5], ["d6", 0.3]]

    # commonResult = getCommon(checkResult, searchResult)
    # commonResult = ["d1", "d6"]

    # for docId in commonResult
    #     if ageCheck & dateCheck:
    #         add finalResult
    #
    # if need sort(finalResult)

    finalResult = searchResult
    return finalResult



###########################################################
# main execution
if __name__ == "__main__":
    print("[" + str(datetime.now()) + "] PreProcessing is Started..")

    userQuery = {'checkOption': { "나이": 25, "관심정책": "창업" }, 'searchOption': "개발인공지능빅데이터"}
    finalSearchResult = searchMain(userQuery)

    print("[" + str(datetime.now()) + "] PreProcessing is Finished..")