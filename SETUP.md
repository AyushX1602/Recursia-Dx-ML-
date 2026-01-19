# RecursiaDx Setup Guide

Complete setup instructions for running the RecursiaDx platform locally.

---

## Prerequisites

Before starting, ensure you have:
- **Node.js 18+** ([Download](https://nodejs.org))
- **Python 3.10+** ([Download](https://www.python.org))
- **MongoDB** (local or Atlas account)
- **Git** ([Download](https://git-scm.com))

---

## 1. Clone Repository

```bash
git clone https://github.com/AyushX1602/Recursia-Dx-ML-.git
cd RecursiaDx
```

---

## 2. Backend Setup

```bash
cd backend
npm install
```

### Configure Environment Variables
Create `.env` file in `backend/` folder:

```env
# MongoDB Connection
MONGODB_URI=mongodb://localhost:27017/recursiadx
PORT=5001

# ML Service URLs
ML_SERVICE_URL=http://localhost:5000
GIGAPATH_SERVICE_URL=http://localhost:5002

# Gemini AI (Optional - for AI reports)
GEMINI_API_KEY=your_gemini_api_key_here

# CORS
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

**Get Gemini API Key (Free):**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy and paste into `.env` file

---

## 3. Frontend Setup

```bash
cd ../client
npm install
```

---

## 4. ML Setup

### Install Python Dependencies

```bash
cd ../ml/api
pip install -r requirements.txt
```

### Download Model Files

**You need to download the ML model files separately** (not in git due to size):

1. **GigaPath Model** (~300MB)
   - Place at: `GigaPath-AI-WSI-Breast-Cancer-Lesion-Analysis/checkpoints/best_model.pth`

2. **Malaria Model** (~95MB)
   - Place at: `Malaria-Disease-Detection-Using-Transfer-Learning/InceptionV3_Malaria_PyTorch.pth`

3. **YOLOv11 Platelet Model** (~22MB)
   - Place at: `Platelates/yolo11n.pt`

**Contact the repository owner for model files.**

---

## 5. Start All Services

### Option 1: Windows Batch Script (Easiest)

```bash
cd ../../  # Back to root
.\start_all.bat
```

This will open 4 terminal windows:
- Frontend (Port 5173)
- Backend (Port 5001)
- Tissue ML API (Port 5002)
- Blood ML API (Port 5000)

### Option 2: Manual Start (4 separate terminals)

**Terminal 1 - Frontend:**
```bash
cd client
npm run dev
```

**Terminal 2 - Backend:**
```bash
cd backend
node server.js
```

**Terminal 3 - Tissue ML (GigaPath):**
```bash
cd ml/api
python gigapath_api.py
```

**Terminal 4 - Blood ML (Malaria + Platelet):**
```bash
cd ml/api
python app.py
```

---

## 6. Access Application

Open your browser and navigate to:
```
http://localhost:5173
```

**Default Demo Access:**
- Use "Demo Mode" button on homepage
- Or create an account

---

## Troubleshooting

### MongoDB Connection Error
```
Error: ECONNREFUSED mongodb://localhost:27017
```
**Solution:** Start MongoDB service
- Windows: `net start MongoDB`
- Mac: `brew services start mongodb-community`
- Or use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (free tier)

### Puppeteer Chrome Download Failed
```
Error: Failed to launch the browser process
```
**Solution:**
```bash
cd backend
npx puppeteer install
```

### ML Model Not Found
```
Error: Model file not found at path...
```
**Solution:** Download model files (see Step 4) or contact repository owner.

### Port Already in Use
```
Error: Port 5001 is already in use
```
**Solution:** Kill the process using that port
```bash
# Windows
netstat -ano | findstr :5001
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5001 | xargs kill -9
```

### Gemini API Rate Limit
```
Error: 429 Too Many Requests
```
**Solution:** 
- Wait 60 seconds and retry
- Free tier has 5 requests/minute limit
- System works with fallback summaries without Gemini

---

## Features

- ✅ AI-powered tissue tumor detection (GigaPath)
- ✅ Malaria parasite detection (InceptionV3)
- ✅ Automated platelet counting (YOLOv11)
- ✅ Gemini AI-generated clinical reports
- ✅ Professional PDF report download
- ✅ 5-step clinical workflow
- ✅ Demo mode for testing

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 18 + Vite + Tailwind CSS |
| Backend | Node.js + Express + MongoDB |
| ML | Python + PyTorch + GigaPath + YOLO |
| AI | Google Gemini 2.5 Flash |

---

## Project Structure

```
RecursiaDx/
├── backend/          # Node.js API server
│   ├── models/      # MongoDB schemas
│   ├── routes/      # API endpoints
│   ├── services/    # Gemini integration
│   └── server.js    # Entry point
├── client/          # React frontend
│   └── src/
│       └── components/
├── ml/              # ML services
│   └── api/
│       ├── app.py            # Blood analysis
│       └── gigapath_api.py   # Tissue analysis
├── start_all.bat    # Windows startup script
└── README.md
```

---

## Support

For issues or questions:
1. Check [README.md](README.md)
2. Review [STARTUP_GUIDE.md](STARTUP_GUIDE.md)  
3. Open a GitHub issue

---

## License

Educational and research purposes only.

---

**Status**: ✅ Production Ready

Enjoy using RecursiaDx! 🚀
