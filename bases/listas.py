
puertos = [23, 24, 80, 8080, 443, 1433]

puertos.append(11)
puertos.remove(8080)

puertos.sort()

for puerto in puertos:
    print(f"Puerto {puerto} disponible")

attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle']
attacks_upper = [attack.upper() for attack in attacks]

print(attacks_upper)

grades = [8, 10, 9.3, 9]

for attack, grade in zip(attacks, grades):
    print(f"{attack} has a grade: {grade}")

last_deleted_item= attacks.pop()
custom_deleted_item = attacks.pop(1)

print(last_deleted_item, custom_deleted_item)

attacks.insert(2, 'Ransomware')
more_attacks = ['attack 1', 'attack 2', 'attack 3']
attacks.extend(more_attacks)
print(attacks)