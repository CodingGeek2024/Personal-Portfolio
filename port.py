import streamlit as st
import base64

def css_styling():
    """Add custom CSS for styling the portfolio"""
    st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        color:rgb(235, 240, 245);
        text-align: center;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 1.5rem;
        color:rgb(236, 241, 245);
        border-bottom: 2px solidrgb(179, 218, 245);
        padding-bottom: 10px;
        margin-top: 20px;
    }
    .contact-info {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #F0F3F4;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .link-button {
        display: inline-block;
        padding: 10px 15px;
        background-color:rgb(187, 219, 241);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin: 5px;
        transition: background-color 0.3s ease;
    }
    .link-button:hover {
        background-color:rgb(195, 223, 242);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Page Configuration
    st.set_page_config(page_title="Shubham Kumar - Portfolio", page_icon=":technologist:", layout="wide")
    
    # Custom CSS
    css_styling()
    
    # Main Content
    st.markdown('<h1 class="main-title">Shubham Kumar - Portfolio</h1>', unsafe_allow_html=True)
    
    # Contact Information
    st.markdown("""
    <div class="contact-info">
        <strong>📧 Email:</strong> Codinggeek1728@gmail.com
        <strong>📱 Phone:</strong> +91-8810325212
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.title("Portfolio Navigator")
    page = st.sidebar.radio("Go to", 
        ["About Me", "Education", "Experience", "Projects", "Skills", "Achievements"])
    
    if page == "About Me":
        about_me()
    elif page == "Education":
        education()
    elif page == "Experience":
        experience()
    elif page == "Projects":
        projects()
    elif page == "Skills":
        skills()
    elif page == "Achievements":
        achievements()

def about_me():
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    st.write("""
    A passionate Computer Science graduate from Delhi Technological University with a strong foundation 
    in software development, problem-solving, and emerging technologies. I am dedicated to creating 
    innovative solutions and continuously expanding my technical skills.
    """)
    
    # Profiles with Direct Links
    st.markdown('<h3>Professional Profiles</h3>', unsafe_allow_html=True)
    
    # Create a row of link buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <a href="https://leetcode.com/CodingGeek2024" target="_blank" class="link-button">
        🧩 LeetCode Profile
        </a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <a href="https://github.com/CodingGeek2024" target="_blank" class="link-button">
        💻 GitHub Profile
        </a>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <a href="https://www.linkedin.com/in/shubham-kumar-rawat-b69b1a19b/" target="_blank" class="link-button">
        🔗 LinkedIn Profile
        </a>
        """, unsafe_allow_html=True)
        
        

def education():
    st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Bachelor in Computer Science
    **Delhi Technological University (Formerly DCE)**
    - Graduated: June 2023
    - Location: New Delhi, India
    - CGPA: 7.34/10
    """)
    
    st.markdown('<h3>Relevant Courses</h3>', unsafe_allow_html=True)
    courses = [
        "Data Structures & algorithm", "Computer Network", "Web Technology", 
        "Machine Learning", "Operating System", 
        "Object-Oriented-Programming", "Database Management System"
    ]
    
    for course in courses:
        st.markdown(f"- {course}")
    
    st.markdown('<h3>Additional Courses</h3>', unsafe_allow_html=True)
    # Adding direct links to course certificates
    st.markdown("""
    ### Coursera Certificates
    - [Crash Course on Python](https://www.coursera.org/account/accomplishments/certificate/3AWJHBS7KHH3)
    - [Building Modern Python Applications on AWS](https://www.coursera.org/account/accomplishments/certificate/EDV2KUP3DLME)
    
    
    """)

def experience():
    st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Web Development & Design Intern
    **Tripfox Travellers** | March 2024 – May 2024
    
    [View Internship Details](https://drive.google.com/drive/u/2/folders/14kg9g3eXmaMfsFatlrnWAVyPtesb12rg)
    
    - Completed an educational internship focused on web development and product design
    - Gained experience with NodeJS, ReactJS, and CI/CD pipelines
    - Collaborated using Agile methodologies
    """)

def projects():
    st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
    
    # AI Chatbot Project
    st.markdown("""
    ### AI Chatbot Project (June 2023 – September 2023)
    [Project Repository](https://github.com/CodingGeek2024/Developed-_AI_Chatbot_using_Python_Project)
    
    - Developed an AI chatbot using Python and TensorFlow for customer support
    - Implemented NLP techniques to enhance user interaction
    - Conducted A/B testing, resulting in 40% performance improvement
    - Presented project outcomes at industry conferences
    """)
    
    # Sales Management System
    st.markdown("""
    ### Sales Management System (September 2021 – March 2022)
    [Project Repository](https://github.com/CodingGeek2024/Developed-_C-_Project)
    
    - Designed a Sales Management System using C++ and Database Management System concepts
    - Documented network policies and procedures
    - Prioritized system maintenance and data integrity
    """)
 # Portfolio
    st.markdown("""
    ### Personal Portfolio (October 2024 – November 2024)
    [Project Repository](https://github.com/CodingGeek2024/Personal-Portfolio)
    
    I developed a personal portfolio web application using Streamlit and Python, 
    showcasing my technical skills, educational background, and professional experiences. 
    The project integrates multiple technologies and demonstrates 
    how I can leverage modern tools to build interactive and user-friendly applications.
    """)
def skills():
    st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        st.markdown("""
        - C++
        - Python
        - Java &
        - JavaScript (Basics)
        """)
        
        st.markdown("### Databases")
        st.markdown("""
        - SQL
        - MySQL       
        
        """)
    
    with col2:
        st.markdown("### Technologies & Tools")
        st.markdown("""
        - HTMl
        - CSS
        - Angular
        - Design Patterns
        - Visual Studio
        - Streamlit
        """)
        
        st.markdown("### Soft Skills")
        st.markdown("""
        - Problem-Solving
        - Customer Needs Analysis
        - Decision-Making
        - Written and Verbal Communication Skills
        - Team Player
        """)

def achievements():
    st.markdown('<h2 class="section-title">Achievements & Publications</h2>', unsafe_allow_html=True)
    
    achievements_list = [
        "[Solved 500+ problems on Coding Blocks and Leetcode](https://leetcode.com/CodingGeek2024)",
        "JEE Mains 2019: Rank 296",
        "JEE Advance 2019: Rank 1751",
        "[Research Paper: Chat GPT & Google Bard AI: A Review - Published at IEEE ICICAT 2023 Conference](https://ieeexplore.ieee.org/document/10263706)"
    ]
    
    for achievement in achievements_list:
        st.markdown(f"- {achievement}", unsafe_allow_html=True)
    
    st.markdown("### Extracurricular")
    st.markdown("- D_CODER Coding Society Member (Aug 2019 – June 2023)")
     

# Run the app
if __name__ == "__main__":
    main()
