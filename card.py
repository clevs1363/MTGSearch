## X-LvuVxheR17ARLHWGW09WzYf19CefVIC6disrFPpgrVVmhHNISvNQbBuzVGN2E4OUeERL7w5YfKwHyDy1rTxv3XtafSdV0JVC_9W3xt3S2daVZuf4ZQSdLBq1nSOrMDvTevKwT6dY46L9QMlRsoAnO-vw8PJRRpJhxUjtU8irve4A6wvyO35wdskdWwruYGDwZ9FPMvxjEpHp1aYkOpU2ifleG9s9pcp8tttVB1aDOTuGnym3PT0j8QevXyCExsMoPwA-EMpglDNSaX4xFgX9DNGqEYLZZ7ApjxSJILGbJoLUGnDnmmB_emHAf2JVgxRR_7Tw
import json
import urllib.request
import requests

def getInfoList(scryfallURL):
    ##Get Scryfall API Info
    infoList = []
    scryfallJSON = requests.get(scryfallURL)
    scryfallArr = scryfallJSON.json()
    cardImage = scryfallArr['image_uris']['normal']
    cardName = scryfallArr['name']
    tcgID = scryfallArr['tcgplayer_id']
    ##Add image and prices to info list
    infoList.append(cardImage)
    ##Get pricing from TCGPlayer API
    tcgURL = "http://api.tcgplayer.com/v1.19.0/pricing/product/{0}".format(tcgID)
    tcgHeader = {'Authorization': 'bearer X-LvuVxheR17ARLHWGW09WzYf19CefVIC6disrFPpgrVVmhHNISvNQbBuzVGN2E4OUeERL7w5YfKwHyDy1rTxv3XtafSdV0JVC_9W3xt3S2daVZuf4ZQSdLBq1nSOrMDvTevKwT6dY46L9QMlRsoAnO-vw8PJRRpJhxUjtU8irve4A6wvyO35wdskdWwruYGDwZ9FPMvxjEpHp1aYkOpU2ifleG9s9pcp8tttVB1aDOTuGnym3PT0j8QevXyCExsMoPwA-EMpglDNSaX4xFgX9DNGqEYLZZ7ApjxSJILGbJoLUGnDnmmB_emHAf2JVgxRR_7Tw'}
    tcgJSON = requests.get(tcgURL, headers=tcgHeader)
    tcgInfo = tcgJSON.json()
    print(tcgInfo)
    for item in tcgInfo['results']: 
        lowPriceArr = [] 
        if item['lowPrice'] != None:
            lowPriceArr.append(item['lowPrice'])
        lowPrice = getAv(lowPriceArr)
        midPriceArr = [] 
        if item['midPrice'] != None:
            midPriceArr.append(item['midPrice'])
        midPrice = getAv(midPriceArr)
        highPriceArr = [] 
        if item['highPrice'] != None:
            highPriceArr.append(item['highPrice'])
        highPrice = getAv(highPriceArr)
        marketPriceArr = [] 
        if item['marketPrice'] != None:
            marketPriceArr.append(item['marketPrice'])
        marketPrice = getAv(marketPriceArr)
    ##Add pricing info to infoList and return it
    infoList.append(lowPrice)
    infoList.append(midPrice)
    infoList.append(highPrice)
    infoList.append(marketPrice)
    print(infoList)
    return json.dumps(infoList)

def getAv(arr):
    count = 0
    total = 0
    average = 0
    for item in arr:
        count += 1
        total += item
        average = total/count
    return average


