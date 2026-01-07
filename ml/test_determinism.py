import requests
import time

# Test the ML API
url = "http://localhost:5000/predict"

# Create a test by uploading the same image multiple times
test_image_path = r"D:\programs vs\RecursiaDx\backend\uploads\images-1767769638871-653683062.jpg"

print("Testing ML Model Determinism")
print("=" * 70)
print(f"Test image: {test_image_path}")
print("\nRunning 5 predictions on the same image...")
print("=" * 70)

results = []
for i in range(5):
    with open(test_image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        data = response.json()
        tumor_prob = data['results']['probabilities']['tumor']
        predicted = data['results']['predicted_class']
        confidence = data['results']['confidence']
        
        results.append(tumor_prob)
        print(f"Run {i+1}: {predicted:12} | Tumor: {tumor_prob:.6f} | Confidence: {confidence:.4f}")
    else:
        print(f"Run {i+1}: ERROR - {response.status_code}")
    
    time.sleep(0.1)

print("\n" + "=" * 70)
print("Results Analysis:")
print("=" * 70)
print(f"All predictions identical: {len(set(results)) == 1}")
print(f"Tumor probability range: {min(results):.6f} - {max(results):.6f}")
print(f"Standard deviation: {sum([(x - sum(results)/len(results))**2 for x in results])/len(results):.10f}")

if len(set(results)) == 1:
    print("\n✅ Model is DETERMINISTIC - Same input always gives same output")
    print(f"   Consistent prediction: Tumor probability = {results[0]:.6f}")
else:
    print("\n❌ Model is NON-DETERMINISTIC - Predictions vary!")
    print("   This indicates random behavior in the model")
