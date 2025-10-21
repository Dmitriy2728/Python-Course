from smartphone import Smartphone

Catalog=[
    Smartphone("Samsung", "D500", "+79001112222"),
    Smartphone("SonyEricssone", "W580", "+79003334444"),
    Smartphone("Nokia", "3310", "+79005556666"),
    Smartphone("Siemens", "A20", "+79007778888"),
    Smartphone("Motorolla", "E398", "+79009990000")
]

for Smartphone in Catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.number}") 
