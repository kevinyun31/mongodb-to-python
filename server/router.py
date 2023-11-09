from flask import Flask, render_template
# python -m pip install flask

# 1. Flask 객체 생성
app = Flask(__name__)

# 2. 라우터 함수 만들기

# http1.1 => 요청 메서드 방식 4가지 방식
# GET(SELECT), POST(INSERT), DELETE(DELETE), PUT(UPDATE)

# Data를 응답


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Data를 응답


@app.route("/board/<id>")
def detail(id):
    return "board"+id


# 해당 파일이 직접 호출되었을 때
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
