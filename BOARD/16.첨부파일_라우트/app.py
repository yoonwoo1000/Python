from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
# 시간 밀리초 1*1000 / 1*60*1000
# 바이트 2^10  1024 
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/upload',methods=['POST'])
def file_form():
    text = request.form.get('text')
    print(text)
    #file1 = request.files['attach1']
    #file1 = request.files.get('attach1')
    # 설정된 업로드 폴더 경로 + 파일이름
    #path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    #print(path)
    # 풀 경로로 파일객체의 내용을 저장해주세요
    #file1.save(path)
    #file2 = request.files.get('attach2')

    # form 데이터에 'files'이름으로 데이터가 있는지 확인
    if 'files' in request.files :
        # 파일객체 리스트를 가져옴
        files = request.files.getlist('files')
        # 리스트가 있으면
        if files :
            # 반복문으로 파일 객체를 꺼내서
            for file in files :
                print(file.filename)
                # 실제로는 파일명을 변경후 저장합니다
                path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(path)
    return 'file_form'

@app.route('/result')
def result():
    return render_template('result.html')

from flask import send_from_directory
# 동적 라우트
@app.route('/upload/<string:filename>')
def upload_route(filename):
    '''
    # 로그인 유저에게만 서비스
    if 'uIDX' not in session :
        return redirect('/')
    # 권한 체크 후 서비스
    if session.get('level') != 'manager' :
        return redirect('/')    '''
    print(f'요청한 파일 이름 : {filename}')
    if not filename or len(filename) < 1 :
        return '잘못된 요청입니다'
    # filename으로 upload 폴더에 파일이 있는지 확인
    full_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    # 전체 경로를 만들어서 확인 : 폴더+파일이름
    if not os.path.exists(full_path) :
        # upload 폴더에 해당 파일이 없음
        return 'FILE Not Found', 404
    else :
        # 파일이 있음 -> 파일을 가져와서, 반환
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],    # 경로
            filename                        # 파일명
        )

if __name__ == '__main__' :
    app.run(debug=True)