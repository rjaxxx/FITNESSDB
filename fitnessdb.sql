--
-- File generated with SQLiteStudio v3.4.4 on Mon Mar 17 11:30:11 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Exercises
CREATE TABLE IF NOT EXISTS Exercises (exercise_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, exercise_name TEXT NOT NULL, muscle_id INTEGER REFERENCES Muscles (muscle_id), FOREIGN KEY (muscle_id) REFERENCES Muscles (muscle_id));
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (1, 'Face Pulls', 13);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (2, 'Shrugs', 4);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (3, 'Leg Raise', 1);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (4, 'Russian Twist', 1);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (5, 'Crunch', 1);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (6, 'Plank', 1);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (7, 'Calf Raise', 3);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (8, 'Hip Thrust', 7);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (9, 'Glute Bridge', 7);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (10, 'Deadlift', 5);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (11, 'Romanian Deadlift', 6);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (12, 'Leg Curl', 8);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (13, 'Lunges', 9);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (14, 'Leg Press', 9);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (15, 'Squat', 9);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (16, 'Bent Over Row', 5);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (17, 'Pull Up', 5);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (18, 'Lat Pulldown', 5);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (19, 'Chin Up', 10);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (20, 'Bicep Curl', 10);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (21, 'Tricep Pushdown', 11);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (22, 'Tricep Dips', 11);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (23, 'Incline Bench Press', 12);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (24, 'Push Up', 12);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (25, 'Bench Press', 12);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (26, 'Front Raise', 13);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (27, 'Shoulder Press', 13);
INSERT INTO Exercises (exercise_id, exercise_name, muscle_id) VALUES (28, 'Lateral Raise', 13);

-- Table: Muscles
CREATE TABLE IF NOT EXISTS Muscles (
    muscle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    muscle_name TEXT NOT NULL
);
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (1, 'Abs');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (2, 'Forearms');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (3, 'Calves');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (4, 'Trapezius');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (5, 'Lats');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (6, 'Back');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (7, 'Glutes');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (8, 'Hamstrings');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (9, 'Quadriceps');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (10, 'Biceps');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (11, 'Triceps');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (12, 'Chest');
INSERT INTO Muscles (muscle_id, muscle_name) VALUES (13, 'Shoulders');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
