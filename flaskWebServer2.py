from datetime import datetime
from flask import Flask, render_template, request
import recommendation_code

app = Flask(__name__, template_folder='templates')

@app.after_request
def set_response_headers(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    return r

@app.route('/')
def mainResponse():
    print("[" + str(datetime.now()) + "] Server Request Income: '/'")
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def searchResponse():
    print("[" + str(datetime.now()) + "] Server Request Income: '/search'")

    resultHtmlStr = ""
    if request.method == 'POST':

        # resultList에 실제 검색 결과를 넣으면 됨.
        # resultList = ["id1", "id2"]
        resultList = []
        resultCnt = len(resultList)

        resultHtmlStr = getSearchResultHtml(request.form, resultCnt, resultList)

    return resultHtmlStr

def getSearchResultHtml(requestForm, resultCnt, resultList):
    htmlStr = "<html>"
    htmlStr = htmlStr + "\n" + "<head>"
    htmlStr = htmlStr + "\n" + "</head>"
    htmlStr = htmlStr + "\n" + "<body>"
    htmlStr = htmlStr + "\n" + "    <center>"
    htmlStr = htmlStr + "\n" + "         <table border=\"0\">"
    htmlStr = htmlStr + "\n" + "            <tr>"
    htmlStr = htmlStr + "\n" + "                <td align=\"center\">"
    htmlStr = htmlStr + "\n" + "                    <font size=\"20\">"
    htmlStr = htmlStr + "\n" + "                        청년 정책 검색 시스템 검색 결과"
    htmlStr = htmlStr + "\n" + "                    </font>"
    htmlStr = htmlStr + "\n" + "                </td>"
    htmlStr = htmlStr + "\n" + "            </tr>"
    htmlStr = htmlStr + "\n" + "            <tr><td><br><br>"
    htmlStr = htmlStr + "\n" + "            나이:" + requestForm['userAge']
    htmlStr = htmlStr + "\n" + "            <br><br>"
    htmlStr = htmlStr + "\n" + "            거주지 (시/도):" + requestForm['userLocation']
    htmlStr = htmlStr + "\n" + "            <br><br>"
    htmlStr = htmlStr + "\n" + "            거주지 (시/군/구):" + requestForm['userLocation_Detail']
    htmlStr = htmlStr + "\n" + "            <br><br>"
    htmlStr = htmlStr + "\n" + "            관심정책:" +requestForm['favoritePolicy']
    htmlStr = htmlStr + "\n" + "            <br><br>"
    htmlStr = htmlStr + "\n" + "            검색 내용:" +requestForm['queryText']
    htmlStr = htmlStr + "\n" + "            <br><br></td></tr>"

    if resultCnt > 0:
        htmlStr = htmlStr + "\n" + "            <tr>"
        htmlStr = htmlStr + "\n" + "               <td>"
        htmlStr = htmlStr + "\n" + "                    <br><br>"
        htmlStr = htmlStr + "\n" + "                    총 {0}건이 검색 되었습니다.".format(resultCnt)
        htmlStr = htmlStr + "\n" + "                    <br><br>"
        htmlStr = htmlStr + "\n" + "                </td>"
        htmlStr = htmlStr + "\n" + "            </tr>"
        htmlStr = htmlStr + "\n" + "           <tr>"
        htmlStr = htmlStr + "\n" + "                <td>"
        htmlStr = htmlStr + "\n" + "                    <!-- 검색 결과 반복 시작 -->"
        for data in resultList:
            htmlStr = htmlStr + "\n" + data + "<br>"

        htmlStr = htmlStr + "\n" + "                    <!-- 검색 결과 반복 끝 -->"
        htmlStr = htmlStr + "\n" + "                </td>"
        htmlStr = htmlStr + "\n" + "           </tr>"
    else:
        htmlStr = htmlStr + "\n" + "            <tr>"
        htmlStr = htmlStr + "\n" + "               <td>"
        htmlStr = htmlStr + "\n" + "                    <br><br>"
        htmlStr = htmlStr + "\n" + "                    입력하신 내용에 맞는 검색 결과가 없습니다."
        htmlStr = htmlStr + "\n" + "                    <br><br>"
        htmlStr = htmlStr + "\n" + "                </td>"
        htmlStr = htmlStr + "\n" + "            </tr>"

    htmlStr = htmlStr + "\n" + "         </table>"
    htmlStr = htmlStr + "\n" + "    </center>"
    htmlStr = htmlStr + "\n" + "</body>"
    htmlStr = htmlStr + "\n" + "</html>"

    return htmlStr

##########################################
# Main Method
##########################################
if __name__ == "__main__":
    print("[" + str(datetime.now()) + "] Web Server Prepare..")
    app.run(host="127.0.0.1", port="8080")


    print("[" + str(datetime.now()) + "] Web Server is Stopped..")






