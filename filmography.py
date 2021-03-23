import requests



class Filmography:
        def __init__(self):
            self.KEY = "#"

        def get_id(self, name):
            """Use api to retrieve id"""
            id_url = ("https://api.themoviedb.org/3/search/person?query=" + 
                      name + "&api_key=" +
                      self.KEY )
            response = requests.get(id_url)
            ID = response.json()['results'][0]['id']
            return ID


        def get_number_of_pages(self, ID):
            """number of pages of films"""
            discover_url = ("https://api.themoviedb.org/3/discover/movie?with_cast=" +
                        str(ID) + "&api_key=" +
                        self.KEY)
            response = requests.get(discover_url)
            pages = response.json()["total_pages"]
            return pages

        def get_films(self, name):
            films = []
            ID = self.get_id(name)
            pages = self.get_number_of_pages(ID)
            for i in range(1,pages+1):
                discover_url = ("https://api.themoviedb.org/3/discover/movie?with_cast=" +
                    str(ID) + "&page=" + str(i) +"&api_key=" +
                    self.KEY)
                response = requests.get(discover_url)
                for result in response.json()["results"]:
                    films.append(result["title"])
            return films

  


name = "bee fhsohu"
""" next task is to cater when invalid name is given maybe raise an exception which will mean user needs to try again"""
"""next task is to write the app, use flask use bootstrap and html and jinja"""
Program = Filmography()
try:
    print(Program.get_films(name) )
except IndexError:
    print("INVALID NAME")


