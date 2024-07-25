import streamlit as st

st.title("Jailxerox")
st.write( "Transforming digital into tangible with every print."
)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jailxerox - Your Trusted Xerox Shop</title>
    <link rel="stylesheet" href="{% static 'xerox/styles.css' %}">
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
