# FastAPI Backend for GitHub Guide

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
import sqlite3
import json
from contextlib import contextmanager

# Configuration
SECRET_KEY = "your-secret-key-here-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI
app = FastAPI(title="GitHub Guide API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database setup
@contextmanager
def get_db():
    conn = sqlite3.connect("github_guide.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# Initialize database
def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                hashed_password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                preferences TEXT DEFAULT '{}',
                is_active BOOLEAN DEFAULT 1
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                section TEXT NOT NULL,
                progress INTEGER DEFAULT 0,
                completed BOOLEAN DEFAULT 0,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id),
                UNIQUE(user_id, section)
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS learning_paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                path_name TEXT NOT NULL,
                path_data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                achievement_type TEXT NOT NULL,
                achievement_data TEXT,
                earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        conn.commit()

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    preferences: Dict
    is_active: bool

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserPreferences(BaseModel):
    theme: str = "light"
    font_size: str = "medium"
    learning_pace: str = "normal"
    email_notifications: bool = True

class ProgressUpdate(BaseModel):
    section: str
    progress: int
    completed: bool = False
    notes: Optional[str] = None

class LearningPath(BaseModel):
    path_name: str
    sections: List[str]
    difficulty: str

class Achievement(BaseModel):
    type: str
    data: Dict

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user(username: str):
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        )
        user = cursor.fetchone()
        if user:
            return UserInDB(
                id=user["id"],
                username=user["username"],
                email=user["email"],
                hashed_password=user["hashed_password"],
                created_at=user["created_at"],
                preferences=json.loads(user["preferences"]),
                is_active=user["is_active"]
            )
    return None

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "GitHub Guide API", "version": "1.0.0"}

@app.post("/register", response_model=User)
async def register(user: UserCreate):
    # Check if user exists
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT id FROM users WHERE username = ? OR email = ?",
            (user.username, user.email)
        )
        if cursor.fetchone():
            raise HTTPException(
                status_code=400,
                detail="Username or email already registered"
            )
        
        # Create new user
        hashed_password = get_password_hash(user.password)
        cursor = conn.execute(
            """INSERT INTO users (username, email, hashed_password, preferences)
               VALUES (?, ?, ?, ?)""",
            (user.username, user.email, hashed_password, json.dumps({}))
        )
        conn.commit()
        user_id = cursor.lastrowid
        
        # Initialize progress for all sections
        sections = ["basics", "setup", "commands", "workflow", "collaboration", "advanced"]
        for section in sections:
            conn.execute(
                """INSERT INTO user_progress (user_id, section, progress)
                   VALUES (?, ?, 0)""",
                (user_id, section)
            )
        conn.commit()
        
        return User(
            id=user_id,
            username=user.username,
            email=user.email,
            created_at=datetime.utcnow(),
            preferences={},
            is_active=True
        )

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.put("/preferences")
async def update_preferences(
    preferences: UserPreferences,
    current_user: User = Depends(get_current_user)
):
    with get_db() as conn:
        conn.execute(
            "UPDATE users SET preferences = ? WHERE id = ?",
            (json.dumps(preferences.dict()), current_user.id)
        )
        conn.commit()
    return {"message": "Preferences updated successfully"}

@app.get("/progress")
async def get_progress(current_user: User = Depends(get_current_user)):
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM user_progress WHERE user_id = ?",
            (current_user.id,)
        )
        progress = cursor.fetchall()
        return [dict(row) for row in progress]

@app.put("/progress")
async def update_progress(
    progress: ProgressUpdate,
    current_user: User = Depends(get_current_user)
):
    with get_db() as conn:
        conn.execute(
            """INSERT OR REPLACE INTO user_progress 
               (user_id, section, progress, completed, notes, last_accessed)
               VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)""",
            (current_user.id, progress.section, progress.progress,
             progress.completed, progress.notes)
        )
        conn.commit()
        
        # Check for achievements
        check_achievements(current_user.id, progress)
        
    return {"message": "Progress updated successfully"}

@app.get("/learning-paths")
async def get_learning_paths(current_user: User = Depends(get_current_user)):
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM learning_paths WHERE user_id = ?",
            (current_user.id,)
        )
        paths = cursor.fetchall()
        return [dict(row) for row in paths]

@app.post("/learning-paths")
async def create_learning_path(
    path: LearningPath,
    current_user: User = Depends(get_current_user)
):
    with get_db() as conn:
        cursor = conn.execute(
            """INSERT INTO learning_paths (user_id, path_name, path_data)
               VALUES (?, ?, ?)""",
            (current_user.id, path.path_name, json.dumps(path.dict()))
        )
        conn.commit()
        return {"id": cursor.lastrowid, "message": "Learning path created"}

@app.get("/achievements")
async def get_achievements(current_user: User = Depends(get_current_user)):
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM achievements WHERE user_id = ?",
            (current_user.id,)
        )
        achievements = cursor.fetchall()
        return [dict(row) for row in achievements]

@app.get("/stats")
async def get_user_stats(current_user: User = Depends(get_current_user)):
    with get_db() as conn:
        # Get overall progress
        cursor = conn.execute(
            """SELECT AVG(progress) as avg_progress,
                      COUNT(CASE WHEN completed = 1 THEN 1 END) as completed_sections,
                      COUNT(*) as total_sections
               FROM user_progress WHERE user_id = ?""",
            (current_user.id,)
        )
        progress_stats = dict(cursor.fetchone())
        
        # Get achievements count
        cursor = conn.execute(
            "SELECT COUNT(*) as total_achievements FROM achievements WHERE user_id = ?",
            (current_user.id,)
        )
        achievement_count = cursor.fetchone()["total_achievements"]
        
        # Get learning streak (simplified)
        cursor = conn.execute(
            """SELECT julianday('now') - julianday(MAX(last_accessed)) as days_since_last_visit
               FROM user_progress WHERE user_id = ?""",
            (current_user.id,)
        )
        days_since = cursor.fetchone()["days_since_last_visit"] or 0
        
        return {
            "overall_progress": progress_stats["avg_progress"] or 0,
            "completed_sections": progress_stats["completed_sections"],
            "total_sections": progress_stats["total_sections"],
            "achievements": achievement_count,
            "learning_streak": 1 if days_since < 2 else 0,
            "member_since": current_user.created_at
        }

# Helper function to check achievements
def check_achievements(user_id: int, progress: ProgressUpdate):
    with get_db() as conn:
        # Check if first section completed
        if progress.completed and progress.progress >= 100:
            cursor = conn.execute(
                """SELECT COUNT(*) as count FROM achievements 
                   WHERE user_id = ? AND achievement_type = 'first_section_complete'""",
                (user_id,)
            )
            if cursor.fetchone()["count"] == 0:
                conn.execute(
                    """INSERT INTO achievements (user_id, achievement_type, achievement_data)
                       VALUES (?, ?, ?)""",
                    (user_id, "first_section_complete", json.dumps({"section": progress.section}))
                )
                conn.commit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)