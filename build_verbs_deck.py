# -*- coding: utf-8 -*-
import genanki

MODEL_ID = 1943015782
DECK_IDS = {3: 1837465012, 4: 1837465013, 5: 1837465014}

DECK_NAMES = {
    3: "Deutsch A1::Verben::03 sein, haben, möchten",
    4: "Deutsch A1::Verben::04 Vokalwechsel",
    5: "Deutsch A1::Verben::05 Modalverben",
}

PRON_NOM = ["я", "ты", "он", "мы", "вы", "они"]
PRON_DAT = ["мне", "тебе", "ему", "нам", "вам", "им"]
PRON_DE = ["ich", "du", "er", "wir", "ihr", "sie"]
PERSON_TAGS = ["ich", "du", "er-sie-es", "wir", "ihr", "sie-Sie"]
IHR_HINT = "несколько человек, на «ты»"

model = genanki.Model(
    MODEL_ID,
    "DE Verbkonjugation RU→DE (Tippen)",
    fields=[
        {"name": "Russian"},
        {"name": "Hint"},
        {"name": "Answer"},
        {"name": "German"},
        {"name": "Verb"},
        {"name": "Group"},
    ],
    templates=[
        {
            "name": "RU → DE",
            "qfmt": """<div class="ru">{{Russian}}</div>
{{#Hint}}<div class="hint">{{Hint}}</div>{{/Hint}}
<div class="typebox">{{type:Answer}}</div>""",
            "afmt": """{{FrontSide}}
<hr id="answer">
<div class="de">{{German}}</div>
<div class="tts">{{tts de_DE voices=Apple_Anna:Answer}}</div>
<div class="verb">{{Verb}}</div>
<div class="group">{{Group}}</div>""",
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
.typebox { margin-top: 18px; }
#typeans {
  font-size: 24px; text-align: center; padding: 6px 10px; width: 82%;
  border: 1px solid #c9c6bd; border-radius: 6px;
  background: #fff; color: #1a1a1a;
}
.nightMode #typeans { background: #2c2b26; color: #e8e6e0; border-color: #4a473f; }
.hint { font-size: 15px; color: #8a8a8a; margin-top: 8px; }
.de { font-size: 38px; font-weight: 600; color: #1d4ed8; margin: 6px 0 14px; }
.verb { font-size: 18px; color: #444; }
.group { font-size: 14px; color: #8a8a8a; margin-top: 4px; }
hr#answer { border: none; border-top: 1px solid #dcdcd6; margin: 20px auto; width: 60%; }
.nightMode.card { background: #21201c; color: #e8e6e0; }
.nightMode .de { color: #93b8ff; }
.nightMode .verb { color: #c9c6bd; }
.nightMode .hint, .nightMode .group { color: #8f8c84; }
.nightMode hr#answer { border-top-color: #3d3b35; }
""",
)

G_BESONDERS = "besondere Verben"
G_EI = "Vokalwechsel  e → i / ie"
G_AAE = "Vokalwechsel  a → ä"
G_MODAL = "Modalverb"

# (kapitel, infinitiv, RU-Bedeutung, Gruppe, Extratags, dt. Formen, Pronomen-Set, ru Formen)
VERBS = [
    (3, "sein", "быть", G_BESONDERS, [],
     ["bin", "bist", "ist", "sind", "seid", "sind"],
     PRON_NOM, ["есть"] * 6),
    (3, "haben", "иметь", G_BESONDERS, [],
     ["habe", "hast", "hat", "haben", "habt", "haben"],
     PRON_NOM, ["имею", "имеешь", "имеет", "имеем", "имеете", "имеют"]),
    (3, "mögen", "любить, нравиться", G_BESONDERS, [],
     ["mag", "magst", "mag", "mögen", "mögt", "mögen"],
     PRON_NOM, ["люблю", "любишь", "любит", "любим", "любите", "любят"]),
    (3, "wissen", "знать", G_BESONDERS, [],
     ["weiß", "weißt", "weiß", "wissen", "wisst", "wissen"],
     PRON_NOM, ["знаю", "знаешь", "знает", "знаем", "знаете", "знают"]),
    (3, "tun", "делать", G_BESONDERS, [],
     ["tue", "tust", "tut", "tun", "tut", "tun"],
     PRON_NOM, ["делаю", "делаешь", "делает", "делаем", "делаете", "делают"]),
    (3, "„möchten“", "хотеть (вежливо)", G_MODAL, ["kapitel05", "modalverben"],
     ["möchte", "möchtest", "möchte", "möchten", "möchtet", "möchten"],
     PRON_DAT, ["хотелось бы"] * 6),

    (4, "essen", "есть, кушать", G_EI, [],
     ["esse", "isst", "isst", "essen", "esst", "essen"],
     PRON_NOM, ["ем", "ешь", "ест", "едим", "едите", "едят"]),
    (4, "empfehlen", "рекомендовать", G_EI, [],
     ["empfehle", "empfiehlst", "empfiehlt", "empfehlen", "empfehlt", "empfehlen"],
     PRON_NOM, ["рекомендую", "рекомендуешь", "рекомендует", "рекомендуем", "рекомендуете", "рекомендуют"]),
    (4, "geben", "давать", G_EI, [],
     ["gebe", "gibst", "gibt", "geben", "gebt", "geben"],
     PRON_NOM, ["даю", "даёшь", "даёт", "даём", "даёте", "дают"]),
    (4, "fernsehen", "смотреть телевизор", G_EI, ["trennbar"],
     ["sehe fern", "siehst fern", "sieht fern", "sehen fern", "seht fern", "sehen fern"],
     PRON_NOM, ["смотрю телевизор", "смотришь телевизор", "смотрит телевизор",
                "смотрим телевизор", "смотрите телевизор", "смотрят телевизор"]),
    (4, "helfen", "помогать", G_EI, [],
     ["helfe", "hilfst", "hilft", "helfen", "helft", "helfen"],
     PRON_NOM, ["помогаю", "помогаешь", "помогает", "помогаем", "помогаете", "помогают"]),
    (4, "lesen", "читать", G_EI, [],
     ["lese", "liest", "liest", "lesen", "lest", "lesen"],
     PRON_NOM, ["читаю", "читаешь", "читает", "читаем", "читаете", "читают"]),
    (4, "mitnehmen", "брать с собой", G_EI, ["trennbar"],
     ["nehme mit", "nimmst mit", "nimmt mit", "nehmen mit", "nehmt mit", "nehmen mit"],
     PRON_NOM, ["беру с собой", "берёшь с собой", "берёт с собой",
                "берём с собой", "берёте с собой", "берут с собой"]),
    (4, "nehmen", "брать", G_EI, [],
     ["nehme", "nimmst", "nimmt", "nehmen", "nehmt", "nehmen"],
     PRON_NOM, ["беру", "берёшь", "берёт", "берём", "берёте", "берут"]),
    (4, "sehen", "видеть", G_EI, [],
     ["sehe", "siehst", "sieht", "sehen", "seht", "sehen"],
     PRON_NOM, ["вижу", "видишь", "видит", "видим", "видите", "видят"]),
    (4, "sprechen", "говорить", G_EI, [],
     ["spreche", "sprichst", "spricht", "sprechen", "sprecht", "sprechen"],
     PRON_NOM, ["говорю", "говоришь", "говорит", "говорим", "говорите", "говорят"]),
    (4, "vergessen", "забывать", G_EI, [],
     ["vergesse", "vergisst", "vergisst", "vergessen", "vergesst", "vergessen"],
     PRON_NOM, ["забываю", "забываешь", "забывает", "забываем", "забываете", "забывают"]),
    (4, "werden", "становиться", G_EI, [],
     ["werde", "wirst", "wird", "werden", "werdet", "werden"],
     PRON_NOM, ["становлюсь", "становишься", "становится", "становимся", "становитесь", "становятся"]),

    (4, "abfahren", "отъезжать", G_AAE, ["trennbar"],
     ["fahre ab", "fährst ab", "fährt ab", "fahren ab", "fahrt ab", "fahren ab"],
     PRON_NOM, ["отъезжаю", "отъезжаешь", "отъезжает", "отъезжаем", "отъезжаете", "отъезжают"]),
    (4, "anfangen", "начинать", G_AAE, ["trennbar"],
     ["fange an", "fängst an", "fängt an", "fangen an", "fangt an", "fangen an"],
     PRON_NOM, ["начинаю", "начинаешь", "начинает", "начинаем", "начинаете", "начинают"]),
    (4, "einladen", "приглашать", G_AAE, ["trennbar"],
     ["lade ein", "lädst ein", "lädt ein", "laden ein", "ladet ein", "laden ein"],
     PRON_NOM, ["приглашаю", "приглашаешь", "приглашает", "приглашаем", "приглашаете", "приглашают"]),
    (4, "einschlafen", "засыпать", G_AAE, ["trennbar"],
     ["schlafe ein", "schläfst ein", "schläft ein", "schlafen ein", "schlaft ein", "schlafen ein"],
     PRON_NOM, ["засыпаю", "засыпаешь", "засыпает", "засыпаем", "засыпаете", "засыпают"]),
    (4, "fahren", "ехать", G_AAE, [],
     ["fahre", "fährst", "fährt", "fahren", "fahrt", "fahren"],
     PRON_NOM, ["еду", "едешь", "едет", "едем", "едете", "едут"]),
    (4, "gefallen", "нравиться", G_AAE, [],
     ["gefalle", "gefällst", "gefällt", "gefallen", "gefallt", "gefallen"],
     PRON_NOM, ["нравлюсь", "нравишься", "нравится", "нравимся", "нравитесь", "нравятся"]),
    (4, "laufen", "бежать", G_AAE, [],
     ["laufe", "läufst", "läuft", "laufen", "lauft", "laufen"],
     PRON_NOM, ["бегу", "бежишь", "бежит", "бежим", "бежите", "бегут"]),
    (4, "schlafen", "спать", G_AAE, [],
     ["schlafe", "schläfst", "schläft", "schlafen", "schlaft", "schlafen"],
     PRON_NOM, ["сплю", "спишь", "спит", "спим", "спите", "спят"]),
    (4, "tragen", "нести, носить", G_AAE, [],
     ["trage", "trägst", "trägt", "tragen", "tragt", "tragen"],
     PRON_NOM, ["ношу", "носишь", "носит", "носим", "носите", "носят"]),
    (4, "waschen", "мыть, стирать", G_AAE, [],
     ["wasche", "wäschst", "wäscht", "waschen", "wascht", "waschen"],
     PRON_NOM, ["мою", "моешь", "моет", "моем", "моете", "моют"]),

    (5, "können", "мочь, уметь", G_MODAL, [],
     ["kann", "kannst", "kann", "können", "könnt", "können"],
     PRON_NOM, ["могу (умею)", "можешь (умеешь)", "может (умеет)",
                "можем (умеем)", "можете (умеете)", "могут (умеют)"]),
    (5, "müssen", "быть должным, быть вынужденным", G_MODAL, [],
     ["muss", "musst", "muss", "müssen", "müsst", "müssen"],
     PRON_NOM, ["должен", "должен", "должен", "должны", "должны", "должны"]),
    (5, "dürfen", "мочь (иметь разрешение)", G_MODAL, [],
     ["darf", "darfst", "darf", "dürfen", "dürft", "dürfen"],
     PRON_DAT, ["можно"] * 6),
    (5, "wollen", "хотеть", G_MODAL, [],
     ["will", "willst", "will", "wollen", "wollt", "wollen"],
     PRON_NOM, ["хочу", "хочешь", "хочет", "хотим", "хотите", "хотят"]),
    (5, "sollen", "быть должным (по чужой воле)", G_MODAL, [],
     ["soll", "sollst", "soll", "sollen", "sollt", "sollen"],
     PRON_DAT, ["следует"] * 6),
]

GROUP_TAGS = {
    G_BESONDERS: "besondere-verben",
    G_EI: "vokalwechsel::e-i",
    G_AAE: "vokalwechsel::a-ae",
    G_MODAL: "modalverben",
}

decks = {k: genanki.Deck(DECK_IDS[k], DECK_NAMES[k]) for k in DECK_IDS}

seen_fronts = {}
total = 0

for kapitel, inf, meaning, group, extra_tags, de_forms, pronouns, ru_forms in VERBS:
    clean_inf = inf.strip("„“")
    for i in range(6):
        russian = pronouns[i] + " " + ru_forms[i]
        hint = IHR_HINT if i == 4 else ""
        if i == 2:
            german = "er / sie / es " + de_forms[i]
        elif i == 5:
            german = "sie %s  /  Sie %s" % (de_forms[i], de_forms[i])
        else:
            german = ["ich", "du", "", "wir", "ihr", ""][i] + " " + de_forms[i]

        if russian in seen_fronts:
            raise SystemExit("Kollision: %r (%s vs %s)" % (russian, seen_fronts[russian], clean_inf))
        seen_fronts[russian] = clean_inf

        tags = ["kapitel%02d" % kapitel, "verb::" + clean_inf,
                "person::" + PERSON_TAGS[i], GROUP_TAGS[group]] + extra_tags
        decks[kapitel].add_note(genanki.Note(
            model=model,
            fields=[russian, hint, PRON_DE[i] + " " + de_forms[i], german,
                    "%s — %s" % (inf, meaning), group],
            tags=tags,
            guid=genanki.guid_for("de-a1-verben", clean_inf, PERSON_TAGS[i]),
        ))
        total += 1

genanki.Package(list(decks.values())).write_to_file("Deutsch_A1_Verben_03-05.apkg")
for k in sorted(decks):
    print("  %-46s %3d Karten" % (DECK_NAMES[k], len(decks[k].notes)))
print("Deutsch_A1_Verben_03-05.apkg:", total, "Karten,", len(VERBS), "Verben")
