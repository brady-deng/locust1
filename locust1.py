import time
from locust import HttpUser, task
import os


class QuickstartUser(HttpUser):

    # @task
    # def hello_world(self):
    #     header = {
    #         "Cookie":"portalUser=1010"
    #     }
    #     rep = self.client.get("/test/5", headers = header)



    @task(1)
    def hello_world(self):
        print("start to request", self, "time ", time.asctime(time.localtime(time.time())))
        with self.client.get("/test/personTest?name=deng", catch_response=True) as rep:
            if rep.status_code != 200 or rep.elapsed.seconds > 10:
                rep.failure("fail")
            else:
                rep.success()

        # self.client.get("/world")
    #
    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})


if __name__ == "__main__":
    os.system("locust -f locust1.py --host=http://localhost:8082")
