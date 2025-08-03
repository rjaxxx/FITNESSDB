from flask import Flask, render_template, request
import random 
import sqlite3


app = Flask(__name__)


# Home page to display previews
@app.route('/')
def home():
    conn = sqlite3.connect('fitness.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT image_url FROM Images")
    image_rows = cur.fetchall()
    conn.close()
    if not image_rows:
        return "No images available."
    random_images = random.sample(image_rows, 10)
    image_urls = [image['image_url'] for image in random_images]
    return render_template('home.html', title="Home", images=image_urls)


#
@app.route('/all_exercises')
def all_exercises():
    conn = sqlite3.connect('fitness.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""
        SELECT e.exercise_id, e.exercise_name, m.muscle_name, i.image_url
        FROM Exercises e
        INNER JOIN Muscles m ON e.muscle_id = m.muscle_id
        LEFT JOIN Images i ON i.image_id = e.exercise_id
    """)
    exercises = cur.fetchall()
    conn.close()
    return render_template('all_exercises.html', title='All Exercises', exercises=exercises)


@app.route("/exercise/<int:id>")
def exercise(id):
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    cur.execute("""
        SELECT e.exercise_id, e.exercise_name, m.muscle_name, i.image_url
        FROM Exercises e
        INNER JOIN Muscles m ON e.muscle_id = m.muscle_id
        LEFT JOIN Images i ON i.image_id = e.exercise_id
        WHERE e.exercise_id = ?
    """, (id,))
    exercise = cur.fetchone()
    title = 'Exercises - ' + str(exercise[1])
    conn.close()
    return render_template('exercise.html', title=title, exercise=exercise)


@app.route('/all_muscles')
def all_muscles():
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Muscles")
    muscles = cur.fetchall()
    conn.close()
    return render_template('all_muscles.html', title='Muscles', muscles=muscles)


#
@app.route("/muscle/<int:id>")
def muscle_exercises(id):
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    cur.execute("SELECT muscle_name FROM Muscles WHERE muscle_id = ?", (id,))
    muscle = cur.fetchone()
    cur.execute("SELECT exercise_id, exercise_name FROM Exercises WHERE muscle_id = ?", (id,))
    exercises = cur.fetchall()
    title = 'Muscles - ' + str(muscle[0])
    conn.close()
    return render_template('muscle_exercises.html', title=title, muscle=muscle, exercises=exercises)


# This is a function to search the database for infromation similar to entered string
@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    cur.execute("SELECT muscle_id, muscle_name FROM Muscles WHERE muscle_name LIKE ?", ('%' + query + '%',))
    muscles = cur.fetchall()
    cur.execute("SELECT exercise_id, exercise_name FROM Exercises WHERE exercise_name LIKE ?", ('%' + query + '%',))
    exercises = cur.fetchall()
    conn.close()
    return render_template('search_results.html', title='Search Results', query=query, muscles=muscles, exercises=exercises)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
