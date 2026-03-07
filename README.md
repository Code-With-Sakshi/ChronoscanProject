# 🧠 ChronoScan – Tumor Change Detection System

ChronoScan is an AI-powered medical imaging tool that analyzes MRI scans to detect **tumor growth or reduction over time**.
The system compares two MRI scans taken at different time intervals and highlights the **percentage change in tumor area**, helping visualize disease progression.

This project demonstrates how **machine learning and image processing** can assist medical analysis by providing automated tumor change detection.

---

# 🚀 Features

* Upload **two MRI scans** (Day-0 and Day-5)
* Automatically detect tumor regions
* Calculate **tumor area change percentage**
* Visualize tumor segmentation masks
* Generate a **diagnostic report**
* Display **tumor change heatmaps**
* User **login/signup authentication system**
* Web interface built with **Streamlit**

---

# 🖥️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning & Image Processing

* TensorFlow / Keras
* OpenCV
* NumPy
* Scikit-image
* Scikit-learn

### Database

* SQLite

### Deployment

* GitHub
* Streamlit Cloud

---

# 📂 Project Structure

chronoscan/
│
├── streamlit_app.py        # Main Streamlit application
├── app.py                  # Flask API for tumor analysis
├── main.py                 # Helper script
├── process.py              # Processing script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
├── user.db                 # SQLite database for login
│
├── ml/                     # Machine learning modules
│   ├── change_detector.py
│   ├── compare.py
│   ├── measure.py
│   ├── pipeline.py
│   ├── preprocess.py
│   ├── report.py
│   ├── scoring.py
│   └── segment.py
│
├── templates/              # HTML templates
│   └── index.html
│
├── uploads/                # Temporary uploaded images
│
└── results/                # Generated results
└── changes/

---

# 🧠 Model

The tumor detection model was trained using a brain tumor MRI dataset from Kaggle.

The dataset contains images categorized into:

* **Tumor (yes)**
* **No Tumor (no)**

Due to GitHub file size limitations, the trained model (`brain_tumor_model.h5`) is stored externally and downloaded automatically from Google Drive when the application starts.

---

# 📊 How ChronoScan Works

1. User uploads **Day-0 MRI scan**
2. User uploads **Day-5 MRI scan**
3. Images are preprocessed
4. Tumor segmentation is performed
5. Tumor area is measured
6. Percentage change is calculated
7. Visual reports and masks are generated

Output includes:

* Tumor segmentation masks
* Tumor change heatmap
* Tumor change percentage
* Diagnostic report

---

# 🔐 Authentication System

ChronoScan includes a simple login system using SQLite.

Users can:

* Create an account
* Login securely
* Access tumor analysis features

---

# ⚙️ Installation (Local Setup)

Clone the repository:

git clone https://github.com/your-username/chronoscan.git

Navigate to project folder:

cd chronoscan

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run streamlit_app.py

The app will start at:

http://localhost:8501

---


# ⚠️ Limitations

* This project is for **educational purposes only**
* Not intended for real medical diagnosis
* Accuracy depends on dataset quality and model training

---

# 🔮 Future Improvements

* 3D MRI tumor analysis
* Improved deep learning segmentation
* Doctor dashboard
* Patient history tracking
* AI-generated medical reports
* Cloud-based medical imaging storage




