import time
from locust import HttpUser, task, constant
import os


class QuickstartUser(HttpUser):

    wait_time = constant(1);

    # @task
    # def hello_world(self):
    #     header = {
    #         "Cookie":"portalUser=1010"
    #     }
    #     rep = self.client.get("/test/5", headers = header)



    # @task(1)
    # def hello_world(self):
    #     print("start to request", self, "time ", time.asctime(time.localtime(time.time())))
    #     with self.client.get("/test/personTest?name=deng", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.get("/test/map/deng", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.put("/test/map/wang", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.get("/test/success", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.get("/test/redis/deng", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.put("/test/redis/wang", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    # @task(1)
    # def hello_world(self):
    #     with self.client.get("/test/1", catch_response=True) as rep:
    #         if rep.status_code != 200 or rep.elapsed.seconds > 10:
    #             rep.failure("fail")
    #         else:
    #             rep.success()

    @task(1)
    def hello_world(self):
        with self.client.put("/test/user/wang", catch_response=True) as rep:
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
    os.system("locust -f locust1.py --host=http://localhost:8080")
