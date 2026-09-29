#!/usr/bin/env python3
"""Static Site Generator for Fisio Hub Lugano (https://fisiohub.ch).

Generates all 24 static HTML pages (Home, HUB, Terapie, Team, Insta, Dove,
4 Team Member biography pages, and 14 Therapy detail pages) from a single
shared layout and data definition.

Usage:
  python3 build.py
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# 1. Shared Site Configuration (Edit here to update across all 24 pages)
# ==============================================================================
SITE_CONFIG = {
    "site_name": "Fisio Hub - Fisioterapia moderna Lugano",
    "company": "FisioHub SA",
    "address_line_1": "Via Carlo Maderno, 26",
    "address_line_2": "6900 Lugano.",
    "phone_display": "079 8396900",
    "phone_whatsapp": "+410798396900",
    "email": "info@fisiohub.ch",
    "nav_items": [
        ("HUB", "hub.html"),
        ("Terapie", "terapie.html"),
        ("Team", "team.html"),
        ("Insta", "insta.html"),
        ("Dove", "dove.html"),
    ],
}

# ==============================================================================
# 2. Team Members Data (Used on team.html and individual biography pages)
# ==============================================================================
TEAM_MEMBERS = [
    {
        "slug": "luca-gilardoni",
        "name": "Luca Gilardoni",
        "photo": "assets/images/LUCA_GILARDONI.jpg",
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
        "slug": "federico-monzoni-2",
        "name": "Federico Monzoni",
        "photo": "assets/images/Federico-Monzoni.jpg",
        "paragraphs": [
            (
                "Federico, nato nelle Marche nel 1999, è da sempre appassionato"
                " di sport e attività all’aria aperta. Le vacanze trascorse sui"
                " Monti Sibillini lo hanno portato fin da bambino a sviluppare"
                " un forte legame con la montagna e ad avvicarsi al mondo"
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

# ==============================================================================
# 3. Therapies Data (Used on terapie.html and project/*.html detail pages)
# ==============================================================================
THERAPIES = [
    {
        "slug": "fisioterapia-ortopedica-e-sportiva",
        "list_title": "FISIOTERAPIA ORTOPEDICA E SPORTIVA",
        "page_title": "FISIOTERAPIA ORTOPEDICA E SPORTIVA",
        "subject": "Fisioterapia ortopedica e sportiva",
        "paragraphs": [
            (
                "La fisioterapia ortopedica e sportiva si occupa della"
                " prevenzione, valutazione e trattamento delle disfunzioni"
                " muscolo-scheletriche causate da traumi o patologie da"
                " sovraccarico. Attraverso tecniche manuali, esercizi"
                " terapeutici e protocolli di recupero mirati basati su misure"
                " oggettive, si interviene per ristabilire il corretto"
                " equilibrio funzionale. Il percorso riabilitativo è"
                " personalizzato in base al tipo di infortunio e agli obiettivi"
                " del paziente, sia esso un atleta o una persona che desidera"
                " tornare alle proprie attività quotidiane. L’obiettivo è"
                " recuperare la forza, la mobilità e la sicurezza nei"
                " movimenti, riducendo il rischio di recidive e migliorando la"
                " performance fisica complessiva. In caso di pazienti sportivi,"
                " il percorso include una fase specifica di return to sport,"
                " strutturata su test funzionali e misure di outcome"
                " scientificamente validate, che consentono di monitorare in"
                " modo oggettivo i progressi e garantire un ritorno sicuro,"
                " efficace e duraturo alla pratica sportiva."
            ),
        ],
        "pathologies": [
            "Tendinopatie",
            "Lesioni meniscali ed LCA del ginocchio",
            "Lesioni della cuffia dei rotatori della spalla",
            "Cervicalgie e Lombalgie",
            "Epicondilite",
            "Fascite plantare",
        ],
    },
    {
        "slug": "fisioterapia-post-operatoria",
        "list_title": "FISIOTERAPIA POST OPERATORIA",
        "page_title": "FISIOTERAPIA POST OPERATORIA",
        "subject": "Fisioterapia post operatoria",
        "paragraphs": [
            (
                "Dopo un intervento chirurgico, la riabilitazione è"
                " fondamentale per favorire un recupero completo e sicuro. La"
                " fisioterapia post-operatoria interviene in tutte le fasi del"
                " percorso, dalla gestione del dolore e del gonfiore fino al"
                " ripristino della mobilità, della forza e della funzionalità"
                " del distretto trattato."
            ),
            (
                "Attraverso un piano personalizzato, il fisioterapista"
                " accompagna il paziente in un percorso graduale e controllato,"
                " favorendo la guarigione dei tessuti e prevenendo complicanze"
                " come rigidità articolare (artrofibrosi), atrofia muscolare o"
                " aderenze cicatriziali. L’obiettivo è tornare progressivamente"
                " alle normali attività quotidiane con piena fiducia nel"
                " proprio corpo."
            ),
        ],
        "pathologies": [
            "Interventi di protesi di anca o ginocchio",
            "Ricostruzione LCA o artroscopie di ginocchio",
            "Intervento di riparazione della cuffia dei rotatori",
            "Interventi sulla colonna vertebrale",
        ],
    },
    {
        "slug": "fisioterapia-reumatologica-e-trattamento-del-dolore-cronico",
        "list_title": "FISIOTERAPIA REUMATOLOGICA E TRATTAMENTO DOLORE CRONICO",
        "page_title": (
            "FISIOTERAPIA REUMATOLOGICA E TRATTAMENTO DEL DOLORE CRONICO"
        ),
        "subject": (
            "Fisioterapia reumatologica e trattamento del dolore cronico"
        ),
        "paragraphs": [
            (
                "Le patologie reumatiche e il dolore cronico richiedono un"
                " approccio delicato e continuo, mirato a migliorare la qualità"
                " della vita e ridurre la disabilità."
            ),
            (
                "Il trattamento del dolore cronico si basa su strategie"
                " multidisciplinari che combinano movimento controllato,"
                " rilassamento miofasciale e educazione sul cambiamento dello"
                " stile di vita. L’obiettivo è aiutare il paziente a gestire il"
                " dolore, ritrovando equilibrio e autonomia nelle attività"
                " quotidiane."
            ),
        ],
        "pathologies": [
            "Fibromialgia",
            "Cervicalgie o lombalgie croniche",
            "Dolore articolare cronico",
            "Artrite reumatoide",
        ],
    },
    {
        "slug": "fisioterapia-neurologica",
        "list_title": "FISIOTERAPIA NEUROLOGICA",
        "page_title": "FISIOTERAPIA NEUROLOGICA",
        "subject": "Fisioterapia neurologica",
        "paragraphs": [
            (
                "La fisioterapia neurologica è dedicata alle persone che"
                " presentano disturbi del sistema nervoso centrale o"
                " periferico. Attraverso un approccio personalizzato e basato"
                " sull’evidenza scientifica, il fisioterapista lavora per"
                " migliorare controllo motorio, equilibrio, coordinazione e"
                " forza."
            ),
            (
                "Il trattamento include esercizi di stimolazione neuromotoria,"
                " tecniche di rieducazione funzionale e strategie di compenso"
                " per favorire l’autonomia. L’obiettivo è aiutare ogni paziente"
                " a raggiungere il massimo potenziale di recupero, migliorando"
                " la qualità della vita e l’indipendenza nei gesti quotidiani."
            ),
        ],
        "pathologies": [
            "Ictus",
            "Sclerosi multipla",
            "Morbo di Parkinson",
            "Neuropatie",
        ],
    },
    {
        "slug": "fisioterapia-cardio-respiratoria",
        "list_title": "FISIOTERAPIA CARDIO-RESPIRATORIA",
        "page_title": "FISIOTERAPIA CARDIO RESPIRATORIA",
        "subject": "Fisioterapia cardio-respiratoria",
        "paragraphs": [
            (
                "Questa branca della fisioterapia è rivolta a persone con"
                " patologie cardiache o respiratori. Gli esercizi e le tecniche"
                " respiratorie proposte mirano a migliorare la ventilazione"
                " polmonare, la capacità aerobica e la resistenza allo sforzo."
            ),
            (
                "Il percorso di riabilitazione cardio-respiratoria aiuta a"
                " gestire meglio la fatica, migliorare la tolleranza"
                " all’esercizio e recuperare una migliore qualità della vita."
                " Grazie a una guida costante, il paziente impara a conoscere e"
                " utilizzare in modo più efficiente le proprie risorse"
                " respiratorie e cardiache."
            ),
        ],
        "pathologies": [
            "BPCO",
            "Asma",
            "Insufficienza cardiaca",
            "Post-intervento toracico",
        ],
    },
    {
        "slug": "fisioterapia-geriatrica",
        "list_title": "FISIOTERAPIA GERIATRICA",
        "page_title": "FISIOTERAPIA GERIATRICA",
        "subject": "Fisioterapia geriatrica",
        "paragraphs": [
            (
                "Con l’avanzare dell’età, mantenere la mobilità e l’autonomia"
                " diventa fondamentale per una buona qualità della vita. La"
                " fisioterapia geriatrica si concentra sulla prevenzione delle"
                " cadute, sul miglioramento dell’equilibrio e sul recupero"
                " della forza muscolare."
            ),
            (
                "Attraverso esercizi personalizzati e un approccio attento ai"
                " bisogni della persona anziana, il fisioterapista aiuta a"
                " preservare indipendenza e sicurezza nei movimenti."
            ),
            (
                "L’obiettivo è promuovere un invecchiamento attivo, riducendo"
                " il dolore articolare e migliorando la funzionalità"
                " quotidiana."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "fisioterapia-a-domicilio",
        "list_title": "FISIOTERAPIA A DOMICILIO",
        "page_title": "FISIOTERAPIA A DOMICILIO",
        "subject": "Fisioterapia a domicilio",
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
                " di patologie croniche. Il paziente può così lavorare sul"
                " recupero in un ambiente familiare e confortevole, favorendo"
                " una riabilitazione più serena e personalizzata."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "linfodrenaggio",
        "list_title": "LINFODRENAGGIO",
        "page_title": "LINFODRENAGGIO",
        "subject": "Linfodrenaggio",
        "paragraphs": [
            (
                "Il linfodrenaggio manuale è una tecnica dolce e ritmica che"
                " favorisce il corretto flusso della linfa nel corpo, riducendo"
                " gonfiori, edemi e ritenzione. È particolarmente indicato dopo"
                " interventi chirurgici, traumi o in presenza di insufficienza"
                " linfatica."
            ),
            (
                "Oltre a migliorare la circolazione e la depurazione dei"
                " tessuti, questa tecnica ha un effetto rilassante e"
                " rigenerante sull’intero organismo. Il trattamento dona una"
                " sensazione di leggerezza e benessere, contribuendo al"
                " recupero funzionale. Può alleviare il disagio, ridurre"
                " l’infiammazione e migliorare la circolazione, favorendo una"
                " guarigione più rapida e migliorando la salute generale."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "prevenzione-e-strength-and-conditioning",
        "list_title": "PREVENZIONE E STRENGTH AND CONDITIONING",
        "page_title": "PREVENZIONE E STRENGTH AND CONDITIONING",
        "subject": "Prevenzione e Strength and Conditioning",
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
                "Attraverso protocolli personalizzati e progressivi, il"
                " fisioterapista lavora su potenza, stabilità, coordinazione e"
                " mobilità, adattando ogni esercizio alle caratteristiche e"
                " agli obiettivi individuali."
            ),
            (
                "Questo approccio permette non solo di ottimizzare la"
                " performance, ma anche di ridurre il rischio di recidive e"
                " prevenire squilibri muscolari o sovraccarichi, favorendo un"
                " corpo più forte, armonico e pronto ad affrontare le sfide"
                " quotidiane o sportive."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "terapia-strumentale",
        "list_title": "TERAPIA STRUMENTALE",
        "page_title": "TERAPIA STRUMENTALE",
        "subject": "Terapia Strumentale",
        "paragraphs": [
            (
                "La terapia strumentale si avvale di tecnologie avanzate come"
                " Tecar e onde d’urto per accelerare i processi di guarigione."
                " Questi strumenti permettono di ridurre dolore e"
                " infiammazione, migliorando la circolazione e la rigenerazione"
                " dei tessuti."
            ),
            (
                "Integrata con la terapia manuale e gli esercizi riabilitativi,"
                " la terapia strumentale potenzia gli effetti del trattamento,"
                " favorendo un recupero più rapido e duraturo."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "taping-e-bendaggio-sportivo",
        "list_title": "TAPING E BENDAGGIO SPORTIVO",
        "page_title": "TAPING E BENDAGGIO SPORTIVO",
        "subject": "Taping e bendaggio sportivo",
        "paragraphs": [
            (
                "Taping neuromuscolare e i bendaggi funzionali vengono"
                " utilizzati per stabilizzare e supportare articolazioni e"
                " muscoli, sono tecniche molto diffuse in ambito sportivo, ma"
                " utili anche nel recupero post-infortunio. Ti assistiamo nella"
                " scelta di bendaggi e tutori adeguati, dal momento"
                " dell’infortunio fino alla fase di ritorno allo sport."
            ),
            (
                "Oltre a sostenere i tessuti senza limitarne il movimento, il"
                " taping stimola la circolazione linfatica e contribuisce alla"
                " riduzione dell’infiammazione. È un valido alleato nel"
                " percorso di guarigione e nella prevenzione delle recidive."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "elettrostimolazione-nmes",
        "list_title": "ELETTROSTIMOLAZIONE NMES",
        "page_title": "ELETTROSTIMOLAZIONE NMES",
        "subject": "Elettrostimolazione NMES",
        "paragraphs": [
            (
                "L’elettrostimolazione neuromuscolare (NMES) utilizza impulsi"
                " elettrici per attivare la contrazione dei muscoli, aiutando a"
                " mantenere o recuperare forza e tono in caso di"
                " immobilizzazione o atrofia."
            ),
            (
                "E’ particolarmente importante in casi di inibizione muscolare"
                " artrogenica, una condizione in cui il corpo limita"
                " l’attivazione muscolare a seguito di un intervento chirurgico"
                " o in presenza di condizioni dolorose. Integrata a esercizi"
                " attivi, contribuisce a un recupero più rapido ed efficace."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "brf-blood-flow-restriction-therapy",
        "list_title": "BRF (BLOOD FLOW RESTRICTION THERAPY)",
        "page_title": "BRF – BLOOD FLOW RESTRICTION THERAPY",
        "subject": "BRF – Blood Flow Restriction Therapy",
        "paragraphs": [
            (
                "La Blood Flow Restriction Therapy è una metodica innovativa"
                " che consiste nell’eseguire esercizi a bassa intensità con un"
                " parziale blocco del flusso sanguigno. Questo stimola la"
                " crescita muscolare e la forza anche con carichi ridotti,"
                " rendendola ideale nella fase riabilitativa."
            ),
            (
                "Sotto il controllo del fisioterapista, la BRF permette di"
                " ottenere risultati simili all’allenamento tradizionale in"
                " modo sicuro e progressivo, riducendo lo stress articolare e"
                " accelerando i tempi di recupero."
            ),
        ],
        "pathologies": [],
    },
    {
        "slug": "mtt-mechanical-therapy-and-training",
        "list_title": "MTT (MECHANICAL THERAPY AND TRAINING)",
        "page_title": "MTT – MECHANICAL THERAPY AND TRAINING",
        "subject": "MTT – Mechanical Therapy and Training",
        "paragraphs": [
            (
                "La Mechanical Therapy and Training (MTT) è un approccio"
                " riabilitativo basato sull’esercizio terapeutico assistito da"
                " macchinari e resistenze controllate. È indicata per il"
                " recupero funzionale dopo traumi, interventi o periodi di"
                " immobilità."
            ),
            (
                "Attraverso un programma progressivo e personalizzato, il"
                " paziente lavora su forza, mobilità e controllo motorio in"
                " modo sicuro e monitorato. L’obiettivo è migliorare la"
                " funzionalità e prevenire recidive, favorendo un ritorno"
                " graduale all’attività quotidiana o sportiva."
            ),
        ],
        "pathologies": [],
    },
]


# ==============================================================================
# 4. Shared HTML Layout Template
# ==============================================================================
def render_page(
    *,
    title: str,
    description: str,
    theme_class: str,
    logo_file: str,
    body_html: str,
    root_prefix: str = "",
    active_nav: str = "",
) -> str:
  """Wraps page content with the shared Fisio Hub header, mobile menu, and footer."""
  nav_lis = []
  overlay_lis = []
  for label, href in SITE_CONFIG["nav_items"]:
    active_cls = ' class="active"' if label.lower() == active_nav.lower() else ""
    nav_lis.append(
        f'          <li><a href="{root_prefix}{href}"{active_cls}>{label}</a></li>'
    )
    overlay_lis.append(
        f'        <li><a href="{root_prefix}{href}">{label}</a></li>'
    )

  nav_html = "\n".join(nav_lis)
  overlay_html = "\n".join(overlay_lis)

  return f"""<!DOCTYPE html>
<html lang="it-IT">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Fisio Hub</title>
  <meta name="description" content="{description}">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="{SITE_CONFIG['site_name']}">
  <meta property="og:title" content="{title} - Fisio Hub">
  <link rel="icon" href="{root_prefix}assets/images/favicon-32x32.png" sizes="32x32">
  <link rel="icon" href="{root_prefix}assets/images/favicon-192x192.png" sizes="192x192">
  <link rel="apple-touch-icon" href="{root_prefix}assets/images/favicon-180x180.png">
  <link rel="stylesheet" href="{root_prefix}css/styles.css">
</head>
<body class="{theme_class}">

  <!-- Shared Header & Navigation -->
  <header class="site-header">
    <div class="nav-container">
      <div class="nav-logo-wrap">
        <a href="{root_prefix}index.html" aria-label="Fisio Hub Home">
          <img src="{root_prefix}assets/logos/{logo_file}" alt="Fisio Hub Logo">
        </a>
      </div>
      <nav class="nav-menu-wrap" aria-label="Menu principale">
        <ul class="nav-list">
{nav_html}
        </ul>
        <button id="mobile-menu-open" class="hamburger-btn" aria-label="Apri menu">
          <span></span>
        </button>
      </nav>
      <div class="nav-spacer" aria-hidden="true"></div>
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
    </div>
  </header>

  <!-- Main Page Content -->
  <main class="page-main">
{body_html}
  </main>

  <!-- Shared Fixed Footer -->
  <footer class="site-footer">
    <div class="footer-grid">
      <div class="footer-col">
        <p>
          <span class="footer-brand">{SITE_CONFIG['company']}</span><br>
          {SITE_CONFIG['address_line_1']}<br>
          {SITE_CONFIG['address_line_2']}
        </p>
      </div>
      <div class="footer-col">
        <p>
          <a href="tel:{SITE_CONFIG['phone_whatsapp']}">{SITE_CONFIG['phone_display']}</a><br>
          <a href="mailto:{SITE_CONFIG['email']}">{SITE_CONFIG['email']}</a>
        </p>
      </div>
      <div class="footer-col footer-whatsapp">
        <a href="https://api.whatsapp.com/send?phone={SITE_CONFIG['phone_whatsapp']}&amp;text=Buongiorno" target="_blank" rel="noopener noreferrer" aria-label="Contattaci su WhatsApp">
          <img src="{root_prefix}assets/images/whatsapp.png" alt="WhatsApp">
        </a>
      </div>
    </div>
  </footer>

  <script src="{root_prefix}js/main.js"></script>
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
# 5. Page Builders
# ==============================================================================
def build_all() -> None:
  # 1. Home (index.html)
  home_body = """    <section class="hero-cover">
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
          <div class="hero-buttons fade-in-left">
            <a id="btn-book-home" class="btn-action btn-rose" href="mailto:info@fisiohub.ch?subject=Prenotazione&amp;body=Buongiorno,%20vorrei%20effettuare%20una%20prenotazione%20per....%20Grazie">
              → PRENOTA APPUNTAMENTO
            </a>
            <a id="btn-services-home" class="btn-action btn-rose btn-services" href="terapie.html">
              → SCOPRI SERVIZI
            </a>
          </div>
        </div>
      </div>
    </section>"""
  write_page(
      "index.html",
      render_page(
          title="Home",
          description=(
              "Fisio Hub Lugano: il punto d'incontro tra scienza, ascolto e"
              " movimento. Fisioterapia moderna a Lugano."
          ),
          theme_class="theme-home",
          logo_file="FisioHub_blu.svg",
          body_html=home_body,
      ),
  )

  # 2. HUB (hub.html)
  hub_body = """    <section class="content-section">
      <div class="container">
        <div class="content-col-5 fade-in-right">
          <h1><span class="accent-arrow">→</span> L'HUB</h1>
          <p>
            FisioHub nasce dall’idea di tre colleghi uniti dalla passione per la fisioterapia e da una visione comune: mettere al centro il benessere reale della persona. Il nome <span class="text-rose">“Hub” rappresenta un punto di connessione,</span> il luogo in cui la scienza incontra l’esperienza, dove metodo e ascolto si fondono per costruire percorsi terapeutici efficaci e personalizzati. Crediamo in una fisioterapia basata sulle evidenze scientifiche, ma profondamente attenta all’unicità di ogni individuo.
            <br><br>
            <span class="text-rose">Ogni paziente viene accompagnato passo dopo passo verso i propri obiettivi,</span> per ritrovare equilibrio, movimento e uno stile di vita più sano.
          </p>
          <p>
            Il nostro simbolo, una “H” minimale ed essenziale, vuole rappresentare proprio questo: un hub centrale, il luogo in cui percorsi, competenze e persone si incontrano per dare vita a un recupero completo, continuo e consapevole.
          </p>
          <p>
            <span class="text-rose">Il nostro approccio vuole essere contemporaneo, affidabile,</span> orientato al movimento e lontano dai cliché della fisioterapia tradizionale. Per questo ci affidiamo anche alla tecnologia, con macchinari e strumenti di ultima generazione che rendono la nostra fisioterapia moderna ed efficace.
          </p>
        </div>
      </div>
    </section>"""
  write_page(
      "hub.html",
      render_page(
          title="HUB",
          description=(
              "Scopri FisioHub Lugano: fisioterapia moderna basata sulle"
              " evidenze scientifiche e orientata al movimento."
          ),
          theme_class="theme-hub",
          logo_file="FisioHub.svg",
          body_html=hub_body,
          active_nav="HUB",
      ),
  )

  # 3. Terapie Index (terapie.html)
  terapie_links = []
  for t in THERAPIES:
    terapie_links.append(
        f'            <li><a href="project/{t["slug"]}.html"><span'
        f' class="accent-arrow">→</span> {t["list_title"]}</a></li>'
    )
  terapie_links_html = "\n".join(terapie_links)
  terapie_body = f"""    <section class="content-section">
      <div class="container">
        <div class="content-col-5 fade-in-right">
          <h1><span class="accent-arrow">→</span> LE TERAPIE</h1>
          <ul class="terapie-list">
{terapie_links_html}
          </ul>
        </div>
      </div>
    </section>"""
  write_page(
      "terapie.html",
      render_page(
          title="Terapie",
          description=(
              "Le terapie di Fisio Hub Lugano: fisioterapia ortopedica,"
              " sportiva, post-operatoria, neurologica, linfodrenaggio e"
              " terapia strumentale."
          ),
          theme_class="theme-terapie",
          logo_file="FisioHub_giallo.svg",
          body_html=terapie_body,
          active_nav="Terapie",
      ),
  )

  # 4. Team Index (team.html) & Individual Team Member Bio Pages
  team_cards = []
  for m in TEAM_MEMBERS:
    team_cards.append(f"""          <a class="team-card fade-in-up" href="{m['slug']}.html">
            <img src="{m['photo']}" width="1000" height="1043" alt="{m['name']}">
            <h2><span class="accent-arrow">→</span> {m['name'].upper()}</h2>
          </a>""")
  team_cards_html = "\n".join(team_cards)
  team_body = f"""    <section class="team-section">
      <div class="container">
        <div class="team-grid">
{team_cards_html}
        </div>
      </div>
    </section>"""
  write_page(
      "team.html",
      render_page(
          title="Team",
          description=(
              "Il team di fisioterapisti di Fisio Hub Lugano: Luca Gilardoni,"
              " Simone Vaccani, Carola Isella e Federico Monzoni."
          ),
          theme_class="theme-team",
          logo_file="FisioHub_BLuw.svg",
          body_html=team_body,
          active_nav="Team",
      ),
  )

  for m in TEAM_MEMBERS:
    paras_html = "\n".join(f"            <p>{p}</p>" for p in m["paragraphs"])
    bio_body = f"""    <section class="content-section">
      <div class="container">
        <div class="bio-grid">
          <div class="bio-photo fade-in-up">
            <img src="{m['photo']}" width="1000" height="1043" alt="{m['name']}">
          </div>
          <div class="bio-text fade-in-right">
            <h1><span class="accent-arrow">→</span> {m['name'].upper()}</h1>
{paras_html}
          </div>
        </div>
      </div>
    </section>"""
    write_page(
        f"{m['slug']}.html",
        render_page(
            title=m["name"],
            description=f"{m['name']} - Fisioterapista presso Fisio Hub Lugano.",
            theme_class="theme-team",
            logo_file="FisioHub_BLuw.svg",
            body_html=bio_body,
            active_nav="Team",
        ),
    )

  # 5. Insta (insta.html)
  insta_body = """    <section class="content-section">
      <div class="container">
        <div class="content-col-7 fade-in-up">
          <script src="https://elfsightcdn.com/platform.js" async></script>
          <div class="elfsight-app-fbefbcda-4027-463d-99c1-13c3c4f3b81c" data-elfsight-app-lazy></div>
        </div>
      </div>
    </section>"""
  write_page(
      "insta.html",
      render_page(
          title="Insta",
          description="Segui Fisio Hub Lugano su Instagram.",
          theme_class="theme-insta",
          logo_file="FisioHub.svg",
          body_html=insta_body,
          active_nav="Insta",
      ),
  )

  # 6. Dove (dove.html)
  dove_body = """    <section class="content-section">
      <div class="container">
        <div class="content-col-6 dove-contact fade-in-up">
          <h1><span class="accent-arrow">→</span> DOVE SIAMO</h1>
          <p>
            <span class="text-rose">FisioHub SA</span><br>
            Via Carlo Maderno, 26<br>
            6900 Lugano.
          </p>
          <p>
            <a href="tel:+410798396900">079 8396900</a><br>
            <a href="mailto:info@fisiohub.ch">info@fisiohub.ch</a>
          </p>
          <div class="embed-map-responsive">
            <iframe
              class="embed-map-frame"
              title="Mappa FisioHub Lugano - Via Carlo Maderno 26"
              loading="lazy"
              src="https://maps.google.com/maps?width=650&amp;height=450&amp;hl=it&amp;q=lugano%20Via%20Carlo%20Maderno%2C%2026&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed">
            </iframe>
          </div>
        </div>
      </div>
    </section>"""
  write_page(
      "dove.html",
      render_page(
          title="Dove",
          description=(
              "Dove trovarci: FisioHub SA, Via Carlo Maderno 26, 6900 Lugano."
          ),
          theme_class="theme-dove",
          logo_file="FisioHub.svg",
          body_html=dove_body,
          active_nav="Dove",
      ),
  )

  # 7. Therapy Detail Pages (project/*.html)
  num_therapies = len(THERAPIES)
  for idx, t in enumerate(THERAPIES):
    prev_t = THERAPIES[(idx - 1) % num_therapies]
    next_t = THERAPIES[(idx + 1) % num_therapies]

    paras_html = "\n".join(f"          <p>{p}</p>" for p in t["paragraphs"])
    pathologies_html = ""
    if t["pathologies"]:
      items = "\n".join(
          f'            <li><span class="accent-arrow">→</span> {item}</li>'
          for item in t["pathologies"]
      )
      pathologies_html = f"""          <p>Alcune delle patologie che trattiamo sono:</p>
          <ul class="pathology-list">
{items}
          </ul>"""

    mailto_href = (
        f"mailto:info@fisiohub.ch?subject=Prenotazione per {t['subject']}"
        "&amp;body=Buongiorno, vorrei effettuare una prenotazione per il"
        " trattamento in oggetto. Grazie"
    )

    project_body = f"""    <section class="content-section">
      <div class="container">
        <div class="content-col-6 fade-in-right">
          <h1><span class="accent-arrow">→</span> {t['page_title']}</h1>
{paras_html}
{pathologies_html}
          <div>
            <a id="btn-book-{t['slug']}" class="btn-action btn-teal" href="{mailto_href}">
              → PRENOTA APPUNTAMENTO
            </a>
          </div>
        </div>
      </div>
    </section>

    <nav class="project-nav-wrapper" aria-label="Navigazione terapie">
      <a class="project-nav-prev" href="{prev_t['slug']}.html">
        <span>&larr;</span> <span>Previous</span>
      </a>
      <a class="project-nav-next" href="{next_t['slug']}.html">
        <span>&rarr;</span> <span>Next</span>
      </a>
    </nav>"""

    write_page(
        f"project/{t['slug']}.html",
        render_page(
            title=t["subject"],
            description=f"{t['subject']} presso Fisio Hub Lugano.",
            theme_class="theme-project",
            logo_file="FisioHub_verde.svg",
            body_html=project_body,
            root_prefix="../",
            active_nav="Terapie",
        ),
    )


if __name__ == "__main__":
  build_all()
