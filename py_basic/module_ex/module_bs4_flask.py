from flask import Flask
app = Flask(__name__)
from urllib import request
from bs4 import BeautifulSoup

@app.route("/")
def hello():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    soup = BeautifulSoup(target, "html.parser")

    output=""
    for location in soup.select("location"):
        # print("도시:", location.select_one("city").string)
        # print("날씨:", location.select_one("wf").string)
        # print("최저기온:", location.select_one("tmn").string)
        # print("최고기온:", location.select_one("tmx").string)
        # print()
        output+="<h3>{}<h3>".format(location.select_one("city").string)
        output+="날씨: {}<br/>".format( location.select_one("wf").string)
        output+="최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output+="<hr/>"
    return output
    

