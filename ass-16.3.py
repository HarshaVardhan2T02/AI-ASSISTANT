"""
Lab 16 – Database Design and Queries: Schema Design and SQL Generation
Complete solution for Hospital, E-commerce, Library, and University databases
"""

# ============================================================================
# TASK 1 - HOSPITAL MANAGEMENT DATABASE
# ============================================================================

hospital_schema = """
-- Doctors Table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    phone VARCHAR(10) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients Table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    phone VARCHAR(10) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    address VARCHAR(255),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Appointments Table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_id INT NOT NULL,
    patient_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    CONSTRAINT valid_appointment_date CHECK (appointment_date > NOW())
);

CREATE INDEX idx_doctor_appointments ON Appointments(doctor_id);
CREATE INDEX idx_patient_appointments ON Appointments(patient_id);
"""

# Hospital Queries
hospital_queries = """
-- Query 1: List all appointments for a specific doctor
SELECT 
    a.appointment_id,
    d.name AS doctor_name,
    p.name AS patient_name,
    a.appointment_date,
    a.status
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
JOIN Patients p ON a.patient_id = p.patient_id
WHERE d.doctor_id = 1
ORDER BY a.appointment_date;

-- Query 2: Retrieve patient history by patient ID
SELECT 
    a.appointment_id,
    d.name AS doctor_name,
    d.specialization,
    a.appointment_date,
    a.status,
    a.notes
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 5
ORDER BY a.appointment_date DESC;

-- Query 3: Count total patients treated by each doctor
SELECT 
    d.doctor_id,
    d.name,
    d.specialization,
    COUNT(DISTINCT a.patient_id) AS total_patients,
    COUNT(a.appointment_id) AS total_appointments
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
    AND a.status = 'completed'
GROUP BY d.doctor_id, d.name, d.specialization
HAVING total_appointments > 0
ORDER BY total_patients DESC;
"""

# ============================================================================
# TASK 2 - E-COMMERCE DATABASE
# ============================================================================

ecommerce_schema = """
-- Users Table
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(10),
    address VARCHAR(255),
    city VARCHAR(50),
    country VARCHAR(50),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    category VARCHAR(50),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_price CHECK (price > 0),
    CONSTRAINT valid_stock CHECK (stock_quantity >= 0)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(12, 2) NOT NULL,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    CONSTRAINT valid_total CHECK (total_amount >= 0)
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CONSTRAINT valid_quantity CHECK (quantity > 0)
);

CREATE INDEX idx_user_orders ON Orders(user_id);
CREATE INDEX idx_order_products ON OrderDetails(order_id);
CREATE INDEX idx_product_orders ON OrderDetails(product_id);
"""

# E-commerce Queries
ecommerce_queries = """
-- Query 1: Retrieve all orders by a user
SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status,
    COUNT(od.order_detail_id) AS item_count
FROM Orders o
LEFT JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.user_id = 10
GROUP BY o.order_id
ORDER BY o.order_date DESC;

-- Query 2: Find the most purchased product
SELECT 
    p.product_id,
    p.name,
    p.category,
    p.price,
    SUM(od.quantity) AS total_quantity_sold,
    SUM(od.subtotal) AS total_revenue
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
JOIN Orders o ON od.order_id = o.order_id
WHERE o.status = 'delivered'
GROUP BY p.product_id, p.name, p.category, p.price
ORDER BY total_quantity_sold DESC
LIMIT 10;

-- Query 3: Calculate total revenue in a given month
SELECT 
    YEAR(o.order_date) AS year,
    MONTH(o.order_date) AS month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.user_id) AS unique_customers,
    SUM(o.total_amount) AS total_revenue
FROM Orders o
WHERE o.status IN ('delivered', 'shipped')
    AND YEAR(o.order_date) = 2024
    AND MONTH(o.order_date) = 1
GROUP BY year, month;

-- Query 4: Find products with low stock
SELECT 
    p.product_id,
    p.name,
    p.stock_quantity,
    p.price,
    COUNT(od.order_detail_id) AS monthly_demand
FROM Products p
LEFT JOIN OrderDetails od ON p.product_id = od.product_id
WHERE p.stock_quantity < 10
GROUP BY p.product_id
ORDER BY p.stock_quantity ASC;

-- Optimization: Instead of subqueries, use JOIN for better performance
-- Original (slower): SELECT * FROM Products WHERE product_id IN (...)
-- Optimized: JOIN instead of subquery for category filtering
SELECT p.*
FROM Products p
WHERE p.stock_quantity < 20
ORDER BY p.stock_quantity ASC;
"""

# ============================================================================
# TASK 3 - LIBRARY DATABASE
# ============================================================================

library_schema = """
-- Books Table
CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    publication_date DATE,
    category VARCHAR(50),
    total_copies INT NOT NULL DEFAULT 1,
    available_copies INT NOT NULL,
    CONSTRAINT valid_copies CHECK (available_copies >= 0 AND available_copies <= total_copies)
);

-- Members Table
CREATE TABLE Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10),
    address VARCHAR(255),
    membership_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'suspended') DEFAULT 'active'
);

-- Loans Table
CREATE TABLE Loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURDATE(),
    due_date DATE NOT NULL,
    return_date DATE,
    status ENUM('active', 'returned', 'overdue') DEFAULT 'active',
    fine_amount DECIMAL(8, 2) DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    CONSTRAINT valid_dates CHECK (due_date > loan_date)
);

-- Create indexes for faster queries
CREATE INDEX idx_book_loans ON Loans(book_id);
CREATE INDEX idx_member_loans ON Loans(member_id);
CREATE INDEX idx_loan_status ON Loans(status);
CREATE INDEX idx_due_date ON Loans(due_date);
"""

# Library Queries
library_queries = """
-- Query 1: Retrieve all books currently issued
SELECT 
    l.loan_id,
    b.book_id,
    b.title,
    b.author,
    b.isbn,
    m.name AS member_name,
    m.email,
    l.loan_date,
    l.due_date,
    DATEDIFF(CURDATE(), l.loan_date) AS days_issued
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.status = 'active'
ORDER BY l.due_date ASC;

-- Query 2: Find overdue books (loan date > 30 days)
SELECT 
    l.loan_id,
    b.title,
    b.author,
    m.name AS member_name,
    m.email,
    m.phone,
    l.loan_date,
    l.due_date,
    DATEDIFF(CURDATE(), l.due_date) AS days_overdue,
    CASE
        WHEN DATEDIFF(CURDATE(), l.due_date) > 30 THEN DATEDIFF(CURDATE(), l.due_date) * 5
        WHEN DATEDIFF(CURDATE(), l.due_date) > 0 THEN DATEDIFF(CURDATE(), l.due_date) * 2
        ELSE 0
    END AS calculated_fine
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.status = 'active' AND DATEDIFF(CURDATE(), l.due_date) > 0
ORDER BY days_overdue DESC;

-- Query 3: Count number of books loaned by each member
SELECT 
    m.member_id,
    m.name,
    m.email,
    m.status,
    COUNT(CASE WHEN l.status = 'active' THEN 1 END) AS currently_borrowed,
    COUNT(CASE WHEN l.status = 'returned' THEN 1 END) AS returned_books,
    COUNT(l.loan_id) AS total_loans
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.name, m.email, m.status
HAVING total_loans > 0
ORDER BY currently_borrowed DESC;

-- Query 4: Popular books (most borrowed)
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.category,
    COUNT(l.loan_id) AS total_loans,
    COUNT(DISTINCT l.member_id) AS unique_members,
    AVG(DATEDIFF(l.return_date, l.loan_date)) AS avg_loan_days
FROM Books b
LEFT JOIN Loans l ON b.book_id = l.book_id
GROUP BY b.book_id
ORDER BY total_loans DESC
LIMIT 20;
"""

# ============================================================================
# TASK 4 - QUERY OPTIMIZATION
# ============================================================================

query_optimization = """
-- OPTIMIZATION EXAMPLE 1: Subquery vs JOIN
-- Original Query (SLOWER - uses subquery)
SELECT * 
FROM Books 
WHERE author_id IN (SELECT author_id FROM Authors WHERE country='UK');

-- Optimized Query (FASTER - uses JOIN)
SELECT b.*
FROM Books b
JOIN Authors a ON b.author_id = a.author_id
WHERE a.country = 'UK';

-- OPTIMIZATION EXAMPLE 2: Multiple subqueries
-- Original (SLOWER)
SELECT * FROM Products 
WHERE category_id IN (SELECT category_id FROM Categories WHERE active = 1)
    AND product_id IN (SELECT product_id FROM OrderDetails GROUP BY product_id HAVING COUNT(*) > 5);

-- Optimized (FASTER)
SELECT DISTINCT p.*
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
JOIN OrderDetails od ON p.product_id = od.product_id
WHERE c.active = 1
GROUP BY p.product_id
HAVING COUNT(od.order_detail_id) > 5;

-- OPTIMIZATION EXAMPLE 3: SELECT * vs Specific columns
-- Original (SLOWER - unnecessary columns)
SELECT * FROM Users WHERE user_id = 1;

-- Optimized (FASTER - only needed columns)
SELECT user_id, name, email, phone FROM Users WHERE user_id = 1;

-- OPTIMIZATION EXAMPLE 4: Use EXIST instead of IN
-- Original
SELECT p.name FROM Products p WHERE p.product_id IN 
    (SELECT product_id FROM Orders WHERE order_date > '2024-01-01');

-- Optimized
SELECT p.name FROM Products p 
WHERE EXISTS (SELECT 1 FROM Orders o 
              WHERE o.product_id = p.product_id AND o.order_date > '2024-01-01');
"""

# ============================================================================
# TASK 5 - UNIVERSITY COURSE REGISTRATION
# ============================================================================

university_schema = """
-- Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10),
    dob DATE,
    enrollment_date DATE NOT NULL DEFAULT CURDATE(),
    status ENUM('active', 'inactive', 'graduated', 'suspended') DEFAULT 'active'
);

-- Faculty Table
CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10),
    department VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'on_leave') DEFAULT 'active'
);

-- Courses Table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_code VARCHAR(10) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT NOT NULL,
    faculty_id INT NOT NULL,
    semester VARCHAR(20),
    max_capacity INT NOT NULL DEFAULT 50,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id),
    CONSTRAINT valid_credits CHECK (credits > 0),
    CONSTRAINT valid_capacity CHECK (max_capacity > 0)
);

-- Registrations Table
CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    grade CHAR(2),
    status ENUM('enrolled', 'completed', 'dropped', 'auditing') DEFAULT 'enrolled',
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    UNIQUE KEY unique_registration (student_id, course_id),
    CONSTRAINT valid_grade CHECK (grade IN ('A', 'B', 'C', 'D', 'F', 'P', 'NP', NULL))
);

CREATE INDEX idx_student_courses ON Registrations(student_id);
CREATE INDEX idx_course_registrations ON Registrations(course_id);
CREATE INDEX idx_faculty_courses ON Courses(faculty_id);
"""

# University Queries
university_queries = """
-- Query 1: List all students enrolled in a specific course
SELECT 
    r.registration_id,
    s.student_id,
    s.roll_number,
    s.first_name,
    s.last_name,
    s.email,
    s.status,
    r.registration_date,
    r.status AS enrollment_status
FROM Registrations r
JOIN Students s ON r.student_id = s.student_id
JOIN Courses c ON r.course_id = c.course_id
WHERE c.course_code = 'CS101'
    AND r.status IN ('enrolled', 'completed')
ORDER BY s.roll_number;

-- Query 2: Find faculty members teaching more than 2 courses
SELECT 
    f.faculty_id,
    f.name,
    f.email,
    f.department,
    COUNT(c.course_id) AS total_courses,
    COUNT(DISTINCT r.student_id) AS total_students,
    GROUP_CONCAT(c.course_code SEPARATOR ', ') AS courses_taught
FROM Faculty f
JOIN Courses c ON f.faculty_id = c.faculty_id
LEFT JOIN Registrations r ON c.course_id = r.course_id
    AND r.status IN ('enrolled', 'completed')
GROUP BY f.faculty_id, f.name, f.email, f.department
HAVING total_courses > 2
ORDER BY total_courses DESC;

-- Query 3: Retrieve courses with the highest number of registrations
SELECT 
    c.course_id,
    c.course_code,
    c.course_name,
    c.credits,
    f.name AS faculty_name,
    c.max_capacity,
    COUNT(r.registration_id) AS enrolled_students,
    ROUND((COUNT(r.registration_id) / c.max_capacity * 100), 2) AS occupancy_percentage,
    COUNT(DISTINCT CASE WHEN r.status = 'enrolled' THEN r.student_id END) AS currently_enrolled
FROM Courses c
JOIN Faculty f ON c.faculty_id = f.faculty_id
LEFT JOIN Registrations r ON c.course_id = r.course_id
GROUP BY c.course_id, c.course_code, c.course_name, c.credits, 
         f.name, c.max_capacity
ORDER BY enrolled_students DESC;

-- Query 4: Student academic summary
SELECT 
    s.student_id,
    s.roll_number,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    COUNT(DISTINCT r.course_id) AS courses_enrolled,
    COUNT(CASE WHEN r.status = 'completed' THEN 1 END) AS completed_courses,
    SUM(CASE WHEN r.status = 'completed' THEN c.credits ELSE 0 END) AS total_credits_earned,
    ROUND(AVG(CASE WHEN r.grade IN ('A', 'B', 'C', 'D') THEN 
        CASE r.grade WHEN 'A' THEN 4.0 WHEN 'B' THEN 3.0 WHEN 'C' THEN 2.0 ELSE 1.0 END 
    END), 2) AS gpa
FROM Students s
LEFT JOIN Registrations r ON s.student_id = r.student_id
LEFT JOIN Courses c ON r.course_id = c.course_id
WHERE s.status = 'active'
GROUP BY s.student_id, s.roll_number, student_name
ORDER BY gpa DESC;

-- Query 5: Find courses that are overfilled
SELECT 
    c.course_id,
    c.course_code,
    c.course_name,
    c.max_capacity,
    COUNT(r.registration_id) AS current_registrations,
    (COUNT(r.registration_id) - c.max_capacity) AS overflow
FROM Courses c
LEFT JOIN Registrations r ON c.course_id = r.course_id
    AND r.status = 'enrolled'
GROUP BY c.course_id, c.course_code, c.course_name, c.max_capacity
HAVING current_registrations > c.max_capacity
ORDER BY overflow DESC;
"""

# ============================================================================
# SAMPLE DATA INSERTION
# ============================================================================

sample_data = """
-- Hospital Sample Data
INSERT INTO Doctors (name, specialization, phone, email) VALUES
('Dr. Rajesh Kumar', 'Cardiology', '9876543210', 'rajesh.k@hospital.com'),
('Dr. Priya Singh', 'Neurology', '9876543211', 'priya.s@hospital.com'),
('Dr. Amit Patel', 'Orthopedics', '9876543212', 'amit.p@hospital.com');

INSERT INTO Patients (name, dob, phone, email, address) VALUES
('John Doe', '1985-05-15', '8765432109', 'john@email.com', 'Mumbai, India'),
('Jane Smith', '1990-03-22', '8765432108', 'jane@email.com', 'Delhi, India');

-- E-commerce Sample Data
INSERT INTO Users (username, email, first_name, last_name) VALUES
('john_doe', 'john@shop.com', 'John', 'Doe'),
('jane_smith', 'jane@shop.com', 'Jane', 'Smith');

INSERT INTO Products (name, price, stock_quantity, category) VALUES
('Laptop', 75000.00, 10, 'Electronics'),
('Mouse', 500.00, 50, 'Electronics'),
('Keyboard', 2000.00, 30, 'Accessories');

-- Library Sample Data
INSERT INTO Books (title, author, isbn, category, total_copies, available_copies) VALUES
('Python Programming', 'Guido van Rossum', '9780134685991', 'Programming', 5, 3),
('Database Design', 'C.J. Date', '9780134085142', 'Database', 3, 2);

INSERT INTO Members (name, email, phone, membership_date) VALUES
('Rahul Sharma', 'rahul@email.com', '7654321098', '2023-01-15'),
('Neha Gupta', 'neha@email.com', '7654321097', '2023-02-20');

-- University Sample Data
INSERT INTO Faculty (name, email, department, specialization) VALUES
('Prof. Dr. Venugopal', 'venugopal@university.edu', 'Computer Science', 'Artificial Intelligence'),
('Prof. Dr. Sharma', 'sharma@university.edu', 'Computer Science', 'Database Systems'),
('Prof. Dr. Patel', 'patel@university.edu', 'Computer Science', 'Web Development');

INSERT INTO Students (roll_number, first_name, last_name, email) VALUES
('CS2021001', 'Aarav', 'Singh', 'aarav.singh@university.edu'),
('CS2021002', 'Bhavna', 'Gupta', 'bhavna.gupta@university.edu');

INSERT INTO Courses (course_code, course_name, credits, faculty_id, max_capacity) VALUES
('CS101', 'Introduction to Programming', 4, 1, 50),
('CS201', 'Database Management Systems', 4, 2, 40),
('CS301', 'Web Development', 3, 3, 35);
"""

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("LAB 16: DATABASE DESIGN AND QUERIES")
    print("=" * 80)
    
    print("\n### TASK 1: HOSPITAL MANAGEMENT DATABASE ###\n")
    print("Schema:")
    print(hospital_schema)
    print("\nQueries:")
    print(hospital_queries)
    
    print("\n\n### TASK 2: E-COMMERCE DATABASE ###\n")
    print("Schema:")
    print(ecommerce_schema)
    print("\nQueries:")
    print(ecommerce_queries)
    
    print("\n\n### TASK 3: LIBRARY DATABASE ###\n")
    print("Schema:")
    print(library_schema)
    print("\nQueries:")
    print(library_queries)
    
    print("\n\n### TASK 4: QUERY OPTIMIZATION ###\n")
    print(query_optimization)
    
    print("\n\n### TASK 5: UNIVERSITY COURSE REGISTRATION ###\n")
    print("Schema:")
    print(university_schema)
    print("\nQueries:")
    print(university_queries)
    
    print("\n\n### SAMPLE DATA ###\n")
    print(sample_data)