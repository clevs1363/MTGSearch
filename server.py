from flask import Flask, request, render_template, url_for
import card
proj2 = Flask(__name__)

@proj2.route("/")
def runIndex():
    return render_template('index.html')

@proj2.route("/graphs.js")
def runGraph():
    return url_for('static', filename='/js/graphs.js')

@proj2.route("/index.css")
def runCSS():
    return url_for('static', filename='/css/index.css')

@proj2.route('/card/<cardname>')
def runCard(cardname):
    ##cardName = request.args.get('cardSearch')
    return card.getInfoList('https://api.scryfall.com/cards/named?fuzzy=%s' % cardname)

if __name__ == '__main__':
    proj2.debug = True
    proj2.run(host = '0.0.0.0', port = 5000)