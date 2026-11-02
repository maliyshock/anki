import genanki

model = genanki.Model(
    1607392319,
    "German-Russian Simple",
    fields=[{"name": "German"}, {"name": "Russian"}],
    templates=[
        {
            "name": "Card",
            "qfmt": "{{German}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Russian}}',
        }
    ],
)

deck = genanki.Deck(2059400110, "German Vocabulary")

cards = [
    ("der Wille", "воля"),
    ("die Wählermehrheit", "большинство избирателей"),
    ("der Wechsel", "изменение"),
    ("die Regierung", "правительство"),
    ("der Mindestanteil", "минимальная доля"),
    ("die Wählerstimme", "голос избирателя"),
    ("die Hürde", "барьер, порог (напр. 5%-й барьер)"),
    ("staatliche Gewalt", "государственная власть"),
    ("das Gericht", "суд (судебная власть)"),
    ("die Arbeitswelt", "сфера труда"),
    ("zuständig", "компетентный, ответственный, уполномоченный"),
    ("die Bundesregierung", "федеральное правительство"),
    ("der/die Abgeordnete", "депутат"),
    ("das Parlamentsmitglied", "член парламента"),
    ("gewählt werden", "быть избранным"),
    ("wählen", "выбирать"),
    ("meistens", "по большей части"),
    ("stärksten", "сильнейший"),
    ("Verfassungsorganen", "конституционные органы"),
    ("Unrecht", "несправедливость"),
    ("gekündigt", "увольнение"),
    ("Kündigungsschutzklage", "иск о защите от увольнения"),
    ("erheben", "поднимать"),
    ("darf", "может"),
    ("jüdischen", "еврейский"),
    ("Mitglied", "член"),
    ("vereinbar", "совместимый"),
    ("Oberhaupt", "глава"),
    ("Staatsoberhaupt", "глава государства"),
    ("Gemeinde", "община, муниципалитет"),
    ("jetzige", "текущий"),
    ("Straftat", "преступление"),
    ("angeklagt wird", "обвиняется"),
    ("vertreten", "представлять"),
    ("Gewerkschaften", "профсоюзы"),
    ("ein Schöffe", "народный судья"),
    ("wahlberechtigte", "имеющие право избиратели"),
    ("Schuld", "вина"),
    ("Wirtschaftsform", "экономическая форма"),
    ("berät", "советует, консультирует, даёт рекомендации"),
    ("Rechtsfragen", "юридические вопросы"),
    ("dreistufigen", "трёхступенчатый"),
    ("Verwaltungsaufbau", "административная структура"),
    ("spricht Urteile", "выносит приговоры (судит)"),
    ("Vereinigung", "ассоциация"),
    ("Judikative", "судебная власть"),
    ("Zweitstimmen", "вторые голоса"),
    ("erschweren", "усложнять"),
    ("verfassungswidrig", "неконституционный"),
    ("gegliedert", "подразделена"),
    ("Gesetze halten", "соблюдать законы"),
    ("Verfahren", "слушания"),
    ("häufigsten", "наиболее распространённый"),
    ("überwachen", "следить"),
    ("leugnen", "отрицать"),
    ("Sozialabgaben", "взносы на социальное обеспечение"),
    ("leitet", "направляет"),
    ("Gerichtsschöffe", "судья-доброволец"),
    ("ehrenamtlicher", "волонтёр"),
    ("Erwerbstätigen", "занятые люди"),
    ("Weltkrieg", "мировая война"),
    ("Sozialversicherung", "социальное обеспечение"),
    ("verbieten", "запретить"),
    ("teilzunehmen", "участвовать"),
]

for de, ru in cards:
    deck.add_note(genanki.Note(model=model, fields=[de, ru]))

genanki.Package(deck).write_to_file("LID_words.apkg")
print("Created LID_words.apkg with", len(cards), "cards")
