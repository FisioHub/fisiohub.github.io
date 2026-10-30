#!/usr/bin/env python3
"""Static Site Generator for Fisio Hub Lugano (https://fisiohub.ch).

Generates every page of the site from a single shared layout and the content
data defined below:

  index.html            Homepage (hero + one-page overview of every section)
  hub.html              Lo studio, il nostro approccio, gli strumenti
  servizi.html          I servizi spiegati + gli strumenti spiegati
  cosa-trattiamo.html   I casi che trattiamo + banner post-operatorio
  team.html             Biografie, sigle spiegate, formazione e sport
  insta.html            Feed Instagram
  contatti.html         Mappa, contatti, fisioterapia a domicilio

Old URLs from the previous version of the site (terapie.html, dove.html, the
individual team pages and project/*.html) are regenerated as small redirect
pages so existing links and search results keep working.

Usage:
  python3 build.py
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# 1. Shared Site Configuration (Edit here to update across all pages)
# ==============================================================================
SITE_CONFIG = {
    "site_name": "Fisio Hub - Fisioterapia moderna Lugano",
    "company": "FisioHub SA",
    "address_line_1": "Via Carlo Maderno, 26",
    "address_line_2": "6900 Lugano",
    "phone_display": "079 839 69 00",
    # International format, digits only (no "+", no leading 0 of the Swiss
    # number): used for tel: and WhatsApp links.
    "phone_intl": "41798396900",
    "email": "fisiohub@hin.ch",
    "whatsapp_text": "Buongiorno, vorrei prenotare un appuntamento.",
    # Where every "Prenota appuntamento" button points. For now it is the
    # contact page; replace with the online booking URL once it is live.
    "booking_url": "contatti.html",
    "map_embed_url": (
        "https://maps.google.com/maps?width=650&amp;height=450&amp;hl=it"
        "&amp;q=lugano%20Via%20Carlo%20Maderno%2C%2026&amp;t=&amp;z=15"
        "&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"
    ),
    "map_link_url": (
        "https://www.google.com/maps/search/?api=1&amp;query=FisioHub%20Via"
        "%20Carlo%20Maderno%2026%20Lugano"
    ),
    "nav_items": [
        ("Hub", "hub.html"),
        ("Servizi", "servizi.html"),
        ("Cosa trattiamo", "cosa-trattiamo.html"),
        ("Il team", "team.html"),
        ("Social", "insta.html"),
        ("Contatti", "contatti.html"),
    ],
}

# Photos of the studio. Put the files in assets/images/ and write the paths
# here (e.g. "assets/images/studio-1.jpg"). While a slot is None, a clearly
# marked placeholder is shown instead.
STUDIO_PHOTOS = {
    "main": None,     # Homepage HUB section + hero of the HUB page
    "gallery_1": None,
    "gallery_2": None,
    "gallery_3": None,
    "sala_operatoria": None,  # Cosa trattiamo: banner "Dentro la sala operatoria"
}

# ==============================================================================
# 2. HUB text (homepage "HUB" section + HUB page)
# ==============================================================================
HUB_PARAGRAPHS = [
    (
        "FisioHub nasce dall’idea di tre colleghi uniti dalla passione per la"
        " fisioterapia e da una visione comune: mettere al centro il benessere"
        " reale della persona. Il nome <span class=\"hl\">“Hub” rappresenta un"
        " punto di connessione,</span> il luogo in cui la scienza incontra"
        " l’esperienza, dove metodo e ascolto si fondono per costruire percorsi"
        " terapeutici efficaci e personalizzati. Crediamo in una fisioterapia"
        " basata sulle evidenze scientifiche, ma profondamente attenta"
        " all’unicità di ogni individuo."
    ),
    (
        "<span class=\"hl\">Ogni paziente viene accompagnato passo dopo passo"
        " verso i propri obiettivi,</span> per ritrovare equilibrio, movimento"
        " e uno stile di vita più sano."
    ),
    (
        "Il nostro simbolo, una “H” minimale ed essenziale, vuole rappresentare"
        " proprio questo: un hub centrale, il luogo in cui percorsi, competenze"
        " e persone si incontrano per dare vita a un recupero completo,"
        " continuo e consapevole."
    ),
]

APPROACH_INTRO = (
    "<span class=\"hl\">Il nostro approccio vuole essere contemporaneo,"
    " affidabile,</span> orientato al movimento e lontano dai cliché della"
    " fisioterapia tradizionale. Per questo ci affidiamo anche alla"
    " tecnologia, con macchinari e strumenti di ultima generazione che rendono"
    " la nostra fisioterapia moderna ed efficace."
)

APPROACH_PILLARS = [
    (
        "Scienza",
        "Lavoriamo secondo le evidenze scientifiche più aggiornate. Il nostro"
        " team si forma costantemente, insegna e partecipa alla ricerca.",
    ),
    (
        "Ascolto",
        "Ogni percorso parte da una valutazione accurata e dall’ascolto della"
        " persona: la sua storia, i suoi obiettivi, la sua vita quotidiana.",
    ),
    (
        "Movimento",
        "L’esercizio terapeutico è al centro del trattamento. Terapia manuale e"
        " strumenti lo supportano, non lo sostituiscono.",
    ),
    (
        "Misure oggettive",
        "Test funzionali e misurazioni della forza ci permettono di monitorare"
        " i progressi con dati reali e di decidere insieme quando tornare allo"
        " sport.",
    ),
]

# ==============================================================================
# 3. Services (homepage "Servizi" section + servizi.html)
# ==============================================================================
SERVICES = [
    {
        "id": "fisioterapia",
        "title": "Fisioterapia",
        "short": (
            "Riabilitazione muscoloscheletrica, ortopedica e post-operatoria,"
            " con un percorso costruito su di te."
        ),
        "paragraphs": [
            (
                "La fisioterapia si occupa della prevenzione, valutazione e"
                " trattamento delle disfunzioni muscolo-scheletriche causate da"
                " traumi, interventi chirurgici o patologie da sovraccarico."
                " Attraverso tecniche manuali, esercizi terapeutici e protocolli"
                " di recupero mirati basati su misure oggettive, interveniamo"
                " per ristabilire il corretto equilibrio funzionale."
            ),
            (
                "Il percorso è personalizzato in base al problema e agli"
                " obiettivi del paziente: l’obiettivo è recuperare forza,"
                " mobilità e sicurezza nei movimenti, riducendo il rischio di"
                " recidive. Seguiamo anche percorsi di fisioterapia"
                " neurologica, geriatrica e cardio-respiratoria."
            ),
        ],
        "focus_title": "Le nostre aree di riferimento",
        "focus": [
            "Riabilitazione ortopedica e muscoloscheletrica",
            "Riabilitazione post-operatoria",
            "Spalla, ginocchio, anca e rachide cervicale",
            "Dolore cronico e reumatologico",
            "Disturbi dell’articolazione temporo-mandibolare (ATM)",
        ],
    },
    {
        "id": "sportiva",
        "title": "Fisioterapia sportiva",
        "short": (
            "Dall’infortunio al ritorno in campo, con test funzionali e misure"
            " oggettive."
        ),
        "paragraphs": [
            (
                "Che tu sia un atleta professionista o uno sportivo amatoriale,"
                " ti accompagniamo dalla gestione dell’infortunio fino al"
                " ritorno alla pratica sportiva. Il nostro team ha lavorato con"
                " squadre di calcio, rugby e basket, tornei ATP e cliniche"
                " specializzate in traumatologia sportiva."
            ),
            (
                "Il percorso include una fase specifica di return to sport,"
                " strutturata su test funzionali e misure di outcome"
                " scientificamente validate, che consentono di monitorare in"
                " modo oggettivo i progressi e garantire un ritorno sicuro,"
                " efficace e duraturo allo sport."
            ),
        ],
        "focus_title": "Ideale per",
        "focus": [
            "Lesioni muscolari, legamentose e tendinee",
            "Riabilitazione dopo ricostruzione del LCA",
            "Infortuni da corsa e da sovraccarico",
            "Test di forza e criteri di ritorno allo sport",
        ],
    },
    {
        "id": "domicilio",
        "title": "Fisioterapia a domicilio",
        "short": (
            "Se lo studio è lontano, viene il terapista: stessa qualità, a"
            " casa tua."
        ),
        "paragraphs": [
            (
                "La fisioterapia a domicilio è pensata per chi ha difficoltà a"
                " raggiungere lo studio, ma desidera ricevere un trattamento di"
                " pari qualità e professionalità. Il fisioterapista si reca"
                " direttamente a casa del paziente, portando con sé"
                " l’attrezzatura necessaria per svolgere le sedute in modo"
                " efficace e sicuro."
            ),
            (
                "Questo servizio permette di mantenere continuità terapeutica,"
                " fondamentale soprattutto dopo interventi chirurgici o in caso"
                " di patologie croniche, in un ambiente familiare e"
                " confortevole."
            ),
        ],
        "focus_title": "Ideale per",
        "focus": [
            "Le prime settimane dopo un intervento",
            "Persone con mobilità ridotta",
            "Pazienti anziani o con patologie croniche",
        ],
    },
    {
        "id": "prevenzione",
        "title": "Prevenzione e Strength &amp; Conditioning",
        "short": (
            "Forza, resistenza e controllo motorio per prevenire gli infortuni"
            " e migliorare la performance."
        ),
        "paragraphs": [
            (
                "Il programma di Strength &amp; Conditioning integra esercizi"
                " di forza, resistenza e controllo motorio con l’obiettivo di"
                " migliorare le prestazioni fisiche e prevenire gli infortuni."
                " È indicato sia per atleti che per chi desidera recuperare o"
                " mantenere una condizione fisica efficiente dopo un periodo di"
                " inattività o un percorso riabilitativo."
            ),
            (
                "Attraverso protocolli personalizzati e progressivi lavoriamo"
                " su potenza, stabilità, coordinazione e mobilità, riducendo il"
                " rischio di recidive e prevenendo squilibri muscolari o"
                " sovraccarichi."
            ),
        ],
        "focus_title": "Ideale per",
        "focus": [
            "Fine del percorso riabilitativo",
            "Preparazione atletica e prevenzione infortuni",
            "Ripresa dell’attività dopo un periodo di stop",
        ],
    },
    {
        "id": "massaggio",
        "title": "Massaggio e linfodrenaggio",
        "short": (
            "Trattamenti manuali per ridurre tensioni, gonfiori ed edemi e"
            " favorire il recupero."
        ),
        "paragraphs": [
            (
                "Il massaggio terapeutico aiuta a ridurre tensioni e"
                " rigidità muscolari, a favorire il recupero dopo l’attività"
                " sportiva e a ritrovare una sensazione di benessere."
            ),
            (
                "Il linfodrenaggio manuale è una tecnica dolce e ritmica che"
                " favorisce il corretto flusso della linfa nel corpo, riducendo"
                " gonfiori, edemi e ritenzione. È particolarmente indicato dopo"
                " interventi chirurgici, traumi o in presenza di insufficienza"
                " linfatica, e ha un effetto rilassante e rigenerante"
                " sull’intero organismo."
            ),
        ],
        "focus_title": "Ideale per",
        "focus": [
            "Gonfiore ed edema dopo intervento o trauma",
            "Insufficienza linfatica",
            "Tensioni muscolari e recupero sportivo",
        ],
    },
]

# ==============================================================================
# 4. Conditions — "Come possiamo aiutarti" / "Cosa trattiamo"
# ==============================================================================
CONDITIONS = [
    {
        "id": "collo-e-schiena",
        "title": "Collo e schiena",
        "short": "Cervicalgia, lombalgia, ernie e dolore irradiato.",
        "paragraphs": [
            (
                "Il dolore al collo e alla schiena è tra i motivi più frequenti"
                " per cui ci si rivolge al fisioterapista. Nella maggior parte"
                " dei casi non è legato a un danno grave, ma può limitare molto"
                " il lavoro, il sonno e lo sport."
            ),
            (
                "Dopo una valutazione accurata, combiniamo terapia manuale,"
                " educazione e un programma di esercizi progressivo per ridurre"
                " il dolore e ritrovare fiducia nel movimento."
            ),
        ],
        "examples": [
            "Cervicalgia e lombalgia, acuta o cronica",
            "Ernia e protrusione discale",
            "Sciatalgia e dolore irradiato al braccio o alla gamba",
            "Colpo di frusta",
            "Riabilitazione dopo intervento alla colonna",
        ],
    },
    {
        "id": "spalla",
        "title": "Spalla",
        "short": "Cuffia dei rotatori, instabilità, spalla congelata.",
        "paragraphs": [
            (
                "Dolore quando muovi il braccio o durante lo sport? La spalla è"
                " un’articolazione molto mobile e per questo vulnerabile a"
                " sovraccarichi, traumi e rigidità."
            ),
            (
                "Lavoriamo su mobilità, forza e controllo con un percorso"
                " graduale che ti riporta ai gesti quotidiani e sportivi."
            ),
        ],
        "examples": [
            "Lesioni e tendinopatie della cuffia dei rotatori",
            "Spalla congelata (capsulite adesiva)",
            "Instabilità e lussazione",
            "Riabilitazione dopo intervento alla spalla",
        ],
    },
    {
        "id": "ginocchio",
        "title": "Ginocchio",
        "short": "LCA, menisco, dolore femoro-rotuleo, protesi.",
        "paragraphs": [
            (
                "Il ginocchio è una delle articolazioni più sollecitate nello"
                " sport e nella vita quotidiana. Trattiamo sia gli infortuni"
                " acuti sia i dolori da sovraccarico e le problematiche"
                " degenerative."
            ),
            (
                "Con esercizi mirati, misure di forza oggettive e test"
                " funzionali seguiamo ogni fase, dal recupero della mobilità"
                " fino al ritorno alla corsa e allo sport."
            ),
        ],
        "examples": [
            "Lesione del legamento crociato anteriore (LCA)",
            "Lesioni meniscali",
            "Dolore femoro-rotuleo",
            "Tendinopatia rotulea",
            "Artrosi e protesi di ginocchio",
        ],
    },
    {
        "id": "caviglia-e-piede",
        "title": "Caviglia e piede",
        "short": "Distorsioni, fascite plantare, tendine d’Achille.",
        "paragraphs": [
            (
                "Una distorsione di caviglia trattata male può diventare un"
                " problema ricorrente. Così come il dolore al tallone o al"
                " tendine d’Achille possono impedire di camminare e correre"
                " senza fastidio."
            ),
            (
                "Lavoriamo con strumenti tecnologici e con esercizi di forza,"
                " equilibrio e propriocezione per diminuire il dolore,"
                " recuperare stabilità e ridurre il rischio di nuovi infortuni."
            ),
        ],
        "examples": [
            "Distorsione e instabilità di caviglia",
            "Fascite plantare",
            "Tendinopatia d’Achille",
            "Recupero dopo fratture e immobilizzazione",
        ],
    },
    {
        "id": "anca-e-inguine",
        "title": "Anca e inguine",
        "short": "Pubalgia, conflitto femoro-acetabolare, protesi d’anca.",
        "paragraphs": [
            (
                "Il dolore all’anca e all’inguine è frequente negli sportivi"
                " che corrono, calciano e cambiano direzione, ma anche in chi"
                " soffre di artrosi o è stato operato."
            ),
            (
                "Una valutazione precisa permette di capire da dove nasce il"
                " dolore e di costruire un programma di carico progressivo per"
                " anca, muscoli adduttori e glutei."
            ),
        ],
        "examples": [
            "Pubalgia e dolore inguinale dell’atleta",
            "Conflitto femoro-acetabolare (FAI)",
            "Tendinopatia glutea",
            "Artrosi e protesi d’anca",
        ],
    },
    {
        "id": "atm",
        "title": "ATM",
        "short": "Dolore alla mandibola, click, bruxismo.",
        "paragraphs": [
            (
                "L’articolazione temporo-mandibolare (ATM) collega la mandibola"
                " al cranio. Dolore alla mascella, click, difficoltà ad aprire"
                " la bocca, bruxismo o mal di testa possono essere legati a un"
                " suo disturbo."
            ),
            (
                "Interveniamo con terapia manuale, esercizi specifici ed"
                " educazione, quando necessario in collaborazione con il"
                " dentista o l’ortodontista."
            ),
        ],
        "examples": [
            "Dolore alla mandibola e ai muscoli masticatori",
            "Click o blocchi articolari",
            "Limitazione nell’apertura della bocca",
            "Bruxismo e cefalea associata",
        ],
    },
    {
        "id": "dolore-cronico",
        "title": "Dolore cronico",
        "short": "Fibromialgia, dolore persistente, patologie reumatiche.",
        "paragraphs": [
            (
                "Le patologie reumatiche e il dolore cronico richiedono un"
                " approccio delicato e continuo, mirato a migliorare la qualità"
                " della vita e ridurre la disabilità."
            ),
            (
                "Il trattamento combina movimento controllato, terapia manuale"
                " ed educazione sul dolore e sullo stile di vita. L’obiettivo è"
                " aiutarti a gestire il dolore, ritrovando equilibrio e"
                " autonomia nelle attività quotidiane."
            ),
        ],
        "examples": [
            "Fibromialgia",
            "Cervicalgie e lombalgie croniche",
            "Dolore articolare cronico e artrosi",
            "Artrite reumatoide",
        ],
    },
    {
        "id": "infortuni-sportivi",
        "title": "Infortuni sportivi",
        "short": "Lesioni muscolari, legamentose e ritorno allo sport.",
        "paragraphs": [
            (
                "Siamo sportivi anche noi, e sappiamo quanto conta tornare in"
                " campo, in pista o in montagna nel minor tempo possibile, ma"
                " senza rischi."
            ),
            (
                "Ogni percorso termina con una fase di return to sport basata"
                " su test funzionali e misure oggettive di forza, per decidere"
                " con dati reali quando sei pronto."
            ),
        ],
        "examples": [
            "Lesioni muscolari (stiramenti, strappi)",
            "Distorsioni e lesioni legamentose",
            "Tendinopatie da sovraccarico",
            "Infortuni da corsa",
        ],
    },
]

# ==============================================================================
# 5. Equipment — "Cosa c'è in studio" (homepage, HUB page, servizi.html)
# ==============================================================================
TOOLS = [
    {
        "id": "tecar",
        "title": "Tecar",
        "short": (
            "Energia a radiofrequenza per aiutare la riduzione di dolore e"
            " infiammazione."
        ),
        "text": (
            "La Tecarterapia utilizza energia elettromagnetica a"
            " radiofrequenza che stimola i tessuti dall’interno, migliorando la"
            " circolazione e riducendo dolore e infiammazione. La integriamo"
            " con la terapia manuale e l’esercizio, soprattutto nelle fasi in"
            " cui il dolore limita il movimento."
        ),
    },
    {
        "id": "onde-d-urto",
        "title": "Onde d’urto",
        "short": (
            "Terapia a onde d’urto extracorporee (ESWT) per favorire i"
            " processi di neovascolarizzazione e rigenerazione tissutale."
        ),
        "text": (
            "Le onde d’urto sono impulsi acustici ad alta energia che stimolano"
            " i processi di riparazione tissutale e la neo-angiogenesi. Sono"
            " utili nel trattamento dell’edema osseo e di alcune patologie"
            " tendinee croniche (come la fascite plantare e la tendinopatia"
            " calcifica della spalla), riducendo efficacemente il dolore e"
            " accelerando la guarigione."
        ),
    },
    {
        "id": "bfr",
        "title": "BFR",
        "short": "Blood Flow Restriction: forza anche con carichi leggeri.",
        "text": (
            "La Blood Flow Restriction Therapy consiste nell’eseguire esercizi"
            " con un parziale blocco del flusso sanguigno,"
            " ottenuto con un bracciale a pressione controllata. Stimola la"
            " crescita muscolare e la forza anche con carichi ridotti,"
            " riducendo lo stress articolare: ideale nelle prime fasi della"
            " riabilitazione."
        ),
    },
    {
        "id": "motion-guidance",
        "title": "Motion Guidance",
        "short": "Feedback visivo per vedere e correggere il movimento.",
        "text": (
            "Un sistema di feedback visivo: un piccolo puntatore laser"
            " applicato al corpo proietta il movimento su un bersaglio, così il"
            " paziente vede e corregge in tempo reale la qualità del gesto."
            " Lo usiamo per allenare controllo motorio, stabilità e"
            " propriocezione, ad esempio di collo, ginocchio e caviglia."
        ),
    },
    {
        "id": "dinamometro",
        "title": "Misurazione con dinamometro",
        "short": "La forza misurata in numeri, non a occhio.",
        "text": (
            "Con il dinamometro misuriamo la forza muscolare in modo"
            " oggettivo. Confrontiamo il lato infortunato con quello sano,"
            " monitoriamo i progressi seduta dopo seduta e usiamo questi dati"
            " come criteri per il ritorno allo sport."
        ),
    },
    {
        "id": "criocompressione",
        "title": "Criocompressione",
        "short": "Freddo e compressione contro dolore e gonfiore.",
        "text": (
            "La criocompressione combina il freddo con una compressione"
            " pneumatica intermittente per ridurre dolore, gonfiore ed edema,"
            " in particolare nelle prime fasi dopo un intervento chirurgico o"
            " un trauma acuto."
        ),
    },
    {
        "id": "nmes",
        "title": "NMES",
        "short": (
            "Elettrostimolazione neuro-muscolare per il reclutamento motorio,"
            " la prevenzione dell’ipotrofia e il recupero della forza"
            " muscolare."
        ),
        "text": (
            "L’elettrostimolazione neuromuscolare (NMES) utilizza impulsi"
            " elettrici per attivare la contrazione dei muscoli, aiutando a"
            " recuperare forza e tono dopo un’immobilizzazione. È"
            " particolarmente utile quando, dopo un intervento o in presenza"
            " di dolore, il corpo limita l’attivazione muscolare (inibizione"
            " muscolare artrogenica)."
        ),
    },
    {
        "id": "taping",
        "title": "Taping e bendaggi",
        "short": "Supporto per articolazioni e muscoli, dentro e fuori dal campo.",
        "text": (
            "Taping neuromuscolare e bendaggi funzionali stabilizzano e"
            " supportano articolazioni e muscoli senza limitarne il movimento."
            " Molto diffusi in ambito sportivo, sono utili anche nel recupero"
            " post-infortunio. Ti aiutiamo anche nella scelta di bendaggi e"
            " tutori adeguati, dall’infortunio al ritorno allo sport."
        ),
    },
]

# ==============================================================================
# 6. Credentials glossary — "Le sigle, spiegate" (team.html)
# ==============================================================================
CREDENTIALS_GLOSSARY = [
    (
        "OMPT",
        "Orthopaedic Manipulative Physical Therapist",
        "Titolo internazionale riconosciuto dall’IFOMPT, ottenuto con un"
        " master universitario in riabilitazione dei disordini"
        " muscoloscheletrici. Indica una formazione avanzata in terapia"
        " manuale, esercizio terapeutico e ragionamento clinico.",
    ),
    (
        "CAS",
        "Certificate of Advanced Studies",
        "Formazione universitaria post-laurea del sistema svizzero. Luca ha"
        " conseguito il CAS in Fisioterapia Muscoloscheletrica alla SUPSI.",
    ),
    (
        "CSCS",
        "Certified Strength and Conditioning Specialist",
        "Certificazione internazionale della NSCA (National Strength and"
        " Conditioning Association) per la programmazione dell’allenamento di"
        " forza e condizionamento, dalla prevenzione alla performance.",
    ),
    (
        "Maitland",
        "Concetto Maitland di terapia manuale",
        "Percorso di formazione in terapia manuale che unisce tecniche di"
        " mobilizzazione a un ragionamento clinico strutturato, con"
        " rivalutazione continua dei risultati.",
    ),
    (
        "Running Injury Specialist",
        "The Running Clinic",
        "Certificazione internazionale dedicata alla prevenzione e al"
        " trattamento degli infortuni da corsa.",
    ),
    (
        "Master",
        "Master universitario post-laurea",
        "Formazione universitaria avanzata dopo la laurea in fisioterapia: nel"
        " nostro team in linfodrenaggio e in biomeccanica clinica e sportiva.",
    ),
]

# ==============================================================================
# 7. Team Members Data (homepage team section + team.html)
#    "credentials" are the short titles shown as tags; "areas" are each
#    therapist's areas of reference.
# ==============================================================================
TEAM_MEMBERS = [
    {
        "slug": "luca-gilardoni",
        "name": "Luca Gilardoni",
        "photo": "assets/images/LUCA_GILARDONI.jpg",
        "credentials": ['OMPT', 'CAS SUPSI'],
        "areas": ['Spalla', 'Rachide cervicale', 'ATM'],
        "paragraphs": [
            (
                "Luca, nato a Sorengo nel 1991 e cresciuto a Valsolda sul lago"
                " di Lugano, è da sempre appassionato di sport. Dopo circa"
                " vent’anni di calcio, alcuni infortuni lo hanno avvicinato al"
                " mondo della fisioterapia. Amante della montagna, ha sciato"
                " per molti anni e dal 2015 si è dedicato alla corsa in"
                " montagna, gareggiando dal 2016 con l’ASD Atletica Pidaggia"
                " 1528 e distinguendosi nelle lunghe distanze nel circuito"
                " italiano e internazionale di Skyrunning."
            ),
            (
                "Laureato in fisioterapia presso l'Università degli studi"
                " dell'Insubria successivamente frequenta e ottiene il titolo"
                " OMPT grazie al Master in riabilitazione dei disordini"
                " muscoloscheletrici presso l'Università di Genova, esperienza"
                " che lo porta ad avere un approccio lavorativo e formativo"
                " molto Evidence-Based."
            ),
            (
                "Dopo, continua la sua formazione universitaria post-laurea"
                " completando il CAS in Fisioterapia Muscoloscheletrica presso"
                " l'Università SUPSI di Lugano."
            ),
            (
                "Frequenta costantemente corsi di aggiornamento in ambito"
                " muscoloscheletrico e sportivo ed ha collaborato a vari studi"
                " di ricerca con pubblicazioni annesse."
            ),
            (
                "Luca inizia la professione presso l’Istituto Ortopedico"
                " Gaetano Pini di Milano, occupandosi di riabilitazione"
                " ortopedica e neurochirurgica. Dal 2015 lavora in Ticino in"
                " uno studio specializzato nella riabilitazione"
                " muscoloscheletrica, dove scopre la possibilità di unire le"
                " sue due passioni: sport e fisioterapia."
            ),
            (
                "Dal 2019 al 2022 segue la riabilitazione dei calciatori"
                " dell’FC Gambarogno Contone, squadra di seconda lega"
                " interregionale svizzera. Successivamente amplia la propria"
                " esperienza nel settore sportivo, approfondendo la"
                " specializzazione nel trattamento di spalla, ginocchio e"
                " distretto cervicale."
            ),
            (
                "Nel suo tempo libero passa il tempo con sua figlia Viola, ama"
                " leggere libri, tifare per il Calcio Como, stare in natura per"
                " osservare paesaggi e viaggiare!"
            ),
        ],
    },
    {
        "slug": "simone-vaccani",
        "name": "Simone Vaccani",
        "photo": "assets/images/SIMONE_VACCANI.jpg",
        "credentials": ['Maitland', 'Running Injury Specialist', 'Certificate Fisioterapia Sportiva'],
        "areas": ['Anca', 'Ginocchio', 'Piede e caviglia'],
        "paragraphs": [
            (
                "Simone, nato a Busto Arsizio (VA) nel 1981, è appassionato di"
                " sport fin da giovane."
            ),
            (
                "Dopo il calcio amatoriale scopre a 18 anni il nuoto, che per"
                " oltre dieci anni diventa il suo principale impegno,"
                " portandolo a conseguire brevetti da istruttore e a gareggiare"
                " nel circuito master, sia in vasca che in acque libere."
            ),
            (
                "Tuttora pratica diversi sport a livello amatoriale quali nuoto"
                " in acque libere, running, mountain bike, snowboard e nel"
                " tempo libero ama fare trekking in montagna con i suoi cani e"
                " la sua famiglia."
            ),
            (
                "Simone si laurea in Fisioterapia all’Università di Varese con"
                " il massimo dei voti, iniziando subito la formazione in"
                " terapia manuale secondo il concetto Maitland, lavorando al"
                " fianco di uno dei docenti più esperti della metodica."
            ),
            (
                "Negli anni sviluppa una solida competenza nell’ambito"
                " ortopedico e sportivo, conseguendo la certificazione"
                " internazionale di Running Injury Specialist di The Running"
                " Clinic, un master in fisioterapia sportiva e diverse"
                " formazioni su problematiche muscolo-scheletriche di anca e"
                " ginocchio."
            ),
            (
                "Nel 2019 si trasferisce a Ortisei, in Alto Adige, per lavorare"
                " alla Dolomiti Sportclinic, centro di riferimento per la"
                " traumatologia sportiva e gli sport invernali. Durante i tre"
                " anni trascorsi lì, collabora con chirurghi in sala operatoria"
                " e segue quotidianamente il recupero di giovani atleti e"
                " professionisti di alto livello, tra cui praticanti di hockey,"
                " sci freestyle, biathlon e pattinaggio artistico."
            ),
            (
                "Dal 2022 Simone si trasferisce in Svizzera, dove continua a"
                " lavorare nella riabilitazione ortopedica e sportiva,"
                " affinando le proprie competenze in particolare nella"
                " riabilitazione dell’articolazione dell’anca e del ginocchio."
            ),
        ],
    },
    {
        "slug": "carola-isella",
        "name": "Carola Isella",
        "photo": "assets/images/CAROLA_ISELLA.jpg",
        "credentials": ['CSCS', 'Maitland', 'Master Linfodrenaggio', 'Pilates Reformer'],
        "areas": ['Fisioterapia sportiva', 'Strength &amp; Conditioning', 'Linfodrenaggio', 'Dolore cronico e scoliosi'],
        "paragraphs": [
            (
                "Carola è nata a Biella (BI) nel 1996. E’ sempre stata una"
                " persona attiva, con una forte passione per lo sport e la"
                " natura. Ex ballerina di danza classica, ha sviluppato un"
                " profondo interesse per il movimento umano e per il recupero"
                " dagli infortuni, che l’ha portata a conseguire la laurea in"
                " Fisioterapia all'università dell'Insubria di Varese."
            ),
            (
                "Dopo aver completato gli studi, Carola ha approfondito la sua"
                " formazione nell’ambito muscolo-scheletrico seguendo il"
                " percorso Maitland. Ha inoltre frequentato numerosi corsi di"
                " fisioterapia sportiva, conseguito la certificazione CSCS"
                " (Certified Strength and Conditioning Specialist) e ottenuto"
                " un master in linfodrenaggio. Nel corso della sua carriera ha"
                " poi ampliato ulteriormente le proprie competenze conseguendo"
                " specifiche qualifiche nel trattamento della scoliosi e del"
                " dolore cronico."
            ),
            (
                "Oggi Carola è dall'altra parte della cattedra: è assistente"
                " docente presso l'università LUDES di Lugano."
            ),
            (
                "Carola ha iniziato subito a lavorare nell’ambito della"
                " riabilitazione muscoloscheletrica e sportiva, arrivando a"
                " ricoprire il ruolo di fisioterapista responsabile per squadre"
                " di rugby e basket di alto livello."
            ),
            (
                "Carola ha maturato una vasta esperienza in molti sport come"
                " rugby, basket, pallavolo e tennis, seguendo tornei ATP e"
                " lavorando in cliniche sportive altamente specializzate e"
                " basate sulle evidenze scientifiche. Nel corso della sua"
                " carriera è diventata anche istruttrice certificata di Pilates"
                " Reformer."
            ),
            (
                "L’approccio di Carola si basa su una pratica evidence-based,"
                " con una forte attenzione a guidare il paziente verso un"
                " recupero completo. Grande importanza viene data"
                " all’educazione del paziente, aiutandolo a comprendere il"
                " proprio infortunio e a gestirlo in modo efficace nel lungo"
                " termine."
            ),
        ],
    },
    {
        "slug": "federico-monzoni",
        "name": "Federico Monzoni",
        "photo": "assets/images/Federico-Monzoni.jpg",
        "credentials": ['Master Biomeccanica Clinica e Sportiva'],
        "areas": ['Analisi biomeccanica e riatletizzazione', 'Running specialist', 'Rachide lombare'],
        "paragraphs": [
            (
                "Federico, nato nelle Marche nel 1999, è da sempre appassionato"
                " di sport e attività all’aria aperta. Le vacanze trascorse sui"
                " Monti Sibillini lo hanno portato fin da bambino a sviluppare"
                " un forte legame con la montagna e ad avvicinarsi al mondo"
                " della Mountain Bike."
            ),
            (
                "Inizia a praticare Downhill in giovane età, e durante la sua"
                " carriera agonistica partecipa a competizioni nazionali e"
                " internazionali, conquistando due titoli italiani nelle"
                " categorie giovanili e un titolo svizzero nel circuito IXS"
                " Swiss Cup. Nel 2016 rappresenta l’Italia ai Campionati del"
                " Mondo di Downhill in Val di Sole."
            ),
            (
                "Terminata l’attività agonistica, intraprende il percorso"
                " universitario in Fisioterapia presso l’Università degli Studi"
                " di Perugia, laureandosi con il massimo dei voti nel novembre"
                " 2021. Durante gli studi ottiene una borsa Erasmus+, che gli"
                " permette di svolgere un tirocinio clinico presso"
                " l’ambulatorio ortopedico dell’Università di Malaga."
            ),
            (
                "Inizia la propria attività clinica in Centro Italia,"
                " occupandosi della riabilitazione di pazienti con patologie"
                " muscolo-scheletriche e neurologiche, sia in fase acuta che"
                " cronica."
            ),
            (
                "Prosegue successivamente la propria formazione attraverso"
                " corsi di perfezionamento in Italia, Svizzera e Inghilterra,"
                " approfondendo in particolare l’ambito muscolo-scheletrico e"
                " sportivo."
            ),
            (
                "Nel 2025 consegue il Master in Biomeccanica Clinica e Sportiva"
                " presso l’Università degli Studi di Camerino, consolidando il"
                " proprio interesse per l’analisi del movimento e la relazione"
                " tra biomeccanica, riabilitazione e performance."
            ),
            (
                "All’inizio del 2026 pubblica inoltre, in qualità di coautore,"
                " il suo primo articolo scientifico dedicato allo studio"
                " dell’arto inferiore, affiancando il ramo della ricerca"
                " scientifica alla sua pratica clinica."
            ),
            (
                "Nel tempo libero ama viaggiare, praticare sport all’aria"
                " aperta e dedicarsi a progetti legati allo sviluppo dello"
                " sport nel territorio."
            ),
        ],
    },
]

TEAM_BANNER_COLUMNS = [
    (
        "Formazione",
        "Master universitari, OMPT, CAS e corsi di aggiornamento continui in"
        " ambito muscoloscheletrico e sportivo: la formazione non si ferma"
        " mai.",
    ),
    (
        "Insegnamento e ricerca",
        "Carola è assistente docente all’università LUDES di Lugano. Luca e"
        " Federico hanno collaborato a studi di ricerca con pubblicazioni"
        " scientifiche.",
    ),
    (
        "Sport",
        "Squadre di calcio, rugby e basket, tornei ATP, una clinica di"
        " traumatologia sportiva nelle Dolomiti. E da atleti: skyrunning,"
        " nuoto master, danza classica e downhill ai Mondiali.",
    ),
]

# Redirects from the previous site structure (old URL -> new URL).
REDIRECTS = {
    "terapie.html": "servizi.html",
    "dove.html": "contatti.html",
    "luca-gilardoni.html": "team.html#luca-gilardoni",
    "simone-vaccani.html": "team.html#simone-vaccani",
    "carola-isella.html": "team.html#carola-isella",
    "federico-monzoni-2.html": "team.html#federico-monzoni",
    "project/fisioterapia-ortopedica-e-sportiva.html": "servizi.html#fisioterapia",
    "project/fisioterapia-post-operatoria.html": "cosa-trattiamo.html#operato",
    "project/fisioterapia-reumatologica-e-trattamento-del-dolore-cronico.html": "cosa-trattiamo.html#dolore-cronico",
    "project/fisioterapia-neurologica.html": "servizi.html#fisioterapia",
    "project/fisioterapia-cardio-respiratoria.html": "servizi.html#fisioterapia",
    "project/fisioterapia-geriatrica.html": "servizi.html#fisioterapia",
    "project/fisioterapia-a-domicilio.html": "servizi.html#domicilio",
    "project/linfodrenaggio.html": "servizi.html#massaggio",
    "project/prevenzione-e-strength-and-conditioning.html": "servizi.html#prevenzione",
    "project/terapia-strumentale.html": "servizi.html#strumenti",
    "project/taping-e-bendaggio-sportivo.html": "servizi.html#strumento-taping",
    "project/elettrostimolazione-nmes.html": "servizi.html#strumento-nmes",
    "project/brf-blood-flow-restriction-therapy.html": "servizi.html#strumento-bfr",
    "project/mtt-mechanical-therapy-and-training.html": "servizi.html#prevenzione",
}


# ==============================================================================
# 8. Small HTML helpers
# ==============================================================================
def whatsapp_url() -> str:
  text = SITE_CONFIG["whatsapp_text"].replace(" ", "%20")
  return f"https://wa.me/{SITE_CONFIG['phone_intl']}?text={text}"


def tel_url() -> str:
  return f"tel:+{SITE_CONFIG['phone_intl']}"


def mailto_url(subject: str = "Prenotazione") -> str:
  subject = subject.replace(" ", "%20")
  return f"mailto:{SITE_CONFIG['email']}?subject={subject}"


WHATSAPP_ICON = (
    '<svg class="icon-wa" viewBox="0 0 24 24" aria-hidden="true"'
    ' focusable="false"><path fill="currentColor" d="M12.04 2C6.58 2 2.13'
    " 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0"
    " 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2Zm0 18.15c-1.48"
    " 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54"
    " 3.7-8.24 8.25-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24"
    " 8.24Zm4.52-6.16c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.13-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17"
    " 0-.43.06-.66.31-.23.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17"
    " 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07"
    " 1.47-.6 1.67-1.18.21-.58.21-1.08.14-1.18-.06-.11-.22-.17-.47-.29Z\"/>"
    "</svg>"
)


def photo(src, alt: str, label: str, cls: str = "") -> str:
  """An image, or a clearly marked placeholder while the photo is missing."""
  if src:
    return (
        f'<figure class="photo {cls}"><img src="{src}" alt="{alt}"'
        ' loading="lazy"></figure>'
    )
  return (
      f'<figure class="photo photo-placeholder {cls}" role="img"'
      f' aria-label="{alt}"><span>{label}</span></figure>'
  )


def btn(href: str, label: str, style: str = "rose", extra: str = "") -> str:
  return f'<a class="btn btn-{style}" href="{href}"{extra}>→ {label}</a>'


def book_btn(style: str = "rose") -> str:
  return btn(SITE_CONFIG["booking_url"], "Prenota appuntamento", style)


def section_title(text: str, tag: str = "h2") -> str:
  return f'<{tag} class="section-title"><span class="accent-arrow">→</span> {text}</{tag}>'


def bullet_list(items, cls: str = "arrow-list") -> str:
  lis = "\n".join(
      f'              <li><span class="accent-arrow">→</span> {i}</li>'
      for i in items
  )
  return f'<ul class="{cls}">\n{lis}\n            </ul>'


def paragraphs(items, indent: int = 12) -> str:
  pad = " " * indent
  return "\n".join(f"{pad}<p>{p}</p>" for p in items)


def page_hero(title: str, lead: str, extra_html: str = "") -> str:
  return f"""    <section class="page-hero">
      <div class="container page-hero-inner fade-in-up">
        {section_title(title, "h1")}
        {f'<p class="lead">{lead}</p>' if lead else ""}
        {extra_html}
      </div>
    </section>"""


def tools_grid(detailed: bool) -> str:
  cards = []
  for i, t in enumerate(TOOLS, 1):
    body = t["text"] if detailed else t["short"]
    cards.append(f"""          <article class="tool-card" id="strumento-{t['id']}">
            <span class="card-num">{i:02d}</span>
            <h3>{t['title']}</h3>
            <p>{body}</p>
          </article>""")
  cls = "tool-grid tool-grid--detailed" if detailed else "tool-grid"
  return f'<div class="{cls}">\n' + "\n".join(cards) + "\n        </div>"


def tools_band(detailed: bool, intro: str, cta: str = "",
               color: str = "orange") -> str:
  """color: "orange", "teal" (white text, orange details) or "rose"."""
  return f"""    <section class="band band-{color} tools-band" id="strumenti">
      <div class="container">
        <div class="section-head">
          {section_title("Cosa c’è in studio")}
          <p class="section-intro">{intro}</p>
        </div>
        {tools_grid(detailed)}
        {cta}
      </div>
    </section>"""


def chips(items) -> str:
  return '<ul class="chips">' + "".join(f"<li>{c}</li>" for c in items) + "</ul>"


def contact_block() -> str:
  c = SITE_CONFIG
  return f"""<div class="contact-block">
            <p class="contact-address">
              <span class="hl">{c['company']}</span><br>
              {c['address_line_1']}<br>
              {c['address_line_2']}
            </p>
            <ul class="contact-links">
              <li><a href="{whatsapp_url()}" target="_blank" rel="noopener">{WHATSAPP_ICON}<span>WhatsApp <strong>{c['phone_display']}</strong></span></a></li>
              <li><a href="{tel_url()}"><span class="contact-ico" aria-hidden="true">☎</span><span>Telefono <strong>{c['phone_display']}</strong></span></a></li>
              <li><a href="mailto:{c['email']}"><span class="contact-ico" aria-hidden="true">@</span><span>Email <strong>{c['email']}</strong></span></a></li>
            </ul>
          </div>"""


def map_embed() -> str:
  return f"""<div class="map-wrap">
            <iframe title="Mappa FisioHub Lugano - {SITE_CONFIG['address_line_1']}" loading="lazy" src="{SITE_CONFIG['map_embed_url']}"></iframe>
          </div>"""


# ==============================================================================
# 9. Shared HTML Layout Template
# ==============================================================================
def render_page(
    *,
    title: str,
    description: str,
    theme_class: str,
    logo_file: str,
    body_html: str,
    active_nav: str = "",
) -> str:
  """Wraps page content with the shared header, mobile menu and footer."""
  c = SITE_CONFIG
  nav_lis = []
  overlay_lis = []
  for label, href in c["nav_items"]:
    is_active = label.lower() == active_nav.lower()
    cur = ' aria-current="page"' if is_active else ""
    act = ' class="active"' if is_active else ""
    nav_lis.append(f'          <li><a href="{href}"{act}{cur}>{label}</a></li>')
    overlay_lis.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
  nav_html = "\n".join(nav_lis)
  overlay_html = "\n".join(overlay_lis)

  return f"""<!DOCTYPE html>
<html lang="it-IT">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Fisio Hub Lugano</title>
  <meta name="description" content="{description}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="{c['site_name']}">
  <meta property="og:title" content="{title} - Fisio Hub Lugano">
  <meta property="og:description" content="{description}">
  <link rel="icon" href="assets/images/favicon-32x32.png" sizes="32x32">
  <link rel="icon" href="assets/images/favicon-192x192.png" sizes="192x192">
  <link rel="apple-touch-icon" href="assets/images/favicon-180x180.png">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body class="{theme_class}">

  <!-- Shared Header & Navigation -->
  <header class="site-header">
    <div class="nav-container">
      <a class="nav-logo" href="index.html" aria-label="Fisio Hub - Home">
        <img class="logo-top" src="assets/logos/{logo_file}" alt="Fisio Hub">
        <img class="logo-scrolled" src="assets/logos/FisioHub_blu.svg" alt="" aria-hidden="true">
      </a>
      <nav class="nav-menu" aria-label="Menu principale">
        <ul class="nav-list">
{nav_html}
        </ul>
      </nav>
      <div class="nav-actions">
        <a class="nav-phone" href="{whatsapp_url()}" target="_blank" rel="noopener" aria-label="Scrivici su WhatsApp al {c['phone_display']}">
          {WHATSAPP_ICON}<span class="nav-phone-num">{c['phone_display']}</span>
        </a>
        <button id="mobile-menu-open" class="hamburger-btn" aria-label="Apri menu" aria-controls="mobile-overlay" aria-expanded="false">
          <span></span>
        </button>
      </div>
    </div>

    <!-- Mobile Overlay Menu -->
    <div id="mobile-overlay" class="mobile-overlay" aria-hidden="true">
      <button id="mobile-menu-close" class="overlay-close-btn" aria-label="Chiudi menu">
        <svg width="18" height="18" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M1 1L7 7M7 1L1 7" stroke="white" stroke-width="1.2" stroke-linecap="round"/>
        </svg>
      </button>
      <ul class="overlay-nav-list">
{overlay_html}
      </ul>
      <a class="overlay-phone" href="{whatsapp_url()}" target="_blank" rel="noopener">{WHATSAPP_ICON} {c['phone_display']}</a>
    </div>
  </header>

  <!-- Main Page Content -->
  <main class="page-main">
{body_html}
  </main>

  <!-- Shared Footer -->
  <footer class="site-footer">
    <div class="footer-grid">
      <div class="footer-col">
        <p>
          <span class="footer-brand">{c['company']}</span><br>
          {c['address_line_1']}<br>
          {c['address_line_2']}
        </p>
      </div>
      <div class="footer-col">
        <p>
          <a href="{tel_url()}">{c['phone_display']}</a><br>
          <a href="mailto:{c['email']}">{c['email']}</a>
        </p>
      </div>
      <div class="footer-col footer-cta">
        {book_btn("navy")}
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp button -->
  <a class="wa-float" href="{whatsapp_url()}" target="_blank" rel="noopener" aria-label="Scrivici su WhatsApp">
    <img src="assets/images/whatsapp.png" alt="">
  </a>

  <script src="js/main.js"></script>
</body>
</html>
"""


def render_redirect(old_path: str, new_url: str) -> str:
  depth = old_path.count("/")
  target = "../" * depth + new_url
  return f"""<!DOCTYPE html>
<html lang="it-IT">
<head>
  <meta charset="UTF-8">
  <title>Fisio Hub Lugano</title>
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
</head>
<body>
  <p>Questa pagina è stata spostata: <a href="{target}">continua qui</a>.</p>
</body>
</html>
"""


def write_page(rel_path: str, content: str) -> None:
  full_path = os.path.join(BASE_DIR, rel_path)
  os.makedirs(os.path.dirname(full_path), exist_ok=True)
  with open(full_path, "w", encoding="utf-8") as f:
    f.write(content)
  print(f"Generated {rel_path}")


# ==============================================================================
# 10. Page Builders
# ==============================================================================
def build_home() -> str:
  c = SITE_CONFIG

  service_rows = "\n".join(
      f"""          <a class="row-link" href="servizi.html#{s['id']}">
            <span class="row-num">{i:02d}</span>
            <span class="row-title">{s['title']}</span>
            <span class="row-text">{s['short']}</span>
            <span class="row-arrow" aria-hidden="true">→</span>
          </a>"""
      for i, s in enumerate(SERVICES, 1)
  )

  condition_tiles = "\n".join(
      f"""          <a class="tile" href="cosa-trattiamo.html#{x['id']}">
            <h3>{x['title']}</h3>
            <p>{x['short']}</p>
            <span class="tile-arrow" aria-hidden="true">→</span>
          </a>"""
      for x in CONDITIONS
  )

  team_cards = "\n".join(
      f"""          <a class="team-card" href="team.html#{m['slug']}">
            <img src="{m['photo']}" width="1000" height="1043" alt="{m['name']}">
            <h3><span class="accent-arrow">→</span> {m['name']}</h3>
            {chips(m['credentials'])}
            <p class="team-areas">{" · ".join(m['areas'])}</p>
          </a>"""
      for m in TEAM_MEMBERS
  )

  return f"""    <section class="hero-cover">
      <div class="hero-video-wrapper">
        <video autoplay playsinline loop muted>
          <source src="assets/video/Comp-1_12_mute.mp4" type="video/mp4">
        </video>
      </div>
      <div class="container hero-grid">
        <div class="hero-logo-col fade-in-up">
          <img src="assets/logos/FisioHub_blu.svg" alt="Fisio Hub Lugano">
        </div>
        <div class="hero-content-col">
          <h1 class="hero-title fade-in-up">
            <span class="text-rose">FISIOHUB LUGANO</span><br>
            <span class="text-navy">IL PUNTO D’INCONTRO<br>TRA SCIENZA, ASCOLTO<br>E MOVIMENTO</span>
          </h1>
          <p class="hero-lead fade-in-up">
            Fisioterapia e fitness di qualità nel cuore di Lugano.<br>
            Riconosciuti da tutte le casse malati, senza bisogno di prescrizione medica.
          </p>
          <div class="hero-buttons fade-in-left">
            <a id="btn-book-home" class="btn-action btn-rose" href="{c['booking_url']}">→ PRENOTA APPUNTAMENTO</a>
            <a id="btn-approach-home" class="btn-action btn-rose btn-secondary" href="hub.html#approccio">→ SCOPRI IL NOSTRO APPROCCIO</a>
          </div>
        </div>
      </div>
    </section>

    <section class="band band-navy" id="hub">
      <div class="container split">
        <div class="split-text">
          {section_title("L’Hub")}
{paragraphs(HUB_PARAGRAPHS)}
            <p>{APPROACH_INTRO}</p>
          {btn("hub.html", "Scopri lo studio", "outline-light")}
        </div>
        <div class="split-media">
          {photo(STUDIO_PHOTOS['main'], "Lo studio FisioHub a Lugano", "Foto dello studio")}
        </div>
      </div>
    </section>

    <section class="band band-teal" id="servizi">
      <div class="container">
        <div class="section-head">
          {section_title("Servizi")}
          <p class="section-intro">Fisioterapia moderna, con un’attenzione particolare alle nostre aree di specializzazione: ortopedia, sport e riabilitazione post-operatoria.</p>
        </div>
        <div class="row-list">
{service_rows}
        </div>
      </div>
    </section>

    <section class="band band-navy" id="cosa-trattiamo">
      <div class="container">
        <div class="section-head">
          {section_title("Come possiamo aiutarti?")}
          <p class="section-intro">Alcuni dei problemi che trattiamo ogni giorno in studio.</p>
        </div>
        <div class="tile-grid">
{condition_tiles}
        </div>
      </div>
    </section>

{tools_band(False, "Tecnologie di ultima generazione per un percorso riabilitativo avanzato.", btn("servizi.html#strumenti", "Gli strumenti spiegati", "outline-light"), "teal")}

    <section class="band band-rose" id="team">
      <div class="container">
        <div class="section-head">
          {section_title("I tuoi esperti")}
          <p class="section-intro">Quattro fisioterapisti con una formazione universitaria avanzata e un’esperienza costruita nello sport.</p>
        </div>
        <div class="team-grid">
{team_cards}
        </div>
      </div>
    </section>

    <section class="band band-lake" id="dove">
      <div class="container split">
        <div class="split-text">
          {section_title("Dove siamo")}
          {contact_block()}
          {book_btn()}
        </div>
        <div class="split-media">
          {map_embed()}
        </div>
      </div>
    </section>"""


def build_hub() -> str:
  pillars = "\n".join(
      f"""          <div class="pillar">
            <span class="card-num">{i:02d}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>"""
      for i, (t, d) in enumerate(APPROACH_PILLARS, 1)
  )
  gallery = "\n".join(
      "          " + photo(STUDIO_PHOTOS[k], "Lo studio FisioHub", "Foto dello studio")
      for k in ("gallery_1", "gallery_2", "gallery_3")
  )
  return f"""{page_hero("L’Hub", "Un punto d’incontro tra scienza, ascolto e movimento, nel cuore di Lugano.")}

    <section class="band band-white" id="studio">
      <div class="container split">
        <div class="split-text">
          {section_title("Lo studio")}
{paragraphs(HUB_PARAGRAPHS)}
        </div>
        <div class="split-media">
          {photo(STUDIO_PHOTOS['main'], "Lo studio FisioHub a Lugano", "Foto dello studio")}
        </div>
      </div>
      <div class="container gallery">
{gallery}
      </div>
    </section>

    <section class="band band-navy" id="approccio">
      <div class="container">
        <div class="section-head">
          {section_title("Il nostro approccio")}
          <p class="section-intro">{APPROACH_INTRO}</p>
        </div>
        <div class="pillar-grid">
{pillars}
        </div>
      </div>
    </section>

{tools_band(True, "Gli strumenti che usiamo ogni giorno, spiegati in breve. Sempre integrati con l’esercizio e la terapia manuale.", color="rose")}"""


def build_servizi() -> str:
  blocks = []
  for i, s in enumerate(SERVICES, 1):
    blocks.append(f"""        <article class="detail" id="{s['id']}">
          <div class="detail-head">
            <span class="card-num">{i:02d}</span>
            <h2>{s['title']}</h2>
          </div>
          <div class="detail-body">
{paragraphs(s['paragraphs'])}
          </div>
          <div class="detail-side">
            <h3>{s['focus_title']}</h3>
            {bullet_list(s['focus'])}
            {btn(SITE_CONFIG["booking_url"], "Prenota", "teal")}
          </div>
        </article>""")
  return f"""{page_hero("Servizi", "")}

    <section class="band band-white">
      <div class="container detail-list">
{chr(10).join(blocks)}
      </div>
    </section>

{tools_band(True, "Gli strumenti che usiamo ogni giorno, spiegati in breve. Sempre integrati con l’esercizio e la terapia manuale.", color="teal")}"""


def build_cosa_trattiamo() -> str:
  blocks = []
  for i, x in enumerate(CONDITIONS, 1):
    blocks.append(f"""        <article class="detail" id="{x['id']}">
          <div class="detail-head">
            <span class="card-num">{i:02d}</span>
            <h2>{x['title']}</h2>
          </div>
          <div class="detail-body">
{paragraphs(x['paragraphs'])}
          </div>
          <div class="detail-side">
            <h3>Trattiamo ad esempio</h3>
            {bullet_list(x['examples'])}
          </div>
        </article>""")
    if i == 4:
      blocks.append("        <!--BANNER_OPERATO-->")
  body = "\n".join(blocks)

  banner_operato = f"""      </div>
    </section>

    <section class="banner banner-rose" id="operato">
      <div class="container banner-inner">
        <div>
          <p class="banner-kicker">Riabilitazione post-operatoria</p>
          <h2>Ti hanno operato?</h2>
          <p>Protesi d’anca o di ginocchio, ricostruzione del LCA, cuffia dei rotatori, colonna vertebrale: ti seguiamo in tutte le fasi, dalla gestione del dolore e del gonfiore fino al ritorno alle tue attività. Con criocompressione, NMES e BFR fin dalle prime settimane, e a domicilio se serve.</p>
        </div>
        <div class="banner-actions">{book_btn("navy")}</div>
      </div>
    </section>

    <section class="banner banner-navy" id="sala-operatoria">
      <div class="container banner-inner banner-inner--media">
        <div>
          <p class="banner-kicker">Dentro la sala operatoria</p>
          <h2>Sappiamo cosa succede in sala operatoria.</h2>
          <p>I nostri fisioterapisti vanno spesso in sala operatoria, collaborando con i chirurghi per costruire una riabilitazione coerente con il loro lavoro e accompagnare il paziente con una fisioterapia di qualità.</p>
          {btn("team.html", "Conosci il team", "outline-light")}
        </div>
        {photo(STUDIO_PHOTOS['sala_operatoria'], "I fisioterapisti di FisioHub in sala operatoria", "Foto in sala operatoria", "banner-photo")}
      </div>
    </section>

    <section class="band band-white">
      <div class="container detail-list">"""
  body = body.replace("        <!--BANNER_OPERATO-->", banner_operato)

  return f"""{page_hero("Cosa trattiamo", "Dal collo alla caviglia, dal dolore cronico all’infortunio sportivo: ecco come possiamo aiutarti.")}

    <section class="band band-white">
      <div class="container detail-list">
{body}
      </div>
    </section>

    <section class="banner banner-teal">
      <div class="container banner-inner">
        <h2>Non trovi il tuo problema? Scrivici.</h2>
        <div class="banner-actions">{btn(whatsapp_url(), "WhatsApp", "outline-light", ' target="_blank" rel="noopener"')} {book_btn("navy")}</div>
      </div>
    </section>"""


def build_team() -> str:
  bios = []
  for m in TEAM_MEMBERS:
    first, rest = m["paragraphs"][:2], m["paragraphs"][2:]
    bios.append(f"""        <article class="bio" id="{m['slug']}">
          <div class="bio-photo">
            <img src="{m['photo']}" width="1000" height="1043" alt="{m['name']}" loading="lazy">
          </div>
          <div class="bio-text">
            <h2><span class="accent-arrow">→</span> {m['name']}</h2>
            {chips(m['credentials'])}
            <p class="bio-areas"><strong>Aree di riferimento:</strong> {" · ".join(m['areas'])}</p>
{paragraphs(first)}
            <details class="bio-more">
              <summary>Leggi tutta la biografia</summary>
{paragraphs(rest, 14)}
            </details>
          </div>
        </article>""")

  glossary = "\n".join(
      f"""          <div class="gloss">
            <h3>{abbr}</h3>
            <p class="gloss-full">{full}</p>
            <p>{desc}</p>
          </div>"""
      for abbr, full, desc in CREDENTIALS_GLOSSARY
  )
  banner_cols = "\n".join(
      f"""          <div>
            <h3><span class="accent-arrow">→</span> {t}</h3>
            <p>{d}</p>
          </div>"""
      for t, d in TEAM_BANNER_COLUMNS
  )

  return f"""{page_hero("Il team", "Fisioterapisti con formazione universitaria avanzata, che vivono lo sport in prima persona.")}

    <section class="band band-white">
      <div class="container bio-list">
{chr(10).join(bios)}
      </div>
    </section>

    <section class="band band-navy" id="sigle">
      <div class="container">
        <div class="section-head">
          {section_title("Le sigle, spiegate")}
          <p class="section-intro">Cosa significano i titoli accanto ai nostri nomi.</p>
        </div>
        <div class="gloss-grid">
{glossary}
        </div>
      </div>
    </section>

    <section class="banner banner-rose" id="formazione">
      <div class="container">
        <h2 class="banner-title">Formazione, insegnamento e sport</h2>
        <div class="banner-cols">
{banner_cols}
        </div>
      </div>
    </section>"""


def build_contatti() -> str:
  return f"""{page_hero("Contatti", "Scrivici su WhatsApp, chiamaci o mandaci una email: ti rispondiamo il prima possibile.")}

    <section class="band band-white">
      <div class="container split">
        <div class="split-text">
          {section_title("Dove siamo")}
          {contact_block()}
          <div class="btn-row">
            {btn(whatsapp_url(), "Scrivici su WhatsApp", "rose", ' target="_blank" rel="noopener"')}
            {btn(mailto_url(), "Mandaci una email", "navy")}
          </div>
          <p class="small"><a href="{SITE_CONFIG['map_link_url']}" target="_blank" rel="noopener">→ Apri in Google Maps</a></p>
        </div>
        <div class="split-media">
          {map_embed()}
        </div>
      </div>
    </section>

    <section class="banner banner-rose" id="domicilio">
      <div class="container banner-inner">
        <div>
          <p class="banner-kicker">Fisioterapia a domicilio</p>
          <h2>Se lo studio è lontano, viene il terapista.</h2>
          <p>Dopo un intervento, con mobilità ridotta o semplicemente se non riesci a raggiungerci: il fisioterapista viene a casa tua con l’attrezzatura necessaria.</p>
        </div>
        <div class="banner-actions">{btn("servizi.html#domicilio", "Scopri il servizio", "navy")}</div>
      </div>
    </section>"""


def build_insta() -> str:
  return f"""{page_hero("Social", "Seguici su Instagram per sbirciare la vita in studio e trovare consigli per la tua riabilitazione.")}

    <section class="band band-white">
      <div class="container">
        <script src="https://elfsightcdn.com/platform.js" async></script>
        <div class="elfsight-app-fbefbcda-4027-463d-99c1-13c3c4f3b81c" data-elfsight-app-lazy></div>
      </div>
    </section>"""


def build_all() -> None:
  pages = [
      ("index.html", "Home",
       "FisioHub Lugano: il punto d’incontro tra scienza, ascolto e movimento."
       " Fisioterapia e fitness di qualità nel cuore di Lugano.",
       "theme-home", "FisioHub_blu.svg", build_home(), ""),
      ("hub.html", "Hub",
       "Lo studio FisioHub a Lugano: il nostro approccio e gli strumenti che"
       " usiamo.",
       "theme-hub", "FisioHub.svg", build_hub(), "Hub"),
      ("servizi.html", "Servizi",
       "Fisioterapia, fisioterapia sportiva, a domicilio, prevenzione e"
       " strength &amp; conditioning, massaggio e linfodrenaggio a Lugano.",
       "theme-servizi", "FisioHub_giallo.svg", build_servizi(), "Servizi"),
      ("cosa-trattiamo.html", "Cosa trattiamo",
       "Collo e schiena, spalla, ginocchio, caviglia, anca, ATM, dolore"
       " cronico e infortuni sportivi: cosa trattiamo a FisioHub Lugano.",
       "theme-trattiamo", "FisioHub_verde.svg", build_cosa_trattiamo(),
       "Cosa trattiamo"),
      ("team.html", "Il team",
       "Il team di FisioHub Lugano: Luca Gilardoni, Simone Vaccani, Carola"
       " Isella e Federico Monzoni.",
       "theme-team", "FisioHub_BLuw.svg", build_team(), "Il team"),
      ("insta.html", "Social", "Segui FisioHub Lugano su Instagram.",
       "theme-insta", "FisioHub.svg", build_insta(), "Social"),
      ("contatti.html", "Contatti",
       "Contatti e indirizzo di FisioHub SA, Via Carlo Maderno 26, 6900"
       " Lugano. WhatsApp, telefono ed email.",
       "theme-contatti", "FisioHub.svg", build_contatti(), "Contatti"),
  ]
  for path, title, desc, theme, logo, body, active in pages:
    write_page(path, render_page(
        title=title, description=desc, theme_class=theme, logo_file=logo,
        body_html=body, active_nav=active,
    ))

  for old, new in REDIRECTS.items():
    write_page(old, render_redirect(old, new))


if __name__ == "__main__":
  build_all()
