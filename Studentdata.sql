#create an student table with the following columns: id, name, age, grade,marks,year
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10),
    marks INT,
    year INT
);
#insert some data into the student table
INSERT INTO student (id, name, age, grade, marks, year) VALUES
(1, 'Alice', 20, 'A', 85, 2022),
(2, 'Bob', 21, 'B', 75, 2022),
(3, 'Charlie', 19, 'A', 90, 2022),
(4, 'David', 22, 'C', 65, 2022),
(5, 'Eve', 20, 'B', 80, 2022);
#select all students who scored above 80 marks
SELECT * FROM student WHERE marks > 80;
#select the names of students who are in grade A
SELECT name FROM student WHERE grade = 'A';
#select the average marks of students in each grade
SELECT grade, AVG(marks) AS average_marks FROM student GROUP BY grade;
#select the number of students in each year
SELECT year, COUNT(*) AS number_of_students FROM student GROUP BY year;
#update the grade of a student with id 2 to A
UPDATE student SET grade = 'A' WHERE id = 2;
#delete a student with id 4 from the table
DELETE FROM student WHERE id = 4;
#select all students to see the changes
SELECT * FROM student;
