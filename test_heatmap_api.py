import requests
import json
import os

def test_heatmap_api():
    """Test the heatmap generation API."""
    
    # Create a test image if it doesn't exist
    test_image_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'uploads', 'test_image.jpg')
    
    if not os.path.exists(test_image_path):
        print("Creating test image...")
        from PIL import Image, ImageDraw
        import numpy as np
        
        # Create a simple test image
        img = Image.new('RGB', (512, 512), color='white')
        draw = ImageDraw.Draw(img)
        
        # Add some colored regions
        for i in range(10):
            x = np.random.randint(0, 400)
            y = np.random.randint(0, 400)
            w = np.random.randint(50, 100)
            h = np.random.randint(50, 100)
            color = (np.random.randint(100, 255), np.random.randint(100, 255), np.random.randint(100, 255))
            draw.ellipse([x, y, x+w, y+h], fill=color)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(test_image_path), exist_ok=True)
        img.save(test_image_path)
        print(f"✅ Test image created: {test_image_path}")
    
    # Test the API
    api_url = 'http://localhost:3000/api/samples/generate-heatmap'
    
    try:
        # Test with existing image path
        payload = {
            'imagePath': test_image_path,
            'heatmapType': 'tumor_probability',
            'colormap': 'hot'
        }
        
        print("🎨 Testing heatmap API...")
        print(f"   URL: {api_url}")
        print(f"   Image: {test_image_path}")
        print(f"   Type: {payload['heatmapType']}")
        print(f"   Colormap: {payload['colormap']}")
        
        response = requests.post(api_url, data=payload, timeout=30)
        
        print(f"\n📊 Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get('success'):
                print("✅ Heatmap generation successful!")
                print(f"   Processing time: {result['data'].get('processing_time', 'N/A')}ms")
                print(f"   Heatmap type: {result['data']['heatmap']['type']}")
                print(f"   Colormap: {result['data']['heatmap']['colormap']}")
                
                # Check if analytics are included
                if 'analytics' in result['data']['heatmap']:
                    analytics = result['data']['heatmap']['analytics']
                    print(f"   Analytics: min={analytics.get('min_value', 0):.3f}, max={analytics.get('max_value', 0):.3f}")
                
                print("✅ API test passed!")
                return True
            else:
                print(f"❌ API returned error: {result.get('error')}")
                return False
        else:
            print(f"❌ API request failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Heatmap API Integration")
    print("=" * 50)
    
    success = test_heatmap_api()
    
    if success:
        print("\n🎉 All tests passed! Your heatmap API is working.")
        print("\n💡 Next steps:")
        print("1. Open http://localhost:5173 in your browser")
        print("2. Upload a sample with images")
        print("3. Go to the 'AI Heatmaps' tab")
        print("4. Select an image and generate heatmaps!")
    else:
        print("\n❌ Tests failed. Please check the error messages above.")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure backend server is running on port 3000")
        print("2. Ensure Python and matplotlib are installed")
        print("3. Check that the ML script path is correct")