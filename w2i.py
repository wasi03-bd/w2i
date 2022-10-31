from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

def h2():
    return 'Sreing 2'

@app.route('/w2m/word=<string:quarry>', methods=['GET', 'POST','OPTIONS'])

def req(quarry):
    quarry = quarry.lower()
    quarry = quarry.replace(" ", "%20")
    ##----Generating Token-----
    urlft = 'https://api.fortress-ww-prd.lightricks.com/v2/auth/refreshToken?app=com.lightricks.Enlight-Editor&cvc=1&plt=a&pltv=33&env=production'

    headersft = {
        "content-type": "application/json", 
    }

    dataft = '{"ltid":"qaG276JdjpEiZ1OTmPjp","refreshToken":"qxQTdTRr-ezTtoY-5LibY-6FoDKI-ABCKUCTFktpcjPB4iK0oUycGfIuthJd6c1t"}'

    rft = requests.post(urlft, headers=headersft, data=dataft)
    token = rft.json()["token"]
    #----Generating TK end-------


    #------Generating Inage----
    urlfai = f'https://txt2img.res.lightricks.com/txt2img/v1/api/generate?prompt={quarry}&high_quality=true&is_subscriber=true'

    headersfai = {
        'x-lightricks-auth-token': f'{token}'
    }
    

    responsefai = requests.post(urlfai, headers=headersfai)
    rfai = responsefai.json()["result_url"]
    link = rfai
    # link.headers['Access-Control-Allow-Origin'] = '*'
    lwj  = {
        "image" : link
    }    #link with json
    # return jsonify(lwj)

    # return(link)
    res = make_response({"image": link}, 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


    
    


if __name__ == "__main__":
    app.run()
