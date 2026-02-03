import pandas as pd
from datetime import datetime
import pyttsx3

# Load product data
df = pd.read_csv("products.csv")

# Convert date columns
df["Manufacture_Date"] = pd.to_datetime(df["Manufacture_Date"])
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

today = datetime.now().date()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("\n===== SUPERMARKET EXPIRY ALERT SYSTEM =====\n")

near_expiry = []
expired = []

for index, row in df.iterrows():
    product = row["Product"]
    exp_date = row["Expiry_Date"].date()
    days_left = (exp_date - today).days

    if days_left < 0:
        status = "EXPIRED"
        expired.append(product)
        color = "\033[91m"  # RED
        
    elif 0 <= days_left <= 3:
        status = "NEAR EXPIRY"
        near_expiry.append(product)
        color = "\033[93m"  # YELLOW
        
    else:
        status = "SAFE"
        color = "\033[92m"  # GREEN

    print(f"{color}{product} → {status} ({days_left} days left)\033[0m")

# Voice Alerts
if expired:
    speak("Warning! Some products have already expired.")
    print("\n⚠ Voice Alert: Expired items found!")

if near_expiry:
    speak("Alert! Some items are near expiry. Please check them immediately.")
    print("⚠ Voice Alert: Items near expiry!")

print("\nProcess Completed.")
