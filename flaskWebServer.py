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

    resultContents = ""
    if request.method == 'POST':
        print("[" + str(datetime.now()) + "] User Input Query Text: '{0}'".format(request.form['queryText']))
        resultContents = request.form['queryText']



    resultHtmlStr = "<html> <head> </head> <body>"
    resultHtmlStr = resultHtmlStr + "당신이 입력한 텍스트는 '" + resultContents + "'입니다."
    resultHtmlStr = resultHtmlStr + "<br>"
    resultHtmlStr = resultHtmlStr + "<img src='./static/image/img1.jpg'/>"
    resultHtmlStr = resultHtmlStr + "</body> </html>"


    return resultHtmlStr


##########################################
# Main Method
##########################################
if __name__ == "__main__":
    print("[" + str(datetime.now()) + "] Web Server Prepare..")
    app.run(host="127.0.0.1", port="8080")


    print("[" + str(datetime.now()) + "] Web Server is Stopped..")






