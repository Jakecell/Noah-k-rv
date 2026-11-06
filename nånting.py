from datetime import date

def veckodag(iso_datum):
  datum = date.fromisoformat(iso_datum)
  
  veckodagar = [
    "måndag",
    "tisdag",
    "onsdag",
    "torsdag",
    "fredag",
    "lördag",
    "söndag"
    ]
  return veckodagar[datum.weekday()]
  
print(veckodag("2026-10-02"))