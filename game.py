from countryinfo import CountryInfo
import random


COUNTRIES = list(CountryInfo().all().keys())
COUNTRY = CountryInfo()
# for c in COUNTRY:
#     print(c)


class Game:
    def __init__(self):
        self.curCountry = ''
        self.curCity = ''
        self.score = 0
        self.guess_city = False

    def get_country(self):
        self.curCountry = COUNTRIES[random.randint(0, len(COUNTRIES))]
        print(self.curCountry)
        self.curCity = CountryInfo(self.curCountry).capital()
        print(self.curCity)
        return self.curCountry

    # def get_city(self):
    #     self.get_country()
    #     self.curCity = CountryInfo(self.curCountry).capital()
    #     print(self.curCity)
    #     return self.curCity

    # def check_answer(self, answer):

    def get_score(self):
        return self.score

    def get_hint(self):
        if self.guess_city:
            return "Answer contains " + len(self.curCountry) + " letters."
        else:
            return "Answer contains " + len(self.curCity) + " letters."


if __name__ == '__main__':
    game = Game()
    while True:
        guess_country = input("Would you like to guess the [CO]untry or the [CA]pital city?").upper()
        if not len(guess_country) == 2:
            print("Please make an appropriate decision.")
        else:
            if guess_country == 'CO':
                game.get_country()
                city = game.curCity
                game.guess_city = False
                while True:
                    guess = input("What's the country of {}?".format(city))
                    if guess == 'skip':
                        break
                    elif guess.lower() == game.curCountry:
                        print("Correct! The country of {} is indeed {}!".format(city, guess))
                        game.score += 1
                        break
                    else:
                        print("Wrong! Try again!")
            elif guess_country == 'CA':
                country = game.get_country()
                game.guess_city = True

                while True:
                    guess = input("What's the capital city of {}?".format(country))
                    if guess == 'skip':
                        break
                    elif guess.lower() == game.curCity.lower():
                        print("Correct! The capital city of {} is indeed {}!".format(country, guess))
                        game.score += 1
                        break
                    else:
                        print("Wrong! Try again!")


