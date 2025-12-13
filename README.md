# 🛡️ Active Defense System (Honeypot Project)

## 📌 Project Overview
This project is a Secure Programming tool designed to implement the concept of **Active Defense**. Instead of just encrypting data, this tool sets a "Trap" (Honeypot) to detect and identify unauthorized access attempts.

## 🚀 How It Works
1. **The Trap:** The system creates a fake file named `secret_passwords.txt` containing fake credentials.
2. **Monitoring:** The Python script monitors the file's metadata (Last Access Time) in real-time.
3. **Detection:** If anyone opens the file, the system triggers an alert immediately.
4. **Forensics:** The intruder's **IP Address** and **Hostname** are logged into `intruder_log.txt` for evidence.

## 🛠️ Features
- **Real-time Monitoring:** Detects file access instantly.
- **Intrusion Logging:** Records timestamp, IP, and Hostname.
- **Forensics Mode:** Allows the admin to view a numbered list of all attack attempts.
- **Menu System:** Simple CLI interface to control the tool.

## 💻 How to Run
1. Ensure you have Python installed.
2. Run the script:
   ```bash
   python final_project.py
