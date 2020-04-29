from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="

@app.route("/")
def home():
    return "<a href='/horoscope'><h1>Check your Horoscope here.</h1></a>"

@app.route("/horoscope")
def horoscope():
    return render_template("HoroscopeData.html")

@app.route("/aries")
def aries():
    sign = "1"
    r = requests.get(url+sign)
    data = r.content
    soup = BeautifulSoup(data,'html.parser')
    p = soup.find_all('p')
    aries_data = p[0].get_text()[14:]
    return render_template("get_data.html", data=aries_data,sign=sign)

@app.route("/taurus")
def taurus():
    sign = "2"
    r = requests.get(url+sign)
    data = r.content
    soup = BeautifulSoup(data,'html.parser')
    p = soup.find_all('p')
    taurus_data = p[0].get_text()[14:]
    return render_template("get_data.html", data=taurus_data,sign=sign)

@app.route("/gemini")
def gemini():
    sign = "3"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    gemini_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=gemini_data)

@app.route("/cancer")
def cancer():
    sign = "4"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    cancer_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=cancer_data)

@app.route("/leo")
def leo():
    sign = "5"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    leo_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=leo_data)

@app.route("/virgo")
def virgo():
    sign = "6"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    virgo_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=virgo_data)

@app.route("/libra")
def libra():
    sign = "7"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    libra_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=libra_data)

@app.route("/scorpio")
def scorpio():
    sign = "8"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    scorpio_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=scorpio_data)

@app.route("/sagittarius")
def sagittarius():
    sign = "9"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    sagittarius_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=sagittarius_data)

@app.route("/capicorn")
def capicorn():
    sign = "10"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    capicorn_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=capicorn_data)


@app.route("/aquarius")
def aquarius():
    sign = "11"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    aquarius_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=aquarius_data)


@app.route("/pisces")
def pisces():
    sign = "12"
    r = requests.get(url + sign)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')
    p = soup.find_all('p')
    pisces_data = p[0].get_text()[14:]
    return render_template("get_data.html", sign=sign,data=pisces_data)

app.run(debug=True)