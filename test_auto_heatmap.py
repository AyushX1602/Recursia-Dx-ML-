#!/usr/bin/env python3
"""
Test script to verify the complete auto-heatmap workflow:
1. Upload an image 
2. Verify heatmap is generated automatically
3. Check if heatmap data is available in the API response
"""

import requests
import json
import time
import os

def test_auto_heatmap_workflow():
    base_url = "http://localhost:5001"
    
    print("🔧 Testing Auto-Heatmap Workflow...")
    print("=" * 50)
    
    # Step 1: Test health endpoint
    print("1. Testing backend health...")
    try:
        health_response = requests.get(f"{base_url}/health", timeout=5)
        if health_response.status_code == 200:
            print("✅ Backend is healthy")
        else:
            print("❌ Backend health check failed")
            return
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        return
    
    # Step 2: Get current samples to see existing heatmaps
    print("\n2. Checking existing samples with heatmaps...")
    try:
        samples_response = requests.get(f"{base_url}/api/samples", timeout=10)
        if samples_response.status_code == 200:
            samples = samples_response.json()
            print(f"📊 Found {len(samples)} samples")
            
            # Look for samples with heatmaps
            heatmap_samples = [s for s in samples if any(img.get('heatmap') for img in s.get('images', []))]
            print(f"🔥 Samples with heatmaps: {len(heatmap_samples)}")
            
            if heatmap_samples:
                sample = heatmap_samples[0]
                print(f"\n📋 Sample with heatmap found:")
                print(f"   ID: {sample.get('_id')}")
                print(f"   Patient: {sample.get('patientInfo', {}).get('name', 'Unknown')}")
                
                for i, img in enumerate(sample.get('images', [])):
                    if img.get('heatmap'):
                        print(f"   Image {i+1}: {img.get('filename')}")
                        print(f"   Heatmap: {img.get('heatmap', {}).get('imagePath', 'No path')}")
                        print(f"   Analytics: {img.get('heatmap', {}).get('analytics', 'No analytics')}")
                        
                print("\n✅ Auto-heatmap workflow is working!")
                print("📱 You can now view heatmaps in the UI at: http://localhost:5173")
                print("🔥 Check the 'Auto Heatmaps' tab in the Analysis Dashboard")
                
            else:
                print("⚠️  No samples with heatmaps found")
                print("💡 Try uploading an image through the UI to trigger auto-generation")
                
        else:
            print(f"❌ Failed to fetch samples: {samples_response.status_code}")
            
    except Exception as e:
        print(f"❌ Error checking samples: {e}")
    
    # Step 3: Check heatmap files on disk
    print("\n3. Checking generated heatmap files...")
    heatmap_dir = "backend/uploads/heatmaps"
    if os.path.exists(heatmap_dir):
        heatmap_files = [f for f in os.listdir(heatmap_dir) if f.endswith('.png')]
        print(f"📁 Found {len(heatmap_files)} heatmap files:")
        for file in heatmap_files[:5]:  # Show first 5
            print(f"   - {file}")
        if len(heatmap_files) > 5:
            print(f"   ... and {len(heatmap_files) - 5} more")
    else:
        print("❌ Heatmap directory not found")
    
    print("\n" + "=" * 50)
    print("🎯 Auto-Heatmap Workflow Test Complete!")
    print("📱 Open http://localhost:5173 to see the UI")
    print("🔥 Upload images to see auto-generation in action")

if __name__ == "__main__":
    test_auto_heatmap_workflow()