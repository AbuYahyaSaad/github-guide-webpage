# GitHub Guide Webpage - Enhanced Edition 🚀

![CI/CD Pipeline](https://github.com/YOUR_USERNAME/github-guide-webpage/actions/workflows/simple-cicd.yml/badge.svg)
![Deploy Status](https://github.com/YOUR_USERNAME/github-guide-webpage/actions/workflows/deploy.yml/badge.svg)
![Quality Check](https://github.com/YOUR_USERNAME/github-guide-webpage/actions/workflows/quality-check.yml/badge.svg)

A comprehensive, interactive webpage for learning GitHub with **personalized accounts**, **dark/light mode**, and **progress tracking**.

## ✨ New Features

### 🌓 Dark/Light Mode
- Toggle between themes with smooth transitions
- Preference saved to user account
- Automatic theme detection

### 👤 User Accounts (Powered by FastAPI)
- Secure authentication with JWT tokens
- Personalized learning experience
- Progress saved across sessions

### 📊 Learning Analytics
- Track progress for each section
- Overall completion percentage
- Learning streak tracking
- Achievement system

### 📝 Personal Notes
- Add notes to any section
- Notes saved to your account
- Export notes feature (coming soon)

## 🚀 Quick Start

### Easiest Way (Windows):
```bash
# Just double-click!
start.bat
```

### Manual Setup:
1. **Install Python 3.8+**
2. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. **Run backend:**
   ```bash
   python main.py
   ```
4. **Open frontend:**
   Open `index.html` in your browser

## 📁 Project Structure

```
github-guide-webpage/
├── 🎨 Frontend
│   ├── index.html          # Enhanced UI with auth
│   ├── github-guide.html   # Original static version
│   ├── github-styles.css   # Additional styles
│   └── github-interactive.js
│
├── ⚡ Backend (FastAPI)
│   ├── backend/
│   │   ├── main.py        # API server
│   │   └── requirements.txt
│   └── github_guide.db    # User database
│
├── 🚀 Automation
│   ├── .github/workflows/ # CI/CD pipelines
│   └── start.bat         # Quick start script
│
└── 📚 Documentation
    ├── README.md         # This file
    ├── SETUP_GUIDE.md    # Detailed setup
    └── DEPLOYMENT.md     # Deploy to cloud
```

## Features

### 🎯 Main Sections

1. **Basics** - Introduction to GitHub concepts
   - What is GitHub?
   - Key terminology (repositories, branches, commits, pull requests)
   - Visual feature cards

2. **Setup** - Getting started with Git and GitHub
   - Installation instructions
   - Configuration commands
   - SSH key setup
   - Account creation guide

3. **Commands** - Essential Git commands reference
   - Basic commands (init, clone, add, commit, push, pull)
   - Branch management commands
   - Advanced commands (rebase, cherry-pick, stash)

4. **Workflow** - Standard Git workflow
   - Visual workflow diagram
   - Step-by-step process
   - Best practices

5. **Collaboration** - Working with teams
   - Pull requests
   - Issues tracking
   - Code review process

6. **Advanced** - Advanced GitHub features
   - GitHub Actions (CI/CD)
   - GitHub Pages
   - Security features

### 🚀 Interactive Features

- **Navigation Buttons**: Easy section switching
- **Copy Commands**: Click to copy Git commands to clipboard
- **Action Buttons**: Various interactive buttons for different actions
- **Alert System**: Visual feedback for user actions
- **Responsive Design**: Works on desktop and mobile devices
- **Keyboard Navigation**: Press 1-6 to jump to sections

### 📁 Files Structure

```
check/
├── github-guide.html      # Main HTML file
├── github-styles.css      # Additional styling
├── github-interactive.js  # Enhanced JavaScript features
└── README.md             # This file
```

## How to Use

1. **Open the webpage**: Double-click `github-guide.html` or open it in a web browser
2. **Navigate sections**: Use the top navigation buttons or keyboard shortcuts (1-6)
3. **Interactive elements**:
   - Click buttons to simulate actions
   - Hover over cards for effects
   - Copy commands by clicking on them

## Customization

You can customize the webpage by:
- Editing the HTML content in `github-guide.html`
- Modifying styles in the embedded CSS or `github-styles.css`
- Adding more interactive features in `github-interactive.js`

## Browser Compatibility

Works best in modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Future Enhancements

Potential additions:
- Dark mode toggle
- Search functionality
- Interactive Git simulator
- Video tutorials integration
- Quiz/assessment section
- Bookmark favorite commands

## Notes

- All Git commands shown are real and can be used in your terminal
- The webpage is self-contained and works offline
- No external dependencies required

---

Created for learning GitHub effectively with an interactive, user-friendly interface.