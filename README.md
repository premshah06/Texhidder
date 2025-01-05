# 🖼️ Texthidder - Secure Your Secrets in Images

Texthidder is an intuitive, GUI-based **image steganography tool** that enables users to hide and extract sensitive data within images using robust encryption techniques. Whether you're looking to safeguard sensitive messages or securely share data, Texthidder provides a beginner-friendly yet powerful solution.

---

## 🚀 Features

- **AES-128 Encryption**: Encrypt your messages before embedding them into images for added security.
- **Steganography**: Hide and retrieve text data seamlessly using image files as carriers.
- **SHA-256 Hashing**: Ensure the integrity of your data with state-of-the-art hashing.
- **Intuitive GUI**: User-friendly interface built with Python's Tkinter framework.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

---

## 📂 Project Structure

```plaintext
Texthidder/
├── README.md              # Documentation
├── main.py                # Entry point of the application
├── Gui.py                 # Main GUI logic
├── StartPage.py           # Start page implementation
├── PageOne.py             # Main functionality: hide/extract text
├── ExitPage.py            # Exit confirmation page
├── ManualPage.py          # Help and shortcuts manual
```

---

## 🛠️ Technology Stack

- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Encryption Algorithm**: AES-128
- **Hashing Algorithm**: SHA-256

---

## 🎯 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.
- Required Python libraries: `tkinter`, `Pillow` (install via `pip install pillow`).

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/premshah06/Texthidder.git
   cd Texthidder
   ```

2. **Install Dependencies**
   ```bash
   pip install pillow
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

---

## 💡 How to Use

1. **Hide Text**:
   - Navigate to the "Hide Text" tab.
   - Select an image file to embed the text.
   - Enter the text to hide and click "Hide Text."

2. **Extract Text**:
   - Switch to the "Extract Text" tab.
   - Select an image file with hidden text.
   - Click "Extract Text" to retrieve the message.

3. **Shortcuts** (Available in the Manual Page):
   - `Ctrl + A`: Select all text.
   - `Ctrl + C`: Copy text.
   - `Ctrl + V`: Paste text.
   - `Ctrl + S`: Save file.

---


**Texthidder** - Secure your secrets, one pixel at a time. 🔐✨
