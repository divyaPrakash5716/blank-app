 
import streamlit as st

# Set the title of the app
st.title("Jailxerox")
st.write("Transforming digital into tangible with every print.")

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jailxerox - Your Trusted Xerox Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f4f4f4;
        }
        header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1em 0;
        }
        header h1 {
            margin: 0;
            font-size: 2.5em;
        }
        header p {
            margin: 0;
            font-size: 1.2em;
        }
        main {
            padding: 20px;
        }
        section {
            margin: 20px 0;
        }
        h2 {
            font-size: 1.8em;
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            background-color: #ddd;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
        }
        form {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #4CAF50;
            color: white;
            position: absolute;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Jailxerox</h1>
        <p>Your Trusted Xerox Shop</p>
    </header>
    <main>
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Xerox</li>
                <li>Printing</li>
                <li>Scanning</li>
                <li>Binding</li>
                <li>Lamination</li>
            </ul>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
            <form>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Jailxerox. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Display HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
