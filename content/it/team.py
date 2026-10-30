"""Team: bios, credentials glossary and banner on team.html (Italian).

"credentials" are the short titles shown as tags; "areas" are each
therapist's areas of reference. Keep slug, name and photo identical across
languages."""

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
