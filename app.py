from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://noobmaster69:a1e2i3o4u5@cluster0.pd5jd.gcp.mongodb.net/fooddb?retryWrites=true&w=majority'
}

initialize_db(app)

# @app.route('/movies')
# def hello():
#     return jsonify(movies)

@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200  

app.run()