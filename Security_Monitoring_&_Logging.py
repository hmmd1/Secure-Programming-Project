import os
import time
import logging
import socket

# ==========================================
#          CONFIGURATION & SETUP
# ==========================================
# ملف السجلات (Where intruders are recorded)
LOG_FILE = 'intruder_log.txt'
# الملف الطعم (The Trap)
HONEY_POT_FILE = "secret_passwords.txt"

# إعداد نظام التسجيل
logging.basicConfig(filename=LOG_FILE, level=logging.WARNING, format='%(asctime)s - %(message)s')

# ==========================================
#              CORE FUNCTIONS
# ==========================================

def get_intruder_info():
    """Retrieves IP and Hostname of the intruder."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return f"Hostname: {hostname} | IP: {ip_address}"
    except:
        return "Unknown Device"

def create_honeypot():
    """Creates the fake file if it doesn't exist."""
    with open(HONEY_POT_FILE, "w") as f:
        f.write("CONFIDENTIAL DATA\nAdmin: admin\nPass: 123456\nDO NOT SHARE!")
    print(f"\n[+] Honeypot file '{HONEY_POT_FILE}' created successfully.")

def view_logs():
    """Displays the intruder log with numbering (Forensics Mode)."""
    print("\n" + "="*50)
    print("       📂 FORENSICS REPORT (LOG VIEWER)")
    print("="*50)
    
    if not os.path.exists(LOG_FILE):
        print("[-] No logs found yet. Start monitoring first.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("[-] Log file is empty.")
    else:
        # Loop through lines with numbering (The feature you asked for)
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")
            
    print("="*50 + "\n")
    input("Press Enter to return to menu...")

def start_monitoring():
    """Starts the active defense system."""
    if not os.path.exists(HONEY_POT_FILE):
        create_honeypot()

    print("\n" + "!"*50)
    print("   🛡️  ACTIVE DEFENSE SYSTEM STARTED  🛡️")
    print("   Press 'Ctrl + C' to stop monitoring.")
    print("!"*50)
    print(f"👀 System is watching '{HONEY_POT_FILE}'...")

    last_access_time = os.path.getatime(HONEY_POT_FILE)

    try:
        while True:
            current_access_time = os.path.getatime(HONEY_POT_FILE)
            
            if current_access_time != last_access_time:
                intruder_info = get_intruder_info()
                
                print("\n🚨 ALERT: INTRUSION DETECTED!")
                print(f"🕵️‍♂️ Details: {intruder_info}")
                
                # Log to file
                logging.warning(f"TAMPERING DETECTED! Details: {intruder_info}")
                
                last_access_time = current_access_time
                print("📝 Event logged.")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Monitoring stopped. Returning to menu...")
        time.sleep(1)

# ==========================================
#              MAIN INTERFACE
# ==========================================
def main_menu():
    while True:
        # Clear screen (optional, works on Windows 'cls' or Linux 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "█"*40)
        print("█   🔐 SECURE PROGRAMMING PROJECT 🔐   █")
        print("█"*40)
        print("1. Start Honeypot Monitoring (Active Mode)")
        print("2. View Intruder Logs (Forensics Mode)")
        print("3. Exit")
        print("-" * 40)
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            start_monitoring()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            print("Exiting... Stay Secure! 👋")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()