#!/usr/bin/env python3
"""
Test script to check the AnalysisDashboard data processing logic
"""

import requests
import json

def test_analysis_dashboard_data():
    """Test what data the AnalysisDashboard receives"""
    
    print("🔍 Testing AnalysisDashboard Data Processing...")
    print("=" * 50)
    
    # Check backend samples endpoint
    try:
        response = requests.get("http://localhost:5001/api/samples", timeout=10)
        if response.status_code == 200:
            samples = response.json()
            print(f"✅ Found {len(samples)} samples")
            
            # Look for samples with ML analysis
            analyzed_samples = []
            for sample in samples:
                if sample.get('images'):
                    for image in sample['images']:
                        if image.get('mlAnalysis'):
                            analyzed_samples.append(sample)
                            break
            
            print(f"🧠 Samples with ML analysis: {len(analyzed_samples)}")
            
            if analyzed_samples:
                sample = analyzed_samples[0]
                print(f"\n📋 Sample structure:")
                print(f"   ID: {sample.get('_id')}")
                print(f"   Patient: {sample.get('patientInfo', {}).get('name', 'Unknown')}")
                print(f"   Images: {len(sample.get('images', []))}")
                
                # Check ML analysis structure
                for i, image in enumerate(sample.get('images', [])):
                    if image.get('mlAnalysis'):
                        ml_data = image['mlAnalysis']
                        print(f"\n🧠 ML Analysis {i+1}:")
                        print(f"   prediction: {ml_data.get('prediction')}")
                        print(f"   confidence: {ml_data.get('confidence')}")
                        print(f"   riskAssessment: {ml_data.get('riskAssessment')}")
                        
                        # Check metadata structure
                        metadata = ml_data.get('metadata', {})
                        print(f"   metadata keys: {list(metadata.keys())}")
                        
                        # Check if prediction structure matches expected
                        if 'prediction' in metadata:
                            pred_meta = metadata['prediction']
                            print(f"   metadata.prediction keys: {list(pred_meta.keys())}")
                            
                            if 'probabilities' in pred_meta:
                                probs = pred_meta['probabilities']
                                print(f"   probabilities keys: {list(probs.keys())}")
                                print(f"   tumor probability: {probs.get('tumor')}")
                        break
                        
                print(f"\n🎯 Data structure analysis:")
                print("Expected by AnalysisDashboard:")
                print("  - analysis.metadata.prediction.probabilities.tumor")
                print("  - analysis.prediction ('malignant' for tumor detection)")
                print("  - analysis.riskAssessment")
                print("  - analysis.confidence")
                
            else:
                print("❌ No samples with ML analysis found")
                print("   The AnalysisDashboard will use mock data")
                
        else:
            print(f"❌ Backend request failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing backend: {e}")

if __name__ == "__main__":
    test_analysis_dashboard_data()