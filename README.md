# 💼 Streamlit Portfolio

An interactive portfolio web application built using **Streamlit** to showcase machine learning and data science projects in a visually engaging and professional format.

## 📌 Project Description

This portfolio serves as a central hub for displaying personal projects, technical skills, and achievements in the field of AI, ML, and data science. It is designed to be simple, responsive, and easy to navigate using Streamlit components and Lottie animations.

### 🔍 Key Highlights
- **Project Display**: Highlights individual projects with descriptions, an image, and GitHub links.
- **Streamlit Lottie Integration**: Adds animated visuals to enhance user engagement.
- **Custom Styling**: Uses local CSS to override default Streamlit styling for a personalized look.
- **Contact Form**: Integrated email contact form using [formsubmit.co](https://formsubmit.co) for direct messaging.

## 🧩 Technologies Used
- **Frontend/Framework**: Streamlit
- **Styling**: Custom CSS
- **Animations**: Lottie
- **Assets**: Pillow for image handling
- **Deployment**: Streamlit Cloud

## 🛠️ Project Structure
Streamlit-Portfolio/
├── app.py                  # Main Streamlit application file
├── style/
│   └── style.css           # Custom CSS for styling the Streamlit app
├── images/
│   ├── githubsticker.png   # Header image
│   ├── Project1.png        # ASL Detector project image
│   ├── Project2.png        # Handwritten Digit Recognition image
│   ├── Project3.jpg        # Smart Health Recognition project image
├── README.md               # Project documentation (this file)


## 📎 Setup Instructions
To run this project locally:

```bash
git clone https://github.com/G5277/Portfolio.git
cd Portfolio
pip install -r requirements.txt
streamlit run app.py

