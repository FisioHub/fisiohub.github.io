"""Interface text (Italian): header, footer, buttons, headings, banners,
page titles and meta descriptions.

Values may contain simple HTML (<br>, <span>) and entities (&amp;); keep the
markup and the {placeholders} as they are when translating.
"""

UI = {
    # --- <head> and language -------------------------------------------------
    "html_lang": "it-IT",
    "og_locale": "it_IT",
    "site_name": "Fisio Hub - Fisioterapia moderna Lugano",
    # Language of the Google Maps embed (2-letter code)
    "map_hl": "it",

    # --- Navigation (keyed by page file) -------------------------------------
    "nav": {
        "hub.html": "Hub",
        "servizi.html": "Servizi",
        "cosa-trattiamo.html": "Cosa trattiamo",
        "team.html": "Il team",
        "insta.html": "Social",
        "contatti.html": "Contatti",
    },
    "nav_aria": "Menu principale",
    "home_aria": "Fisio Hub - Home",
    "menu_open": "Apri menu",
    "menu_close": "Chiudi menu",
    "lang_switch_aria": "Lingua",
    "whatsapp_aria_phone": "Scrivici su WhatsApp al {phone}",
    "whatsapp_aria": "Scrivici su WhatsApp",

    # --- Shared bits ---------------------------------------------------------
    "whatsapp_text": "Buongiorno, vorrei prenotare un appuntamento.",
    "mail_subject": "Prenotazione",
    "book": "Prenota appuntamento",
    "book_short": "Prenota",
    "phone_label": "Telefono",
    "map_title": "Mappa FisioHub Lugano",
    "tools_title": "Cosa c’è in studio",
    "tools_intro_short": (
        "Tecnologie di ultima generazione per un percorso riabilitativo"
        " avanzato."
    ),
    "tools_intro_detailed": (
        "Gli strumenti che usiamo ogni giorno, spiegati in breve. Sempre"
        " integrati con l’esercizio e la terapia manuale."
    ),
    "tools_cta": "Gli strumenti spiegati",
    "photo_studio_alt": "Lo studio FisioHub a Lugano",
    "photo_studio_alt_short": "Lo studio FisioHub",
    "photo_studio_label": "Foto dello studio",
    "dove_title": "Dove siamo",

    # --- Homepage ------------------------------------------------------------
    "home_logo_alt": "Fisio Hub Lugano",
    "home_hero_kicker": "FISIOHUB LUGANO",
    "home_hero_title": "IL PUNTO D’INCONTRO<br>TRA SCIENZA, ASCOLTO<br>E MOVIMENTO",
    "home_hero_lead": (
        "Fisioterapia e fitness di qualità nel cuore di Lugano.<br>\n"
        "            Riconosciuti da tutte le casse malati, senza bisogno di"
        " prescrizione medica."
    ),
    "home_btn_book": "PRENOTA APPUNTAMENTO",
    "home_btn_approach": "SCOPRI IL NOSTRO APPROCCIO",
    "home_hub_title": "L’Hub",
    "home_hub_cta": "Scopri lo studio",
    "home_services_title": "Servizi",
    "home_services_intro": (
        "Fisioterapia moderna, con un’attenzione particolare alle nostre aree"
        " di specializzazione: ortopedia, sport e riabilitazione"
        " post-operatoria."
    ),
    "home_conditions_title": "Come possiamo aiutarti?",
    "home_conditions_intro": (
        "Alcuni dei problemi che trattiamo ogni giorno in studio."
    ),
    "home_team_title": "I tuoi esperti",
    "home_team_intro": (
        "Quattro fisioterapisti con una formazione universitaria avanzata e"
        " un’esperienza costruita nello sport."
    ),

    # --- HUB page ------------------------------------------------------------
    "hub_hero_title": "L’Hub",
    "hub_hero_lead": (
        "Un punto d’incontro tra scienza, ascolto e movimento, nel cuore di"
        " Lugano."
    ),
    "hub_studio_title": "Lo studio",
    "hub_approach_title": "Il nostro approccio",

    # --- Servizi page --------------------------------------------------------
    "services_hero_title": "Servizi",

    # --- Cosa trattiamo page -------------------------------------------------
    "conditions_hero_title": "Cosa trattiamo",
    "conditions_hero_lead": (
        "Dal collo alla caviglia, dal dolore cronico all’infortunio sportivo:"
        " ecco come possiamo aiutarti."
    ),
    "conditions_examples_title": "Trattiamo ad esempio",
    "postop_kicker": "Riabilitazione post-operatoria",
    "postop_title": "Ti hanno operato?",
    "postop_text": (
        "Protesi d’anca o di ginocchio, ricostruzione del LCA, cuffia dei"
        " rotatori, colonna vertebrale: ti seguiamo in tutte le fasi, dalla"
        " gestione del dolore e del gonfiore fino al ritorno alle tue attività."
        " Con criocompressione, NMES e BFR fin dalle prime settimane, e a"
        " domicilio se serve."
    ),
    "or_kicker": "Dentro la sala operatoria",
    "or_title": "Sappiamo cosa succede in sala operatoria.",
    "or_text": (
        "I nostri fisioterapisti vanno spesso in sala operatoria, collaborando"
        " con i chirurghi per costruire una riabilitazione coerente con il loro"
        " lavoro e accompagnare il paziente con una fisioterapia di qualità."
    ),
    "or_cta": "Conosci il team",
    "or_photo_alt": "I fisioterapisti di FisioHub in sala operatoria",
    "or_photo_label": "Foto in sala operatoria",
    "not_found_title": "Non trovi il tuo problema? Scrivici.",

    # --- Team page -----------------------------------------------------------
    "team_hero_title": "Il team",
    "team_hero_lead": (
        "Fisioterapisti con formazione universitaria avanzata, che vivono lo"
        " sport in prima persona."
    ),
    "team_areas_label": "Aree di riferimento:",
    "team_read_more": "Leggi tutta la biografia",
    "glossary_title": "Le sigle, spiegate",
    "glossary_intro": "Cosa significano i titoli accanto ai nostri nomi.",
    "team_banner_title": "Formazione, insegnamento e sport",

    # --- Contatti page -------------------------------------------------------
    "contact_hero_title": "Contatti",
    "contact_hero_lead": (
        "Scrivici su WhatsApp, chiamaci o mandaci una email: ti rispondiamo il"
        " prima possibile."
    ),
    "contact_btn_whatsapp": "Scrivici su WhatsApp",
    "contact_btn_email": "Mandaci una email",
    "contact_open_maps": "Apri in Google Maps",
    "home_visit_kicker": "Fisioterapia a domicilio",
    "home_visit_title": "Se lo studio è lontano, viene il terapista.",
    "home_visit_text": (
        "Dopo un intervento, con mobilità ridotta o semplicemente se non riesci"
        " a raggiungerci: il fisioterapista viene a casa tua con l’attrezzatura"
        " necessaria."
    ),
    "home_visit_cta": "Scopri il servizio",

    # --- Social page ---------------------------------------------------------
    "social_hero_title": "Social",
    "social_hero_lead": (
        "Seguici su Instagram per sbirciare la vita in studio e trovare"
        " consigli per la tua riabilitazione."
    ),

    # --- Page <title> and meta description (keyed by page file) --------------
    "pages": {
        "index.html": (
            "Home",
            "FisioHub Lugano: il punto d’incontro tra scienza, ascolto e"
            " movimento. Fisioterapia e fitness di qualità nel cuore di Lugano.",
        ),
        "hub.html": (
            "Hub",
            "Lo studio FisioHub a Lugano: il nostro approccio e gli strumenti"
            " che usiamo.",
        ),
        "servizi.html": (
            "Servizi",
            "Fisioterapia, fisioterapia sportiva, a domicilio, prevenzione e"
            " strength &amp; conditioning, massaggio e linfodrenaggio a Lugano.",
        ),
        "cosa-trattiamo.html": (
            "Cosa trattiamo",
            "Collo e schiena, spalla, ginocchio, caviglia, anca, ATM, dolore"
            " cronico e infortuni sportivi: cosa trattiamo a FisioHub Lugano.",
        ),
        "team.html": (
            "Il team",
            "Il team di FisioHub Lugano: Luca Gilardoni, Simone Vaccani, Carola"
            " Isella e Federico Monzoni.",
        ),
        "insta.html": (
            "Social",
            "Segui FisioHub Lugano su Instagram.",
        ),
        "contatti.html": (
            "Contatti",
            "Contatti e indirizzo di FisioHub SA, Via Carlo Maderno 26, 6900"
            " Lugano. WhatsApp, telefono ed email.",
        ),
    },
}
