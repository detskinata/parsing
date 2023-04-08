from abc import ABC, abstractmethod

import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, job_title: str, page=500):
        self.job_title = job_title
        self.vacancy_list = []
        for item in range(page):
            self.data = requests.get(f"https://api.hh.ru/vacancies?text={self.job_title}",
                                     params={'page': item, 'per_page': 1}).json()
            self.vacancy_list.append(self.data)

    def get_request(self) -> list:
        return self.vacancy_list
