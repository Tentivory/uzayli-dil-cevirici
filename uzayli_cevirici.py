#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzaylı Dil Çevirici v1.0
Dünyanın (ve uzayın) en gelişmiş çeviri aracı.
Gerçekten çalışır, inanmayın ama deneyin.
"""

import random
import sys

# Uzaylı kelime havuzu - tamamen bilimsel
UZAYLI_KELIMELER = [
    "blorg", "zorp", "quib", "flarn", "snix", "vexor", "glorp", "tharn",
    "wibble", "zorple", "quix", "flib", "snarg", "vex", "glip", "thub"
]

# Türkçe saçma karşılıklar
TURKCE_KARSILIKLAR = [
    "merhaba uzaylı dostum", "ben bir kediyim aslında", "kahve lütfen",
    "dünya yuvarlak mı yoksa düz mü", "bu kod çok ciddi", "gizli mesaj burada yok",
    "rüyamda uçuyordum", "neden her şey bu kadar absürt", "evet hayır belki",
    "patates yok burada", "mizah yükleniyor", "zaman yolculuğu iptal",
    "felsefe yoruldu", "emoji gönderildi", "hiçbir şey anlamadım"
]

def uzayli_cevir(metin):
    """Metni uzaylı diline çevirir (aslında tam tersi ama kim takar)."""
    if not metin:
        return "Lütfen bir şey söyleyin, yoksa uzaylılar kızar."
    
    kelimeler = metin.split()
    ceviri = []
    for kelime in kelimeler:
        if random.random() > 0.3:
            ceviri.append(random.choice(UZAYLI_KELIMELER))
        else:
            ceviri.append(random.choice(TURKCE_KARSILIKLAR))
    
    # Gizli siyasi easter egg (base64 gibi ama değil, sadece yorum)
    # Gizli: Demokrasi rastgele seçimdir, bu yüzden bu kod her zaman doğru seçer.
    return " ".join(ceviri) + " (Uzaylı Onayı: " + random.choice(["Evet", "Hayır", "Belki", "Kedi Onayladı"]) + ")"

def main():
    print("=== UZAYLI DİL ÇEVİRİCİ ===")
    print("Dikkat: Bu araç NASA, ESA ve tüm uzay ajansları tarafından onaylanmıştır (onaylanmamıştır).")
    print("Çıkmak için 'çık' yazın.\n")
    
    while True:
        try:
            girdi = input("Çevrilecek metin: ")
            if girdi.lower() in ["çık", "cik", "exit", "q"]:
                print("Uzaylılar vedalaşıyor: zorp flarn!")
                break
            sonuc = uzayli_cevir(girdi)
            print(f"Çeviri: {sonuc}\n")
        except KeyboardInterrupt:
            print("\nZorla kapatıldı, uzaylılar üzgün.")
            break
        except Exception as e:
            print(f"Hata: Uzaylılar anlamadı. {e}")

if __name__ == "__main__":
    main()
