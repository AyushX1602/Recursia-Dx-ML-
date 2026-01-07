# RecursiaDx Startup Guide

## Prerequisites Check

Before starting, verify the ML model is available:

```bash
cd ml
python test_server.py
```

This will check:
- ✅ Model file exists (`models/__pycache__/best_resnet50_model.pth`)
- ✅ All Python dependencies are installed
- ✅ Model can be loaded successfully

---

## Starting the Complete System

### Step 1: Start the ML Server (Port 5000)

```bash
cd ml
python api/app.py
```

**Expected output:**
```
✅ Found trained model at: ...best_resnet50_model.pth
✅ Pre-trained model loaded successfully
✅ Histopathology pipeline initialized
✅ Server initialization successful
🚀 Starting server on port 5000...
```

**Health check:**
```bash
curl http://localhost:5000/health
```

Should return:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "pipeline_loaded": true
}
```

---

### Step 2: Start the Backend Server (Port 5001)

Open a **new terminal**:

```bash
cd backend
node server.js
```

**Expected output:**
```
🚀 Server started on port 5001
📊 MongoDB connected successfully
```

---

### Step 3: Start the Frontend (Port 5173)

Open a **new terminal**:

```bash
cd client
npm run dev
```

**Expected output:**
```
VITE ready in ...ms
➜  Local:   http://localhost:5173/
```

---

## System Status

| Component | Port | Status Check |
|-----------|------|--------------|
| ML Server | 5000 | http://localhost:5000/health |
| Backend API | 5001 | http://localhost:5001 |
| Frontend | 5173 | http://localhost:5173 |

---

## Important Changes

### ✅ What's New:
1. **Real ML Analysis** - Uses trained ResNet50 model
2. **Real Heatmap Generation** - Patch-based analysis, no random data
3. **No Mock Data** - If ML server is down, uploads will fail (proper error handling)

### ❌ What's Removed:
1. Random heatmap selection
2. Mock prediction results
3. Fake data fallbacks

### ⚠️ Critical:
- **ML server MUST be running** for image uploads to work
- Without ML server, you'll see: "ML service is not available"
- This is intentional - no fake results anymore!

---

## Troubleshooting

### ML Server Won't Start

**Issue:** "Model file not found"
**Solution:** 
```bash
# Verify model exists
ls ml/models/__pycache__/*.pth

# Should show:
# best_resnet50_model.pth
# best_resnet50_malaria_model.pth
# best_efficientnet_bloodcell_model.pth
```

### Backend Can't Connect to ML

**Issue:** "ML service is not available"
**Solution:**
1. Check ML server is running: `curl http://localhost:5000/health`
2. Check firewall settings
3. Restart ML server

### Uploads Fail

**Issue:** "ML analysis failed"
**Solution:**
1. Check ML server logs for errors
2. Verify image format (JPG, PNG, TIFF, BMP)
3. Check image size (max 50MB)

---

## Testing the System

### 1. Test ML Server Directly:

```python
# test_ml_direct.py
import requests

# Test health
response = requests.get('http://localhost:5000/health')
print(response.json())

# Test prediction
with open('test_image.jpg', 'rb') as f:
    files = {'image': f}
    response = requests.post('http://localhost:5000/predict', files=files)
    print(response.json())
```

### 2. Test Backend ML Integration:

```bash
curl http://localhost:5001/api/samples/ml-health-test
```

### 3. Test Complete Flow:

1. Go to http://localhost:5173
2. Login/Register
3. Upload a sample with images
4. Check that ML analysis runs (takes 10-30 seconds)
5. View heatmaps in WSI Viewer

---

## Performance Notes

- **Single Image:** ~2-5 seconds (depends on size)
- **Batch (5 images):** ~10-25 seconds
- **Heatmap Generation:** ~5-15 seconds per image

Large images are processed in patches for detailed analysis.

---

## Quick Commands

```bash
# Check all services
curl http://localhost:5000/health  # ML
curl http://localhost:5001/        # Backend
curl http://localhost:5173/        # Frontend

# View ML logs
cd ml && python api/app.py

# View backend logs
cd backend && node server.js

# Restart all (PowerShell)
# Press Ctrl+C in each terminal, then restart
```
