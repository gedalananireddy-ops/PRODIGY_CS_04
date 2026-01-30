# PRODIGY_CS_04
Simple Keylogger (Educational Project)
⚠️ DISCLAIMER – READ FIRST
This project is created strictly for educational purposes such as:

Understanding how keyboard event listeners work
Learning defensive security concepts
Testing on systems you own or have explicit permission to use
Unauthorized keylogging is illegal and unethical.
Do NOT use this code on any system without clear consent.

📌 Project Description
This is a basic Python keylogger that:

Captures keyboard input
Logs keystrokes with timestamps
Saves them to a local file (keylog.txt)
Stops safely when the ESC key is pressed
There is:

❌ No persistence
❌ No stealth behavior
❌ No network communication
🛠️ Requirements
Python 3.8 or higher
Visual Studio Code (VS Code)
Internet access (only for installing dependencies)
📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/simple-keylogger.git
cd simple-keylogger
2️⃣ Open in VS Code
code .

3️⃣ Create a Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate
4️⃣ Install Dependencies
pip install pynput

▶️ How to Run the Program

In the VS Code terminal, run:

python keylogger.py


You should see:

Keylogger started (Press ESC to stop)

🧪 How It Works

Every key press is logged to keylog.txt

Normal keys are logged as characters

Special keys (Enter, Shift, Space, etc.) are logged in brackets

Press ESC to safely stop the program

📄 Example Output (keylog.txt)
2026-01-24 10:32:15 - h
2026-01-24 10:32:16 - e
2026-01-24 10:32:17 - l
2026-01-24 10:32:18 - l
2026-01-24 10:32:19 - o
2026-01-24 10:32:20 - [Key.space]

🔐 Ethical Considerations

Use only on your own system

Obtain explicit written permission before testing elsewhere

This project should not be used for spying, surveillance, or data theft

Violating privacy laws can lead to criminal charges.

🛡️ Defensive Learning (Suggested Next Steps)

Build a keylogger detection tool

Monitor keyboard hooks

Learn how antivirus software detects keylogging behavior

Harden systems against credential theft
