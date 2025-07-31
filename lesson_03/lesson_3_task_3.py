from adress import Adress
from mailing import Mailing

to_address=Adress("667112", "New_Hope", "Sovetskaya", "25", "26")
from_address=Adress("223445", "Old_Dream", "Kosmonavtov", "10", "45")
mailing=Mailing(to_address, from_address, 4000, "Тушенка")

print (
   f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
   f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat}, "
   f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
   f"{mailing.to_address.house} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей."
      )
    
      

