import sys
sys.path.append(r"D:\programs vs\RecursiaDx\ml")

from models.tumor_predictor import TumorPredictor
from PIL import Image
import numpy as np

print("Testing TumorPredictor with actual trained model")
print("=" * 70)

# Initialize predictor
model_path = r"D:\programs vs\RecursiaDx\ml\models\__pycache__\best_resnet50_model.pth"
predictor = TumorPredictor(model_path=model_path)

# Test image
test_image = r"D:\programs vs\RecursiaDx\backend\uploads\images-1767769638871-653683062.jpg"

print(f"\nTest image: {test_image}")
print("\nRunning 5 predictions to test determinism...")
print("=" * 70)

results = []
for i in range(5):
    result = predictor.predict(test_image)
    tumor_prob = result['probabilities']['tumor']
    results.append(tumor_prob)
    print(f"Run {i+1}: {result['predicted_class']:12} | Tumor: {tumor_prob:.8f} | Conf: {result['confidence']:.4f}")

print("\n" + "=" * 70)
print("Determinism Check:")
print("=" * 70)
print(f"All identical: {len(set(results)) == 1}")
print(f"Range: {min(results):.8f} - {max(results):.8f}")

if len(set(results)) == 1:
    print("\n✅ Model is DETERMINISTIC")
    print(f"   Tumor probability: {results[0]:.8f}")
    
    # Interpret the result
    if results[0] >= 0.5:
        print(f"\n🔴 TUMOR DETECTED (probability >= 50%)")
    else:
        print(f"\n🟢 NON-TUMOR (probability < 50%)")
        print(f"   This means the model predicts NORMAL/HEALTHY tissue")
else:
    print("\n❌ Model is NON-DETERMINISTIC!")

# Test with a different image if available
print("\n" + "=" * 70)
print("Testing with different image types:")
print("=" * 70)

# Create a simple test image (white square)
white_img = Image.new('RGB', (224, 224), color='white')
result_white = predictor.predict(white_img)
print(f"White image:  Tumor prob = {result_white['probabilities']['tumor']:.8f}")

# Black image
black_img = Image.new('RGB', (224, 224), color='black')
result_black = predictor.predict(black_img)
print(f"Black image:  Tumor prob = {result_black['probabilities']['tumor']:.8f}")

# Random noise
np.random.seed(42)
noise_img = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
result_noise = predictor.predict(noise_img)
print(f"Random noise: Tumor prob = {result_noise['probabilities']['tumor']:.8f}")

print("\n" + "=" * 70)
print("Model Analysis:")
print("=" * 70)

if (result_white['probabilities']['tumor'] == result_black['probabilities']['tumor'] == 
    result_noise['probabilities']['tumor']):
    print("⚠️  WARNING: Model gives SAME output for all inputs!")
    print("   This suggests the model is NOT properly trained.")
    print("   All images get the same prediction regardless of content.")
else:
    print("✅ Model distinguishes between different inputs")
    print("   The model is working and trained.")
