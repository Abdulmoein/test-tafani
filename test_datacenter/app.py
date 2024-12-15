from flask import Flask, render_template, request



app = Flask(__name__)

names = []


@app.route("/", methods=["GET", "POST"])
def home():
    
    title = "الصفحة الرئيسية"
    
    if request.method == "POST":
        
        name = request.form.get("name", "not found")
        
        names.append(name)
        
        
        
        
    
    
    
    return render_template("home.html", title=title, names=names)
    
    
    

if __name__ == "__main__":
    
    app.run(debug=True)

