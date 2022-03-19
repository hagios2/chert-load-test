from locust import HttpUser, task, between
import time 


class ChertUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def login(self):
        self.client.post("/api/auth/login", json={'email':'hagioswilson@gmail.com', 'password': '123456'})
    
    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})