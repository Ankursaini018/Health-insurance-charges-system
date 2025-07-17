# 🏥 Insurance Cost Prediction System

A machine learning-based web application that predicts **medical insurance charges** based on a user's health profile and demographics. This tool helps users understand how different factors influence their insurance costs and provides a seamless, data-driven estimation experience.

---

## 🌟 Features

* ✅ **Real-time Prediction** of insurance charges
* 🧠 **Trained ML Model** using scikit-learn for regression analysis
* 🌐 **Interactive Web Interface** with dynamic form inputs
* 📊 **Data Visualization** and analysis through a Jupyter Notebook
* 📁 **Modular Project Structure** with reusable components
* 🖥️ **Responsive HTML Templates** using Flask and Jinja2

---

## 📂 Project Structure

├── app.py # Flask backend server
├── model.pkl # Pre-trained regression model
├── insurance.csv # Dataset used for model training
├── insurance\_clean.csv # Cleaned version of dataset
├── Insurance\_Prediction.ipynb # Notebook with EDA, model training, metrics
├── templates/ # HTML pages for frontend
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ ├── history.html
│ └── layout.html
├── static/ # Images and visual assets
│ └── logo and health-insurance image

## 📝 Important Notes

* Built with **Python 3.8+**, Flask, scikit-learn, pandas, and matplotlib.
* The regression model uses features like:

  * **Age**
  * **Gender**
  * **BMI (Body Mass Index)**
  * **Number of Children**
  * **Smoker status**
  * **Region**
* The model is pre-trained — no need to retrain unless modifying the data.
* All templates and static files are structured for easy customization.

---

⭐ Show Your Support

If you like this project, please ⭐ star the repository to support the work!
