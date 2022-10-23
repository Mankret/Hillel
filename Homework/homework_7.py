# Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.


chess_players = {
    "Carlsen, Magnus": 2865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 2792,
    "Nepomniachtchi, Ian": 2773
}
generation_dict = {v: k for k, v in chess_players.items()}

print(chess_players, generation_dict, sep='\n')


