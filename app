from flask import Flask, render_template, request, url_for, redirect, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "GG"

@app.route('/api/sales')
def salesGetAll():
    pass



@app.route('/post/<post_id>',methods = ['POST', 'GET'])
def lala(post_id):
    if request.method == 'GET':
        return f'Id del post {post_id}'
    else:
        return "Este metodo no es GET lala "

# @app.route("/lala/<user>")
# def lala(user):
#     return "lala " + user 

@app.route("/lele", methods = ['POST', 'GET'])
def lele():
    # abort(404)
    # return redirect(url_for('lala',post_id=666))
    # print(url_for('lala',post_id=666))
    # print(request.form)
    # print(request.form['llave1'])
    # return "lele"  
    # return render_template('index.html')
     return {
         "user": "equisd" 
     }
