# 🤖 AI Resume Ranking System

An intelligent resume screening and ranking system that uses **Machine Learning and NLP techniques** to evaluate and rank resumes based on a given job description.

---

## 🚀 Live Demo

🌐 **Live App:** https://resume-screening-uzpp.onrender.com
📦 **GitHub Repository:** https://github.com/rohhannn/resume-screening

---

## ✨ Features

* 📄 Upload multiple resumes (PDF format)
* 🧠 AI-based resume analysis
* 🎯 Match resumes with job description
* 📊 Resume scoring & ranking system
* 🔍 Keyword extraction using NLP
* ⚡ Instant results with sorted rankings
* 📁 File handling and parsing system
* 🎨 Clean and interactive UI

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python (Flask)
* REST API

### Machine Learning / NLP

* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### File Processing

* PyPDF2 / pdfplumber

---

## 🧠 How It Works

1. User uploads resumes
2. Job description is entered
3. Text is extracted from resumes
4. TF-IDF converts text into vectors
5. Cosine similarity compares resumes with job description
6. Resumes are ranked based on similarity score

---

## 📁 Project Structure

```id="ai1"
resume-screening/
│
├── model/
│   ├── model.py
│   ├── parser.py
│   ├── utils.py
│
├── templates/
│   ├── index.html
│
├── static/
│   ├── style.css
│
├── uploads/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## ▶️ Run Locally

### 1. Clone repository

```id="ai2"
git clone https://github.com/rohhannn/resume-screening.git
cd resume-screening
```

### 2. Create virtual environment

```id="ai3"
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```id="ai4"
pip install -r requirements.txt
```

### 4. Run application

```id="ai5"
python3 app.py
```

### 5. Open in browser

```id="ai6"
http://localhost:5000
```

---

## 📊 Output Example

* Resume Score: 85%
* Ranked position: #1
* Matching keywords highlighted

---

## 🚧 Future Improvements

* 🤖 Deep Learning models (BERT-based ranking)
* 📊 Advanced analytics dashboard
* 📁 Support for DOCX files
* 🔐 User authentication system
* ☁️ Cloud storage integration

---

## 👨‍💻 Author

**Rohan Sanjay Ranga**
🔗 GitHub: https://github.com/rohhannn

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you found this useful, give it a star!
