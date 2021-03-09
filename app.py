from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello World! build is done???<br>이미지 변화 테스트중입니다<br> 테스트34 <br> 지금 커밋상황 확인?<br> 커밋되면 빌드치나?' 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80)
