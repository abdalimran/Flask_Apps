from flask import Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import render_template
import re

app = Flask(__name__)

@app.route("/")
@app.route("/<country>")
def get_events(country='Bangladesh'):
    url = "http://www.ieee.org/conferences_events/conferences/search/index.html?KEYWORDS=&CONF_SRCH_RDO=conf_date&RANGE_FROM_DATE=&RANGE_TO_DATE=&REGION=Region10-Asia+and+Pacific&COUNTRY={}&RowsPerPage=10&PageLinkNum=10&ActivePage=1&SORTORDER=desc&SORTFIELD=start_date".format(country)
    content = urlopen(url)
    soup = BeautifulSoup(content,'lxml')
    conference_table = soup.findChildren('table',class_='nogrid-nopad')
    all_events = re.sub('<img.*?/>', '', str(conference_table))[1:-1]
    final_list = re.sub('(?i)(<a href=")', '<a href="https://www.ieee.org', all_events) 

    return render_template("layout.html", events=final_list)

if __name__ == "__main__":
    app.run()