import random
from bunker_card import *
class bunker_karti():

    def Profession_random():
        global Karta_player_Profession_vivod_dannih
        Karta_player_Profession = random.randint(0, len(Profession))
        Karta_player_Profession_vivod_dannih = (
            Profession[Karta_player_Profession - 1])
        # print(Karta_player_Profession_vivod_dannih)

    def Biology_random():
        global Random_vibor_name_byology
        Random_vibor_byology = random.randint(0, (len(Biology) - 1))
        Random_vibor_name_byology = (Biology[Random_vibor_byology])
        # print(Random_vibor_name_byology)

    def Health_random():
        global Random_vibor_zdorovie_name
        Random_vibor_zdorovie = random.randint(0, (len(Health) - 1))
        Random_vibor_zdorovie_name = (Health[Random_vibor_zdorovie])
        # print(Random_vibor_zdorovie_name)

    def Hobby_random():
        global Random_vibor_Hobby_name
        Random_vibor_Hobby = random.randint(0, (len(Hobby) - 1))
        Random_vibor_Hobby_name = (Hobby[Random_vibor_Hobby])
        # print(Random_vibor_Hobby_name)

    def Luggage_random():
        global Random_vibor_Luggage_name
        Random_vibor_Luggage = random.randint(0, (len(Luggage) - 1))
        Random_vibor_Luggage_name = (Luggage[Random_vibor_Luggage])
        # print(Random_vibor_Luggage_name)

    def Evidence_random():
        global Random_vibor_Evidencev_name
        Random_vibor_Evidencev = random.randint(0, (len(Evidence) - 1))
        Random_vibor_Evidencev_name = (Evidence[Random_vibor_Evidencev])
        # print(Random_vibor_Evidencev_name)

    def Special_conditions_random():
        global Random_vibor_Special_conditions_name
        Random_vibor_Special_conditions = random.randint(
            0, (len(Special_conditions) - 1))
        Random_vibor_Special_conditions_name = (
            Special_conditions[Random_vibor_Special_conditions])
        # print(Random_vibor_Special_conditions_name)

    def Vizon_kart():
        bunker_karti.Profession_random()
        bunker_karti.Biology_random()
        bunker_karti.Health_random()
        bunker_karti.Hobby_random()
        bunker_karti.Luggage_random()
        bunker_karti.Evidence_random()
        bunker_karti.Special_conditions_random()

    def stol_play():

        bunker_karti.Vizon_kart()
        global stol_karti
        Profession_stol = Karta_player_Profession_vivod_dannih
        Biology_stol = Random_vibor_name_byology
        Zdorovie_stol = Random_vibor_zdorovie_name
        Hobby_stol = Random_vibor_Hobby_name
        Luggage_stol = Random_vibor_Luggage_name
        Evidencev_stol = Random_vibor_Evidencev_name
        Special_conditions_stol = Random_vibor_Special_conditions_name
        Ready_table_player = Profession_stol, Biology_stol, Zdorovie_stol,Hobby_stol, Luggage_stol, Evidencev_stol, Special_conditions_stol
        return Ready_table_player
    
class Sobitia():
    # Не выведены в глобал!
    def Disasters_random():
        Random_vibor_Disasters = random.randint(0, len(Disasters))
        Random_vibor_Disasters_name = (
            Disasters[Random_vibor_Disasters])
        print(Random_vibor_Disasters_name)

    def danger_random():
        Random_vibor_danger = random.randint(0, len(danger))
        Random_vibor_danger_name = (danger[Random_vibor_danger])
        print(Random_vibor_danger_name)

    def bunker_cards_random():
        Random_vibor_bunker_cards = random.randint(0, len(bunker_cards))
        Random_vibor_bunker_cards_name = (
            bunker_cards[Random_vibor_bunker_cards])
        print(Random_vibor_bunker_cards_name)