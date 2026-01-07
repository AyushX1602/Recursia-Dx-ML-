#!/usr/bin/env python3
"""
Quick test script to verify ML server and model availability
"""

import os
import sys

def test_model_file():
    """Check if model file exists"""
    model_path = os.path.join(os.path.dirname(__file__), 'models', '__pycache__', 'best_resnet50_model.pth')
    print(f"Checking for model at: {model_path}")
    
    if os.path.exists(model_path):
        file_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
        print(f"✅ Model file found! Size: {file_size:.2f} MB")
        return True
    else:
        print(f"❌ Model file NOT found!")
        print(f"Expected location: {model_path}")
        return False

def test_imports():
    """Test if all required modules can be imported"""
    print("\nTesting imports...")
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except ImportError as e:
        print(f"❌ PyTorch import failed: {e}")
        return False
    
    try:
        from torchvision import models
        print(f"✅ torchvision")
    except ImportError as e:
        print(f"❌ torchvision import failed: {e}")
        return False
    
    try:
        from flask import Flask
        print(f"✅ Flask")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print(f"✅ PIL/Pillow")
    except ImportError as e:
        print(f"❌ PIL import failed: {e}")
        return False
    
    return True

def test_model_loading():
    """Test if model can be loaded"""
    print("\nTesting model loading...")
    
    try:
        sys.path.append(os.path.dirname(__file__))
        from models.tumor_predictor import TumorPredictor
        
        model_path = os.path.join(os.path.dirname(__file__), 'models', '__pycache__', 'best_resnet50_model.pth')
        
        if not os.path.exists(model_path):
            print("❌ Cannot test loading - model file not found")
            return False
        
        predictor = TumorPredictor()
        predictor.load_model(model_path)
        print("✅ Model loaded successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 70)
    print("RecursiaDx ML Server Test")
    print("=" * 70)
    
    results = []
    
    # Test 1: Model file
    results.append(("Model File", test_model_file()))
    
    # Test 2: Imports
    results.append(("Imports", test_imports()))
    
    # Test 3: Model loading
    results.append(("Model Loading", test_model_loading()))
    
    # Summary
    print("\n" + "=" * 70)
    print("Test Summary:")
    print("=" * 70)
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{name:.<40} {status}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n✅ All tests passed! ML server should start successfully.")
        print("\nTo start the ML server, run:")
        print("  cd ml")
        print("  python api/app.py")
    else:
        print("\n❌ Some tests failed. Please fix the issues before starting the server.")
        sys.exit(1)
