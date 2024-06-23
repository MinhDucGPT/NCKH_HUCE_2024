print("Toi_thich_AI_thich_Toan")
import re
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
title = "Tôi thích AI thích Toán"
Volca = sorted(set((' '.join(corpus)).split(' ')))
appear = []
for i in Volca:
    pattern = i
    timKiem = re.findall(i, title)
    appear.append(len(timKiem))
print("Tôi thích AI thích Toán: ", appear)
print("Bag-of-word: ", Volca, end="\n\n\n\n")