# Enhanced GitHub Guide - Full Stack Application

## 🚀 New Features

### Frontend Enhancements
- **🌓 Dark/Light Mode**: Toggle between themes with smooth transitions
- **👤 User Accounts**: Personalized learning experience
- **📊 Progress Tracking**: Track your learning progress across sections
- **🏆 Achievements**: Earn badges as you complete sections
- **📝 Personal Notes**: Add notes to each section
- **📈 Learning Dashboard**: View your stats and progress

### Backend Features (FastAPI)
- **🔐 Authentication**: Secure JWT-based authentication
- **💾 SQLite Database**: Lightweight database for user data
- **📚 Learning Paths**: Create custom learning paths
- **🎯 Progress API**: Track and update progress
- **⚡ Fast & Modern**: Built with FastAPI for high performance

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js (optional, for advanced features)
- Git

## 🛠️ Installation & Setup

### 1. Clone/Navigate to Project
```bash
cd C:\Users\MohammadSaad\GRIHA_april_project\Claude_agent\check
```

### 2. Set Up Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the Backend Server
```bash
# From the backend directory
python main.py
```

The API will be available at: http://localhost:8000
API documentation at: http://localhost:8000/docs

### 5. Open the Frontend
Open `index.html` in your browser or use a local server:

```bash
# Option 1: Python HTTP server (from main directory)
python -m http.server 8080

# Option 2: If you have Node.js
npx http-server -p 8080
```

Then visit: http://localhost:8080

## 🎯 How to Use

### 1. Create an Account
- Click "Register" in the top right
- Enter username, email, and password
- Your account will be created automatically

### 2. Login
- Click "Login" with your credentials
- Your progress will be saved automatically

### 3. Personalized Learning
- Navigate through sections
- Your progress is tracked automatically
- Add personal notes to each section
- Mark sections as complete
- View your dashboard for overall progress

### 4. Theme Preference
- Click the moon/sun icon to toggle dark/light mode
- Your preference is saved to your account

## 📁 Project Structure

```
check/
├── index.html              # Enhanced frontend with auth & dark mode
├── backend/
│   ├── main.py            # FastAPI backend server
│   ├── requirements.txt   # Python dependencies
│   └── github_guide.db    # SQLite database (created automatically)
├── github-guide.html      # Original static version
└── .github/
    └── workflows/         # CI/CD pipelines
```

## 🔧 API Endpoints

- `POST /register` - Create new user account
- `POST /token` - Login and get access token
- `GET /me` - Get current user info
- `PUT /preferences` - Update user preferences
- `GET /progress` - Get user's learning progress
- `PUT /progress` - Update section progress
- `GET /stats` - Get user statistics
- `GET /achievements` - Get user achievements

## 🌐 Deployment Options

### Deploy Frontend to GitHub Pages
1. Push all files to GitHub
2. Enable GitHub Pages in settings
3. Your static site will be live

### Deploy Backend (Options)
1. **Heroku** (Free tier available)
   ```bash
   # Create Procfile
   echo "web: uvicorn backend.main:app --host=0.0.0.0 --port=${PORT:-5000}" > Procfile
   ```

2. **Railway.app** (Simple deployment)
   - Connect GitHub repo
   - Railway will auto-detect FastAPI

3. **Render.com** (Free tier)
   - Create new Web Service
   - Connect GitHub repo
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host=0.0.0.0 --port=$PORT`

## 🔒 Security Notes

For production deployment:
1. Change the `SECRET_KEY` in `main.py`
2. Update CORS settings to specific domains
3. Use environment variables for sensitive data
4. Enable HTTPS
5. Use a production database (PostgreSQL)

## 🐛 Troubleshooting

### Backend won't start
- Ensure all dependencies are installed
- Check Python version (3.8+)
- Make sure port 8000 is not in use

### Frontend can't connect to backend
- Check CORS settings
- Ensure backend is running
- Verify API_URL in frontend matches backend URL

### Database errors
- Delete `github_guide.db` and restart server
- The database will be recreated automatically

## 🚀 Next Steps

1. **Add OAuth**: Integrate GitHub OAuth for login
2. **Email Notifications**: Send progress reports
3. **Collaborative Features**: Share learning paths
4. **Mobile App**: Create React Native version
5. **Advanced Analytics**: Detailed learning insights

## 📝 License

This project is open source and available under the MIT License.

---

Happy Learning! 🎉 Your personalized GitHub learning journey starts here!