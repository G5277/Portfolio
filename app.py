from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# ----- PAGE CONFIG -----
st.set_page_config(page_title=" Portfolio ", page_icon=":star:", layout="wide")

# ----- FUNCTIONS ------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ----- Use Local CSS -----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("./style/style.css")
# ----- LOAD ASSETS -----
lottie_girlie = "https://lottie.host/b27470ff-d11b-414d-8d89-6dbfc6fca337/Monk1RKL50.json"
image_char = Image.open("images/githubsticker.png")
image_p1 = Image.open("images/Project1.png")
image_p2 = Image.open("images/Project2.png")
image_p3 = Image.open("images/Project3.jpg")

# ----- HEADER SECTION -----
with st.container():
    text_column, image_column = st.columns((2,0.7))
    with image_column:
        st.image(image_char, width=1000)
    with text_column:
        st.header("Hi! I am Gazal :dizzy:", divider = True)
        #st.write("---")
        st.write(" ")
        st.subheader(
        "A Data Scientist and Machine Learning Enthusiast from India~")
        about_me = "I'm passionate about finding ways of combining my imagination and fantasies with technology to develop magical."
        s = f"<p style='font-size:20px;'>{about_me}</p>"
        st.markdown(s, unsafe_allow_html=True)
        # st.write(":wink:")
        st.write("[Check out my github > ](https://github.com/G5277)")

# ---- WHAT AM I LEARNING ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("Something about me :eyes:", divider="blue")
        st.write(
            """
            Currently, a pre-final year student at Thapar Institute of Engineering and Technology:            
            - I am studying Data Science in R
            - Trying to get comfortable with Pytorch - a python framework for Deep Learning
            - Doing some projects using Streamlit
            - Looking for a good internship opportunity to put my skills to use
            - Learning DSA and trying to solve problems on LeetCode 
            - and a few more things ~

            If you'd like to collaborate on some project or disucss about soemthing, feel free to contact me ;)
            """
        )

        st.write("[Email me :email:](mailto:2580gazal@gmail.com)")

    with right_column:
        st.write(" ")
        st.write(" ")
        st_lottie(lottie_girlie, height=300, key="girlie")


# ----- PROJECTS -----
with st.container():
    st.write("---")
    st.header("My Projects 👩‍💻", divider=True)


    # Project 1    
    with st.container():
        image_column, text_column = st.columns((1, 2))

        with image_column:
            st.write(" ")
            st.write(" ")
            st.image(image_p2, width=300)

        with text_column:
            st.write(" ")
            st.write(" ")
            st.subheader("Handwritten Digit Recognition")
            st.write(
                """
                - Built a handwritten digit recognition system achieving a classification accuracy of 98.9% on the MNIST dataset
                - Trained the model on 60,000 training images, achieving a loss of 0.02 and validating the model on 10,000 test images
                - Designed and implemented a real-time, interactive front-end in Pygame allowing users to draw digits and receive predictions instantly with a prediction time of under 500 ms
                """
            )
            st.markdown(
                "[Visit the Source Code ~](https://github.com/G5277/handwrittendigit)")
            st.write(" ")
            st.write(" ")

    # Project 2
    with st.container():
        text_column, empty_column, image_column = st.columns((2, 0.3,0.7))

        with image_column:
            st.write(" ")
            st.write(" ")
            st.image(image_p1, width=300)

        with text_column:
            st.write(" ")
            st.write(" ")
            st.subheader("ASL Detector")
            st.write(
                """
                - Developed a real-time American Sign Language (ASL) gesture recognition system Trained a machine learning model to classify hand gestures with an accuracy of 92.1 percent
                - Optimized model performance by pre-processing over 5,000 frames of video data, including resizing, normalization, and augmentation, improving gesture detection reliability by 15%                """
            )
            st.markdown(
                "[Visit the Source Code ~](https://github.com/G5277/ASL-Detector)")
            
    # Project 3    
    with st.container():
        image_column, text_column = st.columns((1, 2))

        with image_column:
            st.write(" ")
            st.write(" ")
            st.image(image_p3, width=300)

        with text_column:
            st.write(" ")
            st.write(" ")
            st.subheader("Smart Health Recognition")
            st.write(
                """
                - Developed a Smart Healthcare Diagnosis System achieving an ensemble model accuracy of 98.64%, reducing false negatives by 15% in healthcare diagnostics.
                - Designed and implemented an ensemble learning approach using Logistic Regression meta-model, combining XGBoost (~98% accuracy) and ANN (~96.79% accuracy) predictions to improve classification reliability.
                - Curated a synthetic dataset with 10+ key attributes to simulate real-world scenarios, improving data availability by 100%.
                - Addressed class imbalance by using SMOTE, oversampling underrepresented classes by 50%, which enhanced model performance on minority classes by 30%.
                """
            )
            st.markdown(
                "[Visit the Source Code ~](https://github.com/G5277/handwrittendigit)")
            st.write(" ")
            st.write(" ")

    # # Project 4
    # with st.container():
    #     text_column, empty_column, image_column = st.columns((2, 0.3,0.7))

    #     with image_column:
    #         st.write(" ")
    #         st.write(" ")
    #         st.image(image_p1, width=300)

    #     with text_column:
    #         st.write(" ")
    #         st.write(" ")
    #         st.subheader("ASL Detector")
    #         st.write(
    #         """
    #             - Developed a real-time American Sign Language (ASL) gesture recognition system Trained a machine learning model to classify hand gestures with an accuracy of 92.1 percent
    #             - Optimized model performance by pre-processing over 5,000 frames of video data, including resizing, normalization, and augmentation, improving gesture detection reliability by 15%                
    #         """
    #         )
    #         st.markdown(
    #             "[Visit the Source Code ~](https://github.com/G5277/ASL-Detector)")

# ----- CONTACT FORM -----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("Fill out the form below to send me a message:")

    # Creating the form
    with st.form(key="contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email")
        message = st.text_area("Your Message", placeholder="Write your message here")
        submit_button = st.form_submit_button(label="Send")

        # Form submission logic
        if submit_button:
            if not name or not email or not message:
                st.error("Please fill out all fields before submitting!")
            else:
                # Simulate a successful form submission
                st.success(f"Thank you, {name}! Your message has been sent successfully.")
                st.write("I will get back to you soon. 😊")
