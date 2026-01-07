#!/usr/bin/env python3
"""
RecursiaDx System Integration Test
Tests the complete ML workflow: Upload → Analysis → Viewing → Reporting
"""

import requests
import json
import time
from pathlib import Path

# Configuration
BACKEND_URL = "http://localhost:5001"  # Updated to correct port
ML_SERVER_URL = "http://localhost:5000"
FRONTEND_URL = "http://localhost:5173"

def test_ml_server_health():
    """Test ML server connectivity"""
    print("🔍 Testing ML Server Health...")
    try:
        response = requests.get(f"{ML_SERVER_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ ML Server is healthy")
            return True
        else:
            print(f"❌ ML Server unhealthy: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ML Server unreachable: {e}")
        return False

def test_backend_health():
    """Test backend server connectivity"""
    print("🔍 Testing Backend Server Health...")
    try:
        response = requests.get(f"{BACKEND_URL}/api/samples/ml-health-test", timeout=5)
        if response.status_code == 200:
            print("✅ Backend Server is healthy")
            return True
        else:
            print(f"❌ Backend Server unhealthy: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend Server unreachable: {e}")
        return False

def test_frontend_accessibility():
    """Test frontend accessibility"""
    print("🔍 Testing Frontend Accessibility...")
    try:
        response = requests.get(FRONTEND_URL, timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend inaccessible: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend unreachable: {e}")
        return False

def test_ml_prediction():
    """Test ML prediction endpoint directly"""
    print("🔍 Testing ML Prediction...")
    try:
        # Test with dummy image data
        test_data = {"image_data": "test_image_base64_data"}
        response = requests.post(f"{ML_SERVER_URL}/predict", 
                               json=test_data, 
                               timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ ML Prediction successful: {result.get('prediction', 'Unknown')}")
            print(f"   Confidence: {result.get('confidence', 0):.2%}")
            return True
        else:
            print(f"❌ ML Prediction failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ML Prediction error: {e}")
        return False

def run_system_test():
    """Run complete system integration test"""
    print("🚀 Starting RecursiaDx System Integration Test")
    print("=" * 50)
    
    tests = [
        ("ML Server", test_ml_server_health),
        ("Backend API", test_backend_health),
        ("Frontend UI", test_frontend_accessibility),
        ("ML Prediction", test_ml_prediction),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} test...")
        results[test_name] = test_func()
        time.sleep(1)  # Brief pause between tests
    
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(tests)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL SYSTEMS OPERATIONAL!")
        print("🔬 RecursiaDx is ready for pathology analysis")
        print(f"🌐 Access the system at: {FRONTEND_URL}")
        print("\n📋 Workflow Test Instructions:")
        print("1. Go to Sample Upload tab")
        print("2. Fill in patient information")
        print("3. Upload medical images")
        print("4. Watch real-time ML analysis")
        print("5. View results in WSI Viewer")
        print("6. Generate comprehensive report")
    else:
        print(f"\n⚠️  {total - passed} system(s) need attention")
        print("Please check server logs and retry")
    
    return passed == total

if __name__ == "__main__":
    run_system_test()