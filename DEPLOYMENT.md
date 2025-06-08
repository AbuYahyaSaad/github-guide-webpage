# Deployment Configuration for Enhanced GitHub Guide

## Option 1: Deploy to Render.com (Recommended - Free Tier)

### Backend Deployment (FastAPI)

1. Create `render.yaml` in root directory:

```yaml
services:
  - type: web
    name: github-guide-api
    env: python
    buildCommand: "pip install -r backend/requirements.txt"
    startCommand: "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: SECRET_KEY
        generateValue: true
```

2. Push to GitHub
3. Connect GitHub repo to Render
4. Deploy automatically

### Frontend Deployment

1. Update `API_URL` in index.html to your Render backend URL
2. Deploy to GitHub Pages or Netlify

## Option 2: Local Development with Ngrok

1. Install ngrok: https://ngrok.com/
2. Run backend locally
3. Expose backend with ngrok:
   ```bash
   ngrok http 8000
   ```
4. Update frontend API_URL to ngrok URL

## Option 3: Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    environment:
      - SECRET_KEY=your-secret-key-here

  frontend:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./:/usr/share/nginx/html
```

## Environment Variables

Create `.env` file:

```
SECRET_KEY=your-super-secret-key-change-this
DATABASE_URL=sqlite:///./github_guide.db
CORS_ORIGINS=["http://localhost:8080", "https://yourdomain.com"]
```

## Production Checklist

- [ ] Change SECRET_KEY
- [ ] Update CORS origins
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Configure logging
- [ ] Add rate limiting
- [ ] Set up monitoring

## Quick Deploy Commands

```bash
# Heroku
heroku create your-app-name
heroku buildpacks:set heroku/python
git push heroku main

# Railway
railway login
railway init
railway up

# Fly.io
fly launch
fly deploy
```