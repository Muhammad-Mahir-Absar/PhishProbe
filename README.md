PhishProbe is an intelligent, machine-learning web application designed to identify and analyze phishing URLs. Developed with a focus on proactive cybersecurity, this tool provides users with an intuitive interface to verify the legitimacy of suspicious links before they can cause harm.

🚀 Key Features
-------------------
Real-time Detection: 
Instantly analyze URLs to determine if they are legitimate or phishing attempts.

Machine Learning Engine: 
Utilizes a trained model (phish_model.pkl) to make data-driven security assessments.

Sophisticated Feature Extraction: 
Breaks down URL structures—including domain age, subdomains, and special character patterns—to identify malicious indicators.

Interactive Streamlit UI: 
A multi-page, user-friendly dashboard for seamless navigation and analysis.

📂 Project Architecture
--------------------------

1_🏚️_Home.py:                
Main landing page & application entry point

2_🔗_PhishURL Detect.py:   
Core detection interface

feature_extraction.py:      
Logic for parsing URL attributes

features.py:                
Definition of security indicators

phish_model.pkl:            
Pre-trained Random Forest/ML model

vectorizer.pkl:             
Serialized text processing component

data_collector.py:          
Script for gathering/updating training data

Pages:                     
Supporting application modules

🛠️ Installation & Setup 
(N.B: Ensure you have Python 3.10+ installed on your system)
-------------------------------------------------------------------------------------

1. Clone the Repository:
--------------------------
git clone https://github.com/Muhammad-Mahir-Absar/PhishProbe.git

cd PhishProbe

2. Set Up a Virtual Environment:
---------------------------------
python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies:
-------------------------
pip install -r requirements.txt

🖥️ How to Use
----------------
To launch the application locally, run this following command to the terminal:

streamlit run 1_🏚️_Home.py

1. Open the local URL provided in your terminal (typically http://localhost:8501).

2. Navigate to the PhishURL Detect page.

3. Enter a suspicious URL and click Analyze to see the safety verdict.

📊 Data & Training
------------------------
The model's accuracy is derived from a diverse training set, including:

Tranco List: Used to establish a baseline for highly reputable, legitimate domains.

PhishTank/OpenPhish Data: Sourced from verified phishing databases to train the model on current attack vectors.

Structured CSVs: Processed data files included in the repo for model transparency.

📝 License
----------------
This project is Developed by Mahir Absar Anik.
