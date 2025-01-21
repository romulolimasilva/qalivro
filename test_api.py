import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
    
    def test_get_posts(self):
        response = requests.get(f"{self.base_url}/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("title", data)
        self.assertIn("body", data)
    
    def test_create_post(self):
        payload = {
            "title": "Teste Post",
            "body": "Conteúdo do teste",
            "userId": 1
        }
        response = requests.post(f"{self.base_url}/posts", json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["title"], payload["title"])

if __name__ == '__main__':
    unittest.main()
