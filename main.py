from utils import loadJson
import requests
from datetime import datetime
import logging
import os


class Food_truck_list():
    def __init__(self, input_params):
        self.url = input_params[0]
        self.timestamp = int(input_params[1])
        self.passw = input_params[2]

    def unix_time_convert(self):
        return datetime.utcfromtimestamp(self.timestamp).timetuple()

    def error_status(self):
        if self.response.status_code != 200:
            return None

    def empty_list(self):
        if self.ret == []:
            return None

    def food_truck_list(self):
        food_truck_list = [i["Applicant"] +
                           ", " +
                           str(i["locationid"]) for i in self.ret]
        food_truck_list = sorted(food_truck_list)
        return food_truck_list

    def req_params(self):
        (year,
         month,
         day,
         hour,
         minutes,
         seconds,
         dayOrder,
         *rest) = self.unix_time_convert()

        self.head = {'Authorization': f'Basic {self.passw}'}

        self.endpoint = f'?year={year}&' +\
            f'month={month}&' +\
            f'day={day}&' +\
            f'hour={hour}&' +\
            f'minutes={minutes}&' +\
            f'seconds={seconds}&' +\
            f'dayOrder={(dayOrder + 1) % 7}'

    def run(self):
        try:
            self.req_params()
            self.response = requests.get(self.url + self.endpoint,
                                         headers=self.head)
            self.error_status()
            self.ret = self.response.json()["data"]
            self.empty_list()
            return self.food_truck_list()

        except Exception as e:
            print(e)


def main():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    log = logging.getLogger("food-logger")
    food = Food_truck_list(loadJson())

    if food.run() is None:
        log.info("N/A")
    else:
        for i in food.run():
            log.info(i)


if __name__ == "__main__":
    main()
