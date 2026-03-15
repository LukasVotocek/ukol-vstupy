from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict

# Datové modely
class Osoba(BaseModel):
    id: int
    nazev: str

class Pristupova_karta(BaseModel):
    id_karty: str
    cislo_zamestnance: Optional[int] = None

class Zaznam(BaseModel):
    id_karty: str
    datum_cas: datetime
    typ: str  # 'vstup' nebo 'vystup'

# Úložiště dat
osoby: Dict[int, Osoba] = {}
pristupove_karty: Dict[str, Pristupova_karta] = {}
zaznamy: List[Zaznam] = []

def pridej_zamestnance(cislo: int, nazev: str) -> None:
    osoby[cislo] = Osoba(id=cislo, nazev=nazev)

def prirad_kartu_zamestnanci(kod: str, cislo: int) -> None:
    pristupove_karty[kod] = Pristupova_karta(id_karty=kod, cislo_zamestnance=cislo)

def zaznamenej_prichod(kod: str) -> None:
    nyni = datetime.now()
    typ = 'vstup'
    if zaznamy and zaznamy[-1].id_karty == kod and zaznamy[-1].typ == 'vstup':
        typ = 'vystup'
    zaznamy.append(Zaznam(id_karty=kod, datum_cas=nyni, typ=typ))

def ziskej_zaznamy(kod: Optional[str] = None, cislo: Optional[int] = None) -> List[Zaznam]:
    vystup = zaznamy
    if kod:
        vystup = [p for p in vystup if p.id_karty == kod]
    if cislo:
        karty_zamestnance = [k.id_karty for k in pristupove_karty.values() if k.cislo_zamestnance == cislo]
        vystup = [p for p in vystup if p.id_karty in karty_zamestnance]
    return vystup

def kdo_je_pritomen() -> List[str]:
    aktualni_stav: Dict[str, str] = {}
    for zaznam in zaznamy:
        aktualni_stav[zaznam.id_karty] = zaznam.typ
    pritomni = [kod for kod, typ in aktualni_stav.items() if typ == 'vstup']
    return pritomni
