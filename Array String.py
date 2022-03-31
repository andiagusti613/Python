hewan = {
    "Jalak Bali" : "Bali",
    "Harimau Sumatera" : "Sumatera",
    "Badak Jawa" : "Jawa Barat",
    "Cendrawasih" : "Papua",
    "Anoa" : "Sulawesi"
}
print("Nama hewan beserta asal Daerahnya: ")
for kunci, value in hewan.items():
    print(kunci + " Berasal dari " +value)