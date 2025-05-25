

# Genix2 - Login-Based Web App with SQL Integration

Genix2 is a simple yet functional login-based web application built using Python Flask, SQL, and HTML/CSS, styled according to a Figma design prototype. The project helps you learn how to integrate frontend designs, backend logic, and database functionality — and deploy the entire system online.

## 🖼️ UI Reference
Design created on [Figma - Assessment GenixAI](https://www.figma.com/design/sr0f0JlmvoeGo99EXsjNXB/Assesment-GenixAi)

---

## 💡 Features

- 🔐 Login & Signup functionality
- 🧠 Basic session-based authentication
- 🗃️ SQLite database integration
- 🎨 Figma-based HTML/CSS UI
- 🚀 Deployed on Render

---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS (custom from Figma)
- **Backend**: Python Flask
- **Database**: SQLite
- **Deployment**: [Render](https://render.com)

---

## 📁 Project Structure

#Genix2/
#│
#├── templates/
#│ ├── login.html
#│ ├── signup.html
#│ └── dashboard.html
#│
#├── static/
#│ └── css/
#│ └── style.css
#│
#├── app.py
#├── database.db
#└── requirements.txt



---

## ⚙️ Setup Instructions (Local)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Shrivastava19/Genix2.git
   cd Genix2
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open browser at: http://localhost:5000

🌐 Deployment (on Render)
The app is live at:
👉 https://genix2.onrender.com

To deploy yourself:

Create a free Render account

Click "New Web Service"

Connect this GitHub repo

Set:

Build Command: pip install -r requirements.txt

Start Command: python app.py

🧠 Learnings
Frontend to backend integration

Secure login logic with Flask

Deploying full-stack apps

Using Figma to guide UI development

📩 Contact
For queries or feedback, contact Yash


---

Let me know if you want me to generate a sample `requirements.txt` or help set up deployment from scratch again.
