from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tempo de espera entre as requisições
    
    def on_start(self):
        # Login antes de iniciar os testes
        self.client.post("/login", {
            "username": "test_user",
            "password": "test_pass"
        })
    
    @task(2)
    def view_items(self):
        self.client.get("/items")
        
    @task(1)
    def view_item(self):
        item_id = 1
        self.client.get(f"/item/{item_id}", name="/item/[id]")
    
    @task(1)
    def add_to_cart(self):
        self.client.post("/cart/add", json={
            "item_id": 1,
            "quantity": 1
        })

# Para executar: locust -f locustfile.py
