from flask import Flask, render_template

app = Flask(__name__)

@app.route("/words/<string:word>")
def words(word):
    dict = {"apple":"사과", "banana":"바나나", "pineapple":"파인애플","Lime":"라임","coconuts":"코코넛" }
    # if word in dict:
    #     mean = dict[word]
    # else:
    #     return render_template("word.html",word=word ,mean="은 나만의 단어장에 없는 단어입니다.")
    
    # return render_template("word.html", word=word, mean=mean)
    
    result = dict.get(word)
    if result:
        result = f"{word} : {result}"
    else:
        result = f"{word}은(는) 단어장에 없는 단어"
    
    return result
    
@app.route("/git")
def git():
    return render_template("git.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)