from flask import Flask, render_template, request
import random
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    try:
        with sqlite3.connect('fitness.db') as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT image_url FROM Images ORDER BY RANDOM() LIMIT 10")
            image_rows = cur.fetchall()

        if not image_rows:
            return render_template('home.html', title="Home", images=[], message="No images available.")

        image_urls = [row['image_url'] for row in image_rows]
        return render_template('home.html', title="Home", images=image_urls)

    except sqlite3.Error as e:
        error_msg = f"Database error: {e}"
        return render_template('home.html', title="Home", images=[], message=error_msg)


# Display all exercises
@app.route('/all_exercises')
def all_exercises():
    # Connect to database
    conn = sqlite3.connect('fitness.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # Select exercise id and name, muscle name and image url
    cur.execute("""
        SELECT e.exercise_id, e.exercise_name, m.muscle_name, i.image_url
        FROM Exercises e
        INNER JOIN Muscles m ON e.muscle_id = m.muscle_id
        LEFT JOIN Images i ON i.image_id = e.exercise_id
    """)
    exercises = cur.fetchall()
    conn.close()
    return render_template('all_exercises.html', title='All Exercises', exercises=exercises)


# Display specific exercise information
@app.route("/exercise/<int:id>")
def exercise(id):
    # Connect to database
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    # Select exercise id and name, muscle name and specific image url
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


# Display all muscles
@app.route('/all_muscles')
def all_muscles():
    # Connect to database
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    # Select all muscle id and name
    cur.execute("SELECT * FROM Muscles")
    muscles = cur.fetchall()
    conn.close()
    return render_template('all_muscles.html', title='Muscles', muscles=muscles)


# Display specific muscle information
@app.route("/muscle/<int:id>")
def muscle_exercises(id):
    # Connect to database
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    # Select specific muscle name
    cur.execute("SELECT muscle_name FROM Muscles WHERE muscle_id = ?", (id,))
    muscle = cur.fetchone()
    # Select specific exercise id and names
    cur.execute("SELECT exercise_id, exercise_name FROM Exercises WHERE muscle_id = ?", (id,))
    exercises = cur.fetchall()
    title = 'Muscles - ' + str(muscle[0])
    conn.close()
    return render_template('muscle_exercises.html', title=title, muscle=muscle, exercises=exercises)


# This is a function to search the database for infromation similar to entered string
@app.route('/search')
def search():
    # Connect to database
    query = request.args.get('query', '').strip()
    conn = sqlite3.connect('fitness.db')
    cur = conn.cursor()
    # Select specific muscle id and name
    cur.execute("SELECT muscle_id, muscle_name FROM Muscles WHERE muscle_name LIKE ?", ('%' + query + '%',))
    muscles = cur.fetchall()
    # Select specific exercise id and name
    cur.execute("SELECT exercise_id, exercise_name FROM Exercises WHERE exercise_name LIKE ?", ('%' + query + '%',))
    exercises = cur.fetchall()
    conn.close()
    return render_template('search_results.html', title='Search Results', query=query, muscles=muscles, exercises=exercises)


# Run code on port:5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
