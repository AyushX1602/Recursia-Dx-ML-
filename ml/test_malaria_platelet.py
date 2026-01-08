import sys
import os

# Add paths for model imports
sys.path.append(r"D:\programs vs\RecursiaDx\ml")
sys.path.append(r"D:\programs vs\RecursiaDx\ml\models")

from models.malaria_predictor import MalariaPredictor
from models.platelet_counter import PlateletCounter
from PIL import Image
import numpy as np

print("=" * 70)
print("Testing Malaria Detection and Platelet Counting Models")
print("=" * 70)

# Initialize models
print("\n1. Loading Malaria Detection Model...")
malaria_model = MalariaPredictor()

print("\n2. Loading Platelet Counting Model...")
platelet_model = PlateletCounter()

# Test samples directory
test_dir = r"D:\programs vs\RecursiaDx\TEST_SAMPLES"
test_images = [
    "1662785427-Malarial Parasite Test.webp",  # Malaria test
    "2.jpg",                                     # Platelet test
    "61466.jpg",                                 # Platelet test
    "image.png"                                  # Platelet test
]

print("\n" + "=" * 70)
print("MALARIA DETECTION TESTS")
print("=" * 70)

# Test malaria detection on all images
for img_name in test_images:
    img_path = os.path.join(test_dir, img_name)
    if not os.path.exists(img_path):
        print(f"\n❌ Image not found: {img_name}")
        continue
    
    print(f"\n📊 Testing: {img_name}")
    print("-" * 70)
    
    try:
        # Test Malaria Detection
        result = malaria_model.predict(img_path)
        
        print(f"🦠 Malaria Detection:")
        print(f"   Prediction: {result['predicted_class']}")
        print(f"   Confidence: {result['confidence']:.2%}")
        print(f"   Parasitized Probability: {result['probabilities']['parasitized']:.2%}")
        print(f"   Uninfected Probability: {result['probabilities']['uninfected']:.2%}")
        
        if result['predicted_class'] == 'Parasitized':
            print(f"   ⚠️  MALARIA DETECTED - Patient is infected!")
        else:
            print(f"   ✅ No malaria detected - Patient is healthy")
            
    except Exception as e:
        print(f"   ❌ Malaria test failed: {str(e)}")

print("\n" + "=" * 70)
print("PLATELET COUNTING TESTS")
print("=" * 70)

# Test platelet counting on all images
for img_name in test_images:
    img_path = os.path.join(test_dir, img_name)
    if not os.path.exists(img_path):
        continue
    
    print(f"\n📊 Testing: {img_name}")
    print("-" * 70)
    
    try:
        # Test Platelet Counting
        result = platelet_model.predict(img_path)
        
        print(f"🔬 Platelet Count:")
        print(f"   Total Platelets Detected: {result['counts']['Platelets']}")
        print(f"   RBC Count: {result['counts']['RBC']}")
        print(f"   WBC Count: {result['counts']['WBC']}")
        print(f"   Total Cells: {result['total_cells']}")
        print(f"   Status: {result['status']}")
        
        # Interpret platelet count
        count = result['counts']['Platelets']
        if count < 5:
            print(f"   ⚠️  LOW PLATELET COUNT (Thrombocytopenia)")
            print(f"      Normal range: 150,000-450,000 per µL")
        elif count > 450:
            print(f"   ⚠️  HIGH PLATELET COUNT (Thrombocytosis)")
            print(f"      Normal range: 150,000-450,000 per µL")
        else:
            print(f"   ✅ Platelet count appears normal")
            print(f"      Normal range: 150,000-450,000 per µL")
            
    except Exception as e:
        print(f"   ❌ Platelet count failed: {str(e)}")

print("\n" + "=" * 70)
print("COMBINED BLOOD ANALYSIS SUMMARY")
print("=" * 70)

# Run combined analysis on blood smear images
blood_smear_images = ["2.jpg", "61466.jpg", "image.png"]

for img_name in blood_smear_images:
    img_path = os.path.join(test_dir, img_name)
    if not os.path.exists(img_path):
        continue
    
    print(f"\n🩸 Blood Smear: {img_name}")
    print("-" * 70)
    
    try:
        # Get both malaria and platelet results
        malaria_result = malaria_model.predict(img_path)
        platelet_result = platelet_model.predict(img_path)
        
        print(f"📋 COMPLETE BLOOD ANALYSIS:")
        print(f"   Malaria Status: {malaria_result['predicted_class']}")
        print(f"   Malaria Confidence: {malaria_result['confidence']:.2%}")
        print(f"   Platelet Count: {platelet_result['counts']['Platelets']} detected")
        print(f"   RBC Count: {platelet_result['counts']['RBC']} detected")
        print(f"   WBC Count: {platelet_result['counts']['WBC']} detected")
        
        # Overall assessment
        if malaria_result['predicted_class'] == 'Parasitized' or platelet_result['counts']['Platelets'] < 5:
            print(f"\n   🔴 ABNORMAL FINDINGS - Further investigation required")
            if malaria_result['predicted_class'] == 'Parasitized':
                print(f"      - Malaria parasites detected")
            if platelet_result['counts']['Platelets'] < 5:
                print(f"      - Low platelet count detected")
        else:
            print(f"\n   🟢 Normal findings in both tests")
            
    except Exception as e:
        print(f"   ❌ Combined analysis failed: {str(e)}")

print("\n" + "=" * 70)
print("Testing Complete!")
print("=" * 70)
