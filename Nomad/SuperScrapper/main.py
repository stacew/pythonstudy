from flask import Flask, render_template, request, redirect, send_file
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    os.path.dirname(__file__))))  # 상위 폴더를 path로 등록하는 코드, 프로그램 종료되면 사라지는 방식.


app = Flask("Super Scrapper")
dataModel = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()

        word = word.lower()
        existingJobs = dataModel.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            # 자동 포맷팅 때문에... 자꾸 제일 상단으로.. 가서 일단 여기 추가.
            from JobScrapper.indeedW import get_jobs
            jobs = get_jobs(word)
            dataModel[word] = jobs

        return render_template("report.html",
                               renderingParameter="My Rendering Parameter",
                               searchingBy=word,
                               resultNumber=len(jobs),
                               jobs=jobs)
    except:
        return redirect("/")


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()

        word = word.lower()
        jobs = dataModel.get(word)
        if not jobs:
            raise Exception()

        from JobScrapper.save import save_to_file
        save_to_file(jobs)  # 파일을 계속 저장하기 때문에, 별로

        # 현재 폴더의 저장된 파일을 유저가 Download 할 수 있음.
        return send_file("jobs.csv", attachment_filename=f'export_jobs_{word}.csv')

    except:
        return redirect("/")

# 연습용
# @app.route("/")
# def home():
#     return "Hello! Welcome!"

# @app.route("/contact")
# def contact():
#     return "Contact me!"

# @app.route("/<username>")  # 인스타그램 같은
# def dynamicURL(username):
#     return f"Hello {username}, how are you doing"


app.run(host="127.0.0.1", port=3000)
