Supermarket Expiry Date Alert System

A Python-based supermarket inventory tool that detects expired and near-expiry items using color-coded warnings and voice alerts.

🚀 Features
- Reads product details from a CSV file  
- Calculates days left for expiry  
- Color-coded alerts:
  - 🟩 Safe  
  - 🟨 Near Expiry (0–3 days)  
  - 🟥 Expired  
- Voice notifications using Text-to-Speech  
- Simple and user-friendly

🛠 Technologies Used
- Python  
- Pandas  
- Pyttsx3  
- CSV File Handling  

📂 Project Files
```
expiry_alert.py  
products.csv  
requirements.txt  
README.md  
```
 📊 Sample CSV Format
```
Product,Manufacture_Date,Expiry_Date,Quantity
Milk,2024-01-01,2024-01-07,10
Bread,2024-01-05,2024-01-09,5
Biscuits,2024-01-01,2025-01-01,20
```
 ▶️ How to Run
Install required libraries:
```
pip install pandas pyttsx3
```

Run the script:
```
python expiry_alert.py
```
👩‍💻 Developer
Meher Nikhita Mandavilli
