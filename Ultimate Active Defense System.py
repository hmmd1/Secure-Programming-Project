import os
import time
import logging
import socket
import requests       # For Telegram & Geolocation
import winsound       # For Alarm (Windows only)
import pyautogui      # For Screenshots
import ctypes         # For System Lock
import tkinter as tk  # For Popup Warnings
from tkinter import messagebox
from datetime import datetime

# ==========================================
#          CONFIGURATION & SETUP
# ==========================================
1
# 🔴 STEP 1: PASTE YOUR TELEGRAM CREDENTIALS HERE
TELEGRAM_TOKEN = "8483397448:AAFFcAc-nxKyWsLTvbrwZp8i8MhQZY2dySg1"
CHAT_ID = "895439704"

# File Names
LOG_FILE = 'intruder_log.txt'
HONEY_POT_FILE = "secret_passwords.txt"

# Logging Configuration
logging.basicConfig(filename=LOG_FILE, level=logging.WARNING, format='%(asctime)s - %(message)s')

# ==========================================
#        COUNTERMEASURES (DEFENSE TOOLS)
# ==========================================

def get_public_ip_info():
    """Fetches Public IP and Location (City, Country)."""
    try:
        response = requests.get('https://ipinfo.io/json').json()
        return f"Public IP: {response.get('ip')} | Location: {response.get('city')}, {response.get('country')}"
    except:
        return "Public IP: Not Available (No Internet Connection)"

def take_screenshot():
    """Captures a screenshot of the intruder's screen."""
    try:
        # Generate a unique filename with timestamp
        filename = f"evidence_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(filename)
        print(f"📸 [Evidence] Screenshot saved as: {filename}")
    except Exception as e:
        print(f"⚠️ Screenshot failed: {e}")

def play_alarm():
    """Plays a loud beep sound to startle the intruder."""
    try:
        # Frequency: 2500Hz, Duration: 1000ms (1 second)
        print("🔊 [Alarm] Siren Triggered!")
        winsound.Beep(2500, 1000) 
        winsound.Beep(2500, 1000)
    except:
        pass

def show_warning_popup():
    """Displays a scary popup message on the screen."""
    root = tk.Tk()
    root.withdraw() # Hide the main window
    root.attributes("-topmost", True) # Keep popup on top
    
    # This message blocks code execution until user clicks OK
    messagebox.showwarning("⚠️ CRITICAL SECURITY ALERT ⚠️", 
                           "UNAUTHORIZED ACCESS DETECTED!\n\n"
                           "Your IP Address, Location, and Photo have been sent to the Administrator.\n\n"
                           "Do not attempt to close this window.")
    root.destroy()

def lock_workstation():
    """Locks the Windows session immediately."""
    print("🔒 [Defense] Locking System...")
    ctypes.windll.user32.LockWorkStation()

def send_telegram_alert(message):
    """Sends the security report to your Telegram App."""
    try:
        if "YOUR_BOT" in TELEGRAM_TOKEN:
            print("⚠️ Token not set. Skipping Telegram alert.")
            return 
            
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, data=data)
        print("✅ [Alert] Telegram notification sent!")
    except:
        print("⚠️ Failed to connect to Telegram.")

# ==========================================
#              CORE LOGIC
# ==========================================

def create_honeypot():
    """Creates the trap file."""
    with open(HONEY_POT_FILE, "w") as f:
        f.write("CONFIDENTIAL DATA\nServer Admin: root\nPassword: Toor_12345\nDO NOT SHARE!")
    print(f"\n[+] Honeypot file '{HONEY_POT_FILE}' deployed successfully.")

def start_monitoring():
    if not os.path.exists(HONEY_POT_FILE):
        create_honeypot()

    print("\n" + "!"*60)
    print("   🛡️  ULTIMATE ACTIVE DEFENSE SYSTEM (ONLINE)  🛡️")
    print("   ------------------------------------------------")
    print("   📸 Screenshot | 📢 Alarm | 🌍 Location | 🔒 Auto-Lock")
    print("!"*60)
    print(f"👀 System is watching '{HONEY_POT_FILE}'...")
    
    send_telegram_alert("🟢 System Online: Monitoring Started.")
    
    # Get initial access time
    last_access_time = os.path.getatime(HONEY_POT_FILE)

    try:
        while True:
            current_access_time = os.path.getatime(HONEY_POT_FILE)
            
            if current_access_time != last_access_time:
                print("\n🚨 INTRUSION DETECTED! INITIATING COUNTERMEASURES... 🚨")
                
                # 1. Play Alarm (Psychological Warfare)
                play_alarm()
                
                # 2. Capture Evidence
                take_screenshot()
                
                # 3. Gather Intelligence
                local_host = socket.gethostname()
                local_ip = socket.gethostbyname(local_host)
                public_info = get_public_ip_info()
                
                # Prepare Report
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                details = f"Time: {timestamp}\nHost: {local_host} ({local_ip})\n{public_info}"
                
                # 4. Notify Admin (Telegram)
                alert_msg = f"⛔ HACKER CAUGHT! ⛔\n\n{details}\n\n📸 Evidence saved locally."
                send_telegram_alert(alert_msg)
                
                # 5. Log Locally
                logging.warning(f"BREACH DETECTED: {details}")
                
                # 6. Show Warning Popup (Freezes user until OK is clicked)
                show_warning_popup()
                
                # 7. Final Blow: Lock the PC
                lock_workstation()
                
                # Update time to avoid loops
                last_access_time = current_access_time
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")

# ==========================================
#              MAIN MENU
# ==========================================
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "█"*50)
        print("█   🔐 SECURE PROGRAMMING: ACTIVE DEFENSE 🔐     █")
        print("█"*50)
        print("1. Start Ultimate Monitoring (Beast Mode)")
        print("2. View Forensics Logs")
        print("3. Exit")
        
        choice = input("\nSelect Option > ")

        if choice == '1':
            start_monitoring()
        elif choice == '2':
            print("\n--- FORENSICS LOGS ---")
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    print(f.read())
            else:
                print("No logs found.")
            input("\nPress Enter to return...")
        elif choice == '3':
            print("Exiting... Stay Safe!")
            break

if __name__ == "__main__":
    main_menu()