# Model Setup Guide

## Quick Start

After cloning the repository, the model files need to be set up:

### Option 1: Models Already Included (Platelet Only)
The platelet detection models are included via Git LFS:
- ✅ `Platelates/runs/detect/bccd_blood_cells/weights/best.pt`
- ✅ `Platelates/yolo11n.pt`
- ✅ `Platelates/yolov8s.pt`

### Option 2: Download Missing Models

The GigaPath and Malaria models are NOT included in the repository due to size constraints.

#### Required Models

| Model | Size | Location | Status |
|-------|------|----------|--------|
| GigaPath (best_model.pth) | ~27MB | `GigaPath-AI-WSI-Breast-Cancer-Lesion-Analysis/checkpoints/` | ❌ Not included |
| GigaPath (last_model.pth) | ~27MB | `GigaPath-AI-WSI-Breast-Cancer-Lesion-Analysis/checkpoints/` | ❌ Not included |
| Malaria (InceptionV3) | ~85MB | `Malaria-Disease-Detection-Using-Transfer-Learning/` | ❌ Not included |
| Platelet (YOLOv8) | ~22MB each | `Platelates/runs/detect/bccd_blood_cells/weights/` | ✅ Included via LFS |

---

## Setup Instructions

### 1. Install Git LFS (if not already installed)

```bash
# Windows (using Chocolatey)
choco install git-lfs

# macOS
brew install git-lfs

# Linux (Debian/Ubuntu)
sudo apt-get install git-lfs

# Initialize LFS
git lfs install
```

### 2. Clone with LFS

```bash
git clone https://github.com/AyushX1602/Recursia-Dx-ML-.git
cd Recursia-Dx-ML-
git lfs pull  # Download LFS files
```

### 3. Download Missing Models

**Contact the repository owner** to obtain:
- `best_model.pth` and `last_model.pth` (GigaPath checkpoints)
- `InceptionV3_Malaria_PyTorch.pth` (Malaria model)

Place them in the correct directories as shown in the table above.

---

## Verification

Run this to verify models are in place:

```bash
# Check GigaPath models
ls GigaPath-AI-WSI-Breast-Cancer-Lesion-Analysis/checkpoints/

# Check Malaria model
ls Malaria-Disease-Detection-Using-Transfer-Learning/InceptionV3_Malaria_PyTorch.pth

# Check Platelet models
ls Platelates/runs/detect/bccd_blood_cells/weights/
```

---

## Alternative: Train Your Own Models

If you cannot obtain the pre-trained models, you can train them yourself:

### GigaPath Model
See `GigaPath-AI-WSI-Breast-Cancer-Lesion-Analysis/README.md` for training instructions.

### Malaria Model
See `Malaria-Disease-Detection-Using-Transfer-Learning/README.md` for training instructions.

### Platelet Model
See `Platelates/README.md` for training instructions.

---

## Troubleshooting

### "Checkpoint not found" error
- Ensure model files are in the correct directories
- Check file names match exactly (case-sensitive)
- Verify Git LFS is installed and initialized

### Git LFS not downloading files
```bash
git lfs install
git lfs pull
```

### Models too large for GitHub
The models are configured for Git LFS, which supports files up to 2GB per file.
