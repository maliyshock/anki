# -*- coding: utf-8 -*-
import genanki

MODEL_ID = 1777223587899
DECK_ID = 1788553613699
DECK_NAME = "Deutsch A1::Verben::Unregelmäßige Verben"

model = genanki.Model(
    MODEL_ID,
    "DE Unregelmäßige Verben RU→3 Formen",
    fields=[
        {"name": "Russian"},
        {"name": "Forms"},
        {"name": "Speech"},
    ],
    templates=[
        {
            "name": "RU → 3 Formen",
            "qfmt": """<div class="ru">{{Russian}}</div>""",
            "afmt": """{{FrontSide}}
<hr id="answer">
<div class="forms">{{Forms}}</div>
<div class="tts">{{tts de_DE voices=Apple_Anna:Speech}}</div>""",
        }
    ],
    css="""
.card {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  text-align: center;
  background: #fdfdfb;
  color: #1a1a1a;
  padding: 24px 16px;
}
.ru { font-size: 30px; font-weight: 500; }
.forms { font-size: 34px; font-weight: 600; color: #1d4ed8; margin: 6px 0 4px; line-height: 1.35; }
hr#answer { border: none; border-top: 1px solid #dcdcd6; margin: 20px auto; width: 60%; }
.nightMode.card { background: #21201c; color: #e8e6e0; }
.nightMode .forms { color: #93b8ff; }
.nightMode hr#answer { border-top-color: #3d3b35; }
""",
)

# (Gruppe, Infinitiv, Präteritum, Partizip II, RU-Bedeutung)
VERBS = [
    ("a-i-a", "fangen", "fing", "gefangen", "ловить, поймать"),
    ("a-i-a", "lassen", "ließ", "gelassen", "велеть, позволять"),
    ("a-i-a", "fallen", "fiel", "gefallen", "падать, упасть (вниз)"),
    ("a-i-a", "halten", "hielt", "gehalten", "держать"),
    ("a-i-a", "raten", "riet", "geraten", "советовать"),
    ("a-u-a", "waschen", "wusch", "gewaschen", "мыть"),
    ("a-u-a", "wachsen", "wuchs", "gewachsen", "расти"),
    ("a-u-a", "laden", "lud", "geladen", "грузить"),
    ("a-u-a", "schlagen", "schlug", "geschlagen", "бить, ударять"),
    ("a-u-a", "tragen", "trug", "getragen", "носить, нести"),
    ("a-u-a", "fahren", "fuhr", "gefahren", "ехать, ездить"),
    ("e-a-e", "essen", "aß", "gegessen", "есть; питаться"),
    ("e-a-e", "vergessen", "vergaß", "vergessen", "забывать"),
    ("e-a-e", "lesen", "las", "gelesen", "читать"),
    ("e-a-e", "geben", "gab", "gegeben", "давать"),
    ("e-a-e", "sehen", "sah", "gesehen", "смотреть, глядеть"),
    ("e-a-e", "geschehen", "geschah", "geschehen", "происходить"),
    ("e-a-e", "treten", "trat", "getreten", "входить"),
    ("e-a-o", "nehmen", "nahm", "genommen", "брать, взять"),
    ("e-a-o", "helfen", "half", "geholfen", "помогать"),
    ("e-a-o", "sprechen", "sprach", "gesprochen", "говорить, разговаривать"),
    ("e-a-o", "erschrecken", "erschrak", "erschrocken", "(ис)пугаться"),
    ("e-a-o", "bewerben", "bewarb", "beworben", "(sich) подавать заявление, претендовать на место"),
    ("e-a-o", "empfehlen", "empfahl", "empfohlen", "рекомендовать"),
    ("e-a-o", "treffen", "traf", "getroffen", "встречать, заставать"),
    ("e-a-o", "werfen", "warf", "geworfen", "кидать"),
    ("e-a-o", "brechen", "brach", "gebrochen", "(с)ломать"),
    ("e-a-o", "stehlen", "stahl", "gestohlen", "воровать"),
    ("e-a-o", "sterben", "starb", "gestorben", "умирать, умереть"),
    ("i-a-u", "springen", "sprang", "gesprungen", "прыгать, скакать"),
    ("i-a-u", "trinken", "trank", "getrunken", "пить"),
    ("i-a-u", "finden", "fand", "gefunden", "находить"),
    ("i-a-u", "klingen", "klang", "geklungen", "звенеть"),
    ("i-a-u", "singen", "sang", "gesungen", "петь"),
    ("i-a-u", "sinken", "sank", "gesunken", "опускаться, тонуть, снижаться"),
    ("i-a-u", "verschwinden", "verschwand", "verschwunden", "исчезать, пропадать"),
    ("i-o-o", "ziehen", "zog", "gezogen", "тащить"),
    ("i-o-o", "verlieren", "verlor", "verloren", "(по)терять"),
    ("i-o-o", "schließen", "schloss", "geschlossen", "закрывать, захлопывать"),
    ("i-o-o", "fliegen", "flog", "geflogen", "летать, лететь"),
    ("i-o-o", "biegen", "bog", "gebogen", "гнуть"),
    ("i-o-o", "bieten", "bot", "geboten", "предлагать"),
    ("i-o-o", "riechen", "roch", "gerochen", "нюхать"),
    ("ei-ie-ie", "steigen", "stieg", "gestiegen", "подниматься"),
    ("ei-ie-ie", "schreiben", "schrieb", "geschrieben", "писать, написать"),
    ("ei-ie-ie", "bleiben", "blieb", "geblieben", "оставаться где-либо"),
    ("ei-ie-ie", "treiben", "trieb", "getrieben", "гнать"),
    ("ei-ie-ie", "entscheiden", "entschied", "entschieden", "принять решение"),
    ("ei-ie-ie", "leihen", "lieh", "geliehen", "одалживать"),
    ("ei-ie-ie", "scheinen", "schien", "geschienen", "светить, сиять"),
    ("ei-ie-ie", "vergleichen", "verglich", "verglichen", "сравнивать"),
    ("ei-ie-ie", "streiten", "stritt", "gestritten", "спорить"),
    ("i-a-o", "beginnen", "begann", "begonnen", "начинать"),
    ("i-a-o", "gewinnen", "gewann", "gewonnen", "выигрывать"),
    ("i-a-o", "schwimmen", "schwamm", "geschwommen", "плавать, плыть"),
    ("i-a-e", "bitten", "bat", "gebeten", "просить"),
    ("i-a-e", "liegen", "lag", "gelegen", "лежать"),
    ("i-a-e", "sitzen", "saß", "gesessen", "сидеть"),
    ("mischverben-t", "denken", "dachte", "gedacht", "думать, вспоминать"),
    ("mischverben-t", "bringen", "brachte", "gebracht", "приносить что-либо"),
    ("mischverben-t", "kennen", "kannte", "gekannt", "знать (быть знакомым)"),
    ("mischverben-t", "nennen", "nannte", "genannt", "называть"),
    ("mischverben-t", "brennen", "brannte", "gebrannt", "гореть"),
    ("mischverben-t", "wissen", "wusste", "gewusst", "знать (факт, информацию)"),
    ("sonstige", "gehen", "ging", "gegangen", "идти, ходить"),
    ("sonstige", "stehen", "stand", "gestanden", "стоять, находиться"),
    ("sonstige", "laufen", "lief", "gelaufen", "бегать, бежать"),
    ("sonstige", "tun", "tat", "getan", "делать"),
]

deck = genanki.Deck(DECK_ID, DECK_NAME)

seen_fronts = {}
for group, inf, praet, part2, ru in VERBS:
    if ru in seen_fronts:
        raise SystemExit("Kollision auf der Vorderseite: %r (%s vs %s)" % (ru, seen_fronts[ru], inf))
    seen_fronts[ru] = inf

    forms = "%s – %s – %s" % (inf, praet, part2)
    speech = "%s, %s, %s" % (inf, praet, part2)
    deck.add_note(genanki.Note(
        model=model,
        fields=[ru, forms, speech],
        tags=["unregelmaessige-verben", "gruppe::" + group, "verb::" + inf],
        guid=genanki.guid_for("de-unregelmaessige-verben", inf),
    ))

genanki.Package([deck]).write_to_file("Deutsch_Unregelmaessige_Verben.apkg")

from collections import Counter
counts = Counter(v[0] for v in VERBS)
for g in ["a-i-a", "a-u-a", "e-a-e", "e-a-o", "i-a-u", "i-o-o", "ei-ie-ie",
          "i-a-o", "i-a-e", "mischverben-t", "sonstige"]:
    print("  %-16s %2d" % (g, counts[g]))
print("Deutsch_Unregelmaessige_Verben.apkg:", len(deck.notes), "Karten")
