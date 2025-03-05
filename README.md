# COVID-19 Data Analysis Dashboard

## 📌 Overview
This project is a **COVID-19 Data Analysis Dashboard** built using Python and **Streamlit**. The application provides visual insights into the COVID-19 pandemic by displaying:
- Total confirmed cases over time
- Daily new cases
- Case fatality rate

The dashboard allows users to explore the data interactively through a sidebar selection.

---
## 🚀 Features
- **Data Loading**: Simulated COVID-19 data.
- **Data Preprocessing**: Cleaning, computing daily new cases, and case fatality rate.
- **Visualization**:
  - Line plot for total confirmed cases.
  - Bar chart for daily new cases.
  - Line plot for case fatality rate.
- **Interactive Dashboard**: Users can select different visualizations.
- **Key Statistics Display**: Total confirmed cases, total deaths, and case fatality rate.

---
## 🛠️ Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

---
## 📂 Project Structure
```
📂 covid-dashboard
│── app.py                  # Main application file
│── requirements.txt        # Dependencies required to run the project
│── README.md               # Project documentation
```

---
## 📥 Installation & Setup
### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/your-username/covid-dashboard.git
 cd covid-dashboard
```
### 2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

---
## 📊 How to Use
1. Open the **sidebar** and select a visualization:
   - "Total Cases"
   - "Daily New Cases"
   - "Case Fatality Rate"
2. The corresponding graph will be displayed.
3. Check the **Key Statistics** section for summarized COVID-19 metrics.

---
## 📌 Future Enhancements
- ✅ Integration of real-world COVID-19 datasets from **WHO** or **Johns Hopkins University**.
- ✅ Addition of more interactive filters (e.g., country selection).
- ✅ Implementation of predictive modeling for COVID-19 trends.


