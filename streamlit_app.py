 
import streamlit as st

# Set the title of the app
st.set_page_config(page_title="Jailxerox", layout="wide")

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
    st.markdown("""
    <style>
    body {
        background-color: #333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Jailxerox")
    st.write("Transforming digital into tangible with every print.")
    st.write("Welcome to Jailxerox, your trusted partner for all Xerox and printing needs.")

def show_services():
    st.markdown("""
    <style>
    body {
        background-color: #333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Our Services")
    st.write("At Jailxerox, we offer a wide range of services to cater to your needs:")
    services = ["Xerox", "Printing", "Scanning", "Binding", "Lamination"]
    for service in services:
        st.write(f"- {service}")

def show_blog():
    st.markdown("""
    <style>
    body {
        background-color: #333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Blog")
    st.write("Stay tuned for updates and insights from Jailxerox.")
    st.write("We'll be sharing tips, news, and articles on the latest in printing technology and services.")

def show_contact_us():
    st.markdown("""
    <style>
    body {
        background-color: #333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
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

