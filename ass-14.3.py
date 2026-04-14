# Lab 14: Web Design Applications Using AI Assistance
# This file generates complete web applications for all tasks

# Task 1: Personal Portfolio Website
portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
            scroll-behavior: smooth;
        }
        
        nav a:hover {
            opacity: 0.8;
        }
        
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 6rem 2rem;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        section {
            padding: 3rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .project-card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        }
        
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
        }
        
        @media (max-width: 768px) {
            nav {
                flex-direction: column;
                gap: 1rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .projects {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    
    <section id="home" class="hero">
        <h1>Welcome to My Portfolio</h1>
        <p>Full Stack Developer | AI Enthusiast</p>
    </section>
    
    <section id="about">
        <h2>About Me</h2>
        <p>I am a passionate developer with expertise in web design and AI applications.</p>
    </section>
    
    <section id="projects">
        <h2>My Projects</h2>
        <div class="projects">
            <div class="project-card">
                <h3>Project 1</h3>
                <p>Description of project 1</p>
            </div>
            <div class="project-card">
                <h3>Project 2</h3>
                <p>Description of project 2</p>
            </div>
            <div class="project-card">
                <h3>Project 3</h3>
                <p>Description of project 3</p>
            </div>
        </div>
    </section>
    
    <section id="contact">
        <h2>Contact</h2>
        <p>Email: your.email@example.com</p>
    </section>
    
    <footer>
        <p>&copy; 2024 My Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Task 3: Event Registration Form
registration_form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Registration Form</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        
        .form-container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            padding: 3rem;
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 2rem;
            color: #333;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
            font-weight: 500;
        }
        
        input, select {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        input:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .error {
            color: #e74c3c;
            font-size: 0.875rem;
            display: none;
            margin-top: 0.25rem;
        }
        
        .error.show {
            display: block;
        }
        
        button {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            font-weight: bold;
            transition: opacity 0.3s;
        }
        
        button:hover {
            opacity: 0.9;
        }
        
        .success-message {
            display: none;
            background: #2ecc71;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        
        .success-message.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Event Registration</h1>
        <div class="success-message" id="successMsg">Form submitted successfully!</div>
        
        <form id="registrationForm">
            <div class="form-group">
                <label for="name">Full Name *</label>
                <input type="text" id="name" name="name" required>
                <div class="error" id="nameError">Name is required</div>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email" required>
                <div class="error" id="emailError">Please enter a valid email</div>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number *</label>
                <input type="tel" id="phone" name="phone" required>
                <div class="error" id="phoneError">Phone number must be 10 digits</div>
            </div>
            
            <div class="form-group">
                <label for="department">Department *</label>
                <select id="department" name="department" required>
                    <option value="">Select Department</option>
                    <option value="CSE">Computer Science</option>
                    <option value="ECE">Electronics</option>
                    <option value="ME">Mechanical</option>
                    <option value="CE">Civil</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="event">Event Selection *</label>
                <select id="event" name="event" required>
                    <option value="">Select Event</option>
                    <option value="coding">Coding Competition</option>
                    <option value="hackathon">Hackathon</option>
                    <option value="workshop">Workshop</option>
                    <option value="seminar">Seminar</option>
                </select>
            </div>
            
            <button type="submit">Register Now</button>
        </form>
    </div>
    
    <script>
        const form = document.getElementById('registrationForm');
        
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (validateForm()) {
                document.getElementById('successMsg').classList.add('show');
                form.reset();
                setTimeout(() => {
                    document.getElementById('successMsg').classList.remove('show');
                }, 3000);
            }
        });
        
        function validateForm() {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            
            let isValid = true;
            
            if (name === '') {
                showError('nameError');
                isValid = false;
            } else {
                hideError('nameError');
            }
            
            const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
            if (!emailRegex.test(email)) {
                showError('emailError');
                isValid = false;
            } else {
                hideError('emailError');
            }
            
            if (phone.length !== 10 || isNaN(phone)) {
                showError('phoneError');
                isValid = false;
            } else {
                hideError('phoneError');
            }
            
            return isValid;
        }
        
        function showError(errorId) {
            document.getElementById(errorId).classList.add('show');
        }
        
        function hideError(errorId) {
            document.getElementById(errorId).classList.remove('show');
        }
    </script>
</body>
</html>
"""

# Task 5: Responsive Web Page Layout
responsive_layout_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Web Layout</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        header h1 {
            font-size: 1.5rem;
        }
        
        nav {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }
        
        nav a:hover {
            opacity: 0.8;
        }
        
        main {
            display: grid;
            grid-template-columns: 1fr 3fr 1fr;
            gap: 2rem;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .sidebar {
            background: #f4f4f4;
            padding: 1.5rem;
            border-radius: 8px;
        }
        
        .content {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .card {
            background: white;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
        }
        
        @media (max-width: 1024px) {
            main {
                grid-template-columns: 1fr;
            }
        }
        
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                gap: 1rem;
            }
            
            nav {
                flex-direction: column;
                gap: 0.5rem;
            }
            
            main {
                padding: 1rem;
            }
            
            .content, .sidebar, .card {
                padding: 1rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Responsive Web Layout</h1>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    
    <main>
        <aside class="sidebar">
            <div class="card">
                <h3>Sidebar</h3>
                <p>This is the sidebar content area for secondary information.</p>
            </div>
        </aside>
        
        <section class="content">
            <h2>Main Content Area</h2>
            <p>Welcome to our responsive web page. This layout adapts beautifully to different screen sizes using CSS Grid and Flexbox.</p>
            <p>The layout features:</p>
            <ul>
                <li>Header with navigation</li>
                <li>Three-column layout on desktop</li>
                <li>Single column on mobile</li>
                <li>Footer with information</li>
            </ul>
            
            <div class="card">
                <h3>Feature 1</h3>
                <p>Description of feature 1 goes here.</p>
            </div>
            
            <div class="card">
                <h3>Feature 2</h3>
                <p>Description of feature 2 goes here.</p>
            </div>
        </section>
        
        <aside class="sidebar">
            <div class="card">
                <h3>Right Sidebar</h3>
                <p>Additional content and widgets can be placed here.</p>
            </div>
        </aside>
    </main>
    
    <footer>
        <p>&copy; 2024 Responsive Web Layout. All rights reserved. | Contact: info@example.com</p>
    </footer>
</body>
</html>
"""

# Export HTML content to files
if __name__ == "__main__":
    with open('portfolio.html', 'w') as f:
        f.write(portfolio_html)
    
    with open('registration_form.html', 'w') as f:
        f.write(registration_form_html)
    
    with open('responsive_layout.html', 'w') as f:
        f.write(responsive_layout_html)
    
    print("All HTML files generated successfully!")
    print("Generated files:")
    print("1. portfolio.html - Personal Portfolio Website")
    print("2. registration_form.html - Event Registration Form")
    print("3. responsive_layout.html - Responsive Web Page Layout")