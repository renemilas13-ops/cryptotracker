def test_pass():
    assert True
    
def test_api():
    try:
        import requests
        print("✅ Requests OK")
    except:
        print("⚠️ Requests not installed")
