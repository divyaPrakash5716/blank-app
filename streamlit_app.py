import streamlit as st

# Set the title of the app
st.set_page_config(page_title="Jailxerox", layout="wide")

# Add CSS styles for smoother navigation transitions and paper animation
st.markdown("""
<style>
    body {
        background-color: #333;
        color: white;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    .paper {
        position: bottom;
        top: 50%;
        right: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 300px;
        background-color: #fff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        /* Add other paper styling (e.g., lines, folds) */
        animation: floatPaper 3s infinite alternate;
    }
    @keyframes floatPaper {
        0% {
            transform: translate(-50%, -50%) rotate(0deg);
        }
        100% {
            transform: translate(-50%, -50%) rotate(5deg);
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Services", "Blog", "Contact Us"])

    if page == "Home":
        show_home()
    elif page == "Services":
        show_services()
    elif page == "Blog":
        show_blog()
    elif page == "Contact Us":
        show_contact_us()

def show_home():
    st.title("Jailxerox")
    st.markdown("<p class='fade-in'>Transforming digital into tangible with every print.</p>", unsafe_allow_html=True)
    st.write("Welcome to Jailxerox, your trusted partner for all Xerox and printing needs.")
    st.markdown("<div class='paper'></div>", unsafe_allow_html=True)  # Add the paper animation

def show_services():
    st.title("Our Services")
    st.write("At Jailxerox, we offer a wide range of services to cater to your needs:")
    services = ["Xerox", "Printing", "Scanning", "Binding", "Lamination"]
    for service in services:
        st.write(f"- {service}")

def show_blog():
    st.title("Blog")
    st.write("Stay tuned for updates and insights from Jailxerox.")
    st.write("We'll be sharing tips, news, and articles on the latest in printing technology and services.")

def show_contact_us():
    st.title("Contact Us")
    st.write("We'd love to hear from you! Please fill out the form below to get in touch with us.")

    with st.form(key='contact_form'):
        name = st.text_input(label="Name")
        email = st.text_input(label="Email")
        message = st.text_area(label="Message")
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            st.success("Thank you for reaching out to us!")

if __name__ == "__main__":
    main()
