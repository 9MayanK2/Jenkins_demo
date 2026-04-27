import flask from Flask

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "HOME directory"


@app.route("/version",methods=['GET'])
def version():
    return "Version Directory"


@app.route("/health",methods=['GET'])
def health():
    return "Health Directory"

app.run(host='0.0.0.0', port=5500)