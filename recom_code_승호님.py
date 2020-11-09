from datetime import datetime
import json
import konlpy
from konlpy.tag import Kkma, Komoran, Hannanum
import os
# print(os.getcwd())
#//// -> C:\Users\Playdata\Desktop\정책분석>

def getPostaggingResult(searchQuery):

    #//// searchQuery로 들어온 단어를 'kkma'함수를 활용하여 result_list를 만들어야 함

    ##파라미터로 받아들어온 값(searchQuery): '개발인공지능빅데이터'
    searchQuery_list = list()

    komoran = Komoran()
    KomoranList = komoran.nouns(searchQuery) #결과 자체가 list로 반환됨

    #//// 1글자 데이터는 삭제(final.json에서도 자체적으로 '1글자 데이터'는 모두 삭제했음)
    #//// 문제: '빅데이터'는 자체적으로 '빅'과 '데이터'로 분할.
    #//// 검색의 정확성?을 높일 수 있는 방법 없을까?: ex) 빅데이터 - 데이터 - 공공데이터 등의 연관성 높이기? 

    for word in KomoranList:
        if len(word) < 2:
            KomoranList.remove(word)
            
    result = KomoranList 

    return result




#///// => searh_db 가져오는 함수
def loadSearchInfo():
    f = open("./final.json", 'r', encoding='utf-8')
    readLine = ""
    while True:
        line = f.readline()
        if not line: break
        
        readLine = readLine + line.strip()
    f.close()
    initDict4Search = json.loads(readLine)
    searchDataList = initDict4Search['data4search']
    return searchDataList




#//// => check_db 가져오는 함수
def loadCheckInfo():
    f2 = open("./final2.json", 'r', encoding='utf-8')
    readLine2 = ""
    while True:
        line2 = f2.readline()
        if not line2: break
        
        readLine2 = readLine2 + line2.strip()
    f2.close()
    initDict4Check = json.loads(readLine2)
    checkDataList = initDict4Check['data4check']
    return checkDataList



#checkOption_DB_List 예시
{
        "documnet_number" : "1",
        "documnet_info" : 
            {
                "locationCode" : "경기",
                "location" : "경기 성남시",
                "interestPol" : "교육, 훈련",
                "yearMin" : "99999",
                "yearMax" : "99999",
                "startDate" : "99999",
                "endDate" : "99999"
            }
        
    }


def getCheckResult(userQuery):
    checkOption_DB_List = loadCheckInfo()
    print("[" + str(datetime.now()) + "] Database(list) for check Option is loaded: Total {0} policy..".format(len(checkOption_DB_List)))

    userLocationCode = userQuery['checkOption']['locationCode']
    userLocation= userQuery['checkOption']['location']
    userInterestPol = userQuery['checkOption']['interestPol']
    userYear = userQuery['checkOption']['year']

    checkResult = list()
    for db_dict in checkOption_DB_List:
        if userLocationCode == db_dict['documnet_info']['locationCode'] and userLocation == db_dict['documnet_info']['location'] and userInterestPol == db_dict['documnet_info']['interestPol']:
            if userYear >= db_dict['documnet_info']['yearMin'] and userYear <= db_dict['documnet_info']['yearMax']:
                if int(datetime.today().strftime('%Y%m%d')) >= db_dict['documnet_info']['startDate'] and int(datetime.today().strftime('%Y%m%d')) <= db_dict['documnet_info']['endDate']:
                    checkResult.append(db_dict['documnet_number'])

    #논의 사항1: 날짜 지정 기능이 필요함. (why? datetime.today로 하면 2020년 11월쯤이라, 정책의 대부분이 끝났을 시기)
    return checkResult




#///// => search Result를 구하는 함수
def getSearchResult(searchQuery):
    #search4Word_DB_List = final.json 파일
    search4Word_DB_List = loadSearchInfo()
    print("[" + str(datetime.now()) + "] Database(list) for word based Searching is loaded: Total {0} words..".format(len(search4Word_DB_List)))

    #qWordList = ['개발', '데이터', '인공지능']
    qWordList = getPostaggingResult(searchQuery) 
    print("[" + str(datetime.now()) + "] Words in User Query: {0}".format(searchQuery), "->", str(qWordList))


    searchDocDict = {}

    for db_dict in search4Word_DB_List:
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
                        #//// tfidf의 점수를 왜 합칠까? 다시 Logic 이해하기

                    addCnt = addCnt + 1

            if isExist:
                print("[" + str(datetime.now()) + "] '{0}' word Search Success. {1} results".format(qWord, addCnt))

    print("[" + str(datetime.now()) + "] Total Search Result Count: {0}".format(len(searchDocDict)))
    searchDocDict_sorted = sorted(searchDocDict.items(), key=(lambda x: x[1]), reverse = True)

    return searchDocDict_sorted




def searchMain(userQuery):
    
    # ////getCheckResult 함수 제작해야 함
    # ////checkOption을 만족하는 'documet 번호'가 담긴 result_list를 output으로
    # ////=> return ["d1", "d3", "d6"]
    checkResult = getCheckResult(userQuery['checkOption'])
    print("[" + str(datetime.now()) + "] check Info Info :", checkResult)

    searchResult = getSearchResult(userQuery['searchOption'])
    print("[" + str(datetime.now()) + "] Search Info :", searchResult)
    
    #////searchResult와 checkResult의 교집합 구하는 코드
    finalResult = list()
    for checkDoc in checkResult:
        for i in range(len(searchResult)):
            for searchTuple in searchResult:
                if checkDoc == searchTuple[i][0]:
                  finalResult.append(searchTuple)
    return finalResult




########################################main
if __name__ == "__main__":
    print("[" + str(datetime.now()) + "PreProcessing is Started..")

    userQuery = {'checkOption' : {"locationCode" : "경기", "location": "경기 성남시", "interestPol" : "창업", "year" : "28"}, 'searchOption' : "개발인공지능빅데이터"}
    finalSearchResult = searchMain(userQuery)

    print("[" + str(datetime.now()) + "Preprocessing is Finished")