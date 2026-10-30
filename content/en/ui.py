"""Interface text (English): header, footer, buttons, headings, banners,
page titles and meta descriptions.

Values may contain simple HTML (<br>, <span>) and entities (&amp;); keep the
markup and the {placeholders} as they are when translating.
"""

UI = {
    # --- <head> and language -------------------------------------------------
    "html_lang": "en",
    "og_locale": "en_GB",
    "site_name": "Fisio Hub - Modern Physiotherapy Lugano",
    # Language of the Google Maps embed (2-letter code)
    "map_hl": "en",

    # --- Navigation (keyed by page file) -------------------------------------
    "nav": {
        "hub.html": "Hub",
        "servizi.html": "Services",
        "cosa-trattiamo.html": "What we treat",
        "team.html": "The team",
        "insta.html": "Social",
        "contatti.html": "Contact",
    },
    "nav_aria": "Main menu",
    "home_aria": "Fisio Hub - Home",
    "menu_open": "Open menu",
    "menu_close": "Close menu",
    "lang_switch_aria": "Language",
    "whatsapp_aria_phone": "Message us on WhatsApp at {phone}",
    "whatsapp_aria": "Message us on WhatsApp",

    # --- Shared bits ---------------------------------------------------------
    "whatsapp_text": "Hello, I would like to book an appointment.",
    "mail_subject": "Booking",
    "book": "Book an appointment",
    "book_short": "Book",
    "phone_label": "Phone",
    "map_title": "FisioHub Lugano map",
    "tools_title": "What’s in the studio",
    "tools_intro_short": (
        "State-of-the-art technology for an advanced rehabilitation"
        " journey."
    ),
    "tools_intro_detailed": (
        "The tools we use every day, explained briefly. Always combined with"
        " exercise and manual therapy."
    ),
    "tools_cta": "Explore our tools",
    "photo_studio_alt": "The FisioHub studio in Lugano",
    "photo_studio_alt_short": "The FisioHub studio",
    "photo_studio_label": "Studio photo",
    "dove_title": "Where we are",

    # --- Homepage ------------------------------------------------------------
    "home_logo_alt": "Fisio Hub Lugano",
    "home_hero_kicker": "FISIOHUB LUGANO",
    "home_hero_title": "THE MEETING POINT<br>BETWEEN SCIENCE, LISTENING<br>AND MOVEMENT",
    "home_hero_lead": (
        "Quality physiotherapy and fitness in the heart of Lugano.<br>\n"
        "            Recognised by all health insurers, no doctor’s referral"
        " needed."
    ),
    "home_btn_book": "BOOK AN APPOINTMENT",
    "home_btn_approach": "DISCOVER OUR APPROACH",
    "home_hub_title": "The Hub",
    "home_hub_cta": "Discover the studio",
    "home_services_title": "Services",
    "home_services_intro": (
        "Modern physiotherapy, with particular focus on our areas of"
        " specialisation: orthopaedics, sport and post-operative"
        " rehabilitation."
    ),
    "home_conditions_title": "How can we help you?",
    "home_conditions_intro": (
        "Some of the conditions we treat every day in the studio."
    ),
    "home_team_title": "Your experts",
    "home_team_intro": (
        "Four physiotherapists with advanced university training and"
        " experience built in sport."
    ),

    # --- HUB page ------------------------------------------------------------
    "hub_hero_title": "The Hub",
    "hub_hero_lead": (
        "A meeting point between science, listening and movement, in the heart"
        " of Lugano."
    ),
    "hub_studio_title": "The studio",
    "hub_approach_title": "Our approach",

    # --- Servizi page --------------------------------------------------------
    "services_hero_title": "Services",

    # --- Cosa trattiamo page -------------------------------------------------
    "conditions_hero_title": "What we treat",
    "conditions_hero_lead": (
        "From the neck to the ankle, from chronic pain to sports injuries:"
        " here’s how we can help you."
    ),
    "conditions_examples_title": "For example, we treat",
    "postop_kicker": "Post-operative rehabilitation",
    "postop_title": "Have you had surgery?",
    "postop_text": (
        "Hip or knee replacement, ACL reconstruction, rotator cuff, spine: we"
        " support you through every phase, from managing pain and swelling to"
        " getting back to your activities. With cryo-compression, NMES and BFR"
        " from the first weeks, and home visits if needed."
    ),
    "or_kicker": "Inside the operating theatre",
    "or_title": "We know what happens in the operating theatre.",
    "or_text": (
        "Our physiotherapists often work in the operating theatre, collaborating"
        " with surgeons to build rehabilitation that fits their work and to"
        " guide the patient through quality physiotherapy."
    ),
    "or_cta": "Meet the team",
    "or_photo_alt": "FisioHub physiotherapists in the operating theatre",
    "or_photo_label": "Operating theatre photo",
    "not_found_title": "Can’t find your problem? Get in touch.",

    # --- Team page -----------------------------------------------------------
    "team_hero_title": "The team",
    "team_hero_lead": (
        "Physiotherapists with advanced university training who live sport"
        " first-hand."
    ),
    "team_areas_label": "Areas of focus:",
    "team_read_more": "Read the full biography",
    "glossary_title": "Our credentials, explained",
    "glossary_intro": "What the titles next to our names mean.",
    "team_banner_title": "Training, teaching and sport",

    # --- Contatti page -------------------------------------------------------
    "contact_hero_title": "Contact",
    "contact_hero_lead": (
        "Message us on WhatsApp, call us or send us an email: we’ll get back to"
        " you as soon as possible."
    ),
    "contact_btn_whatsapp": "Message us on WhatsApp",
    "contact_btn_email": "Email us",
    "contact_open_maps": "Open in Google Maps",
    "home_visit_kicker": "Home physiotherapy",
    "home_visit_title": "If the studio is far away, the physiotherapist comes to you.",
    "home_visit_text": (
        "After an operation, with reduced mobility, or simply if you can’t get"
        " to us: the physiotherapist comes to your home with the necessary"
        " equipment."
    ),
    "home_visit_cta": "Discover the service",

    # --- Social page ---------------------------------------------------------
    "social_hero_title": "Social",
    "social_hero_lead": (
        "Follow us on Instagram for a glimpse of life in the studio and tips for"
        " your rehabilitation."
    ),

    # --- Page <title> and meta description (keyed by page file) --------------
    "pages": {
        "index.html": (
            "Home",
            "FisioHub Lugano: the meeting point between science, listening and"
            " movement. Quality physiotherapy and fitness in the heart of Lugano.",
        ),
        "hub.html": (
            "Hub",
            "The FisioHub studio in Lugano: our approach and the tools we use.",
        ),
        "servizi.html": (
            "Services",
            "Physiotherapy, sports physiotherapy, home visits, prevention and"
            " strength &amp; conditioning, massage and lymphatic drainage in"
            " Lugano.",
        ),
        "cosa-trattiamo.html": (
            "What we treat",
            "Neck and back, shoulder, knee, ankle, hip, TMJ, chronic pain and"
            " sports injuries: what we treat at FisioHub Lugano.",
        ),
        "team.html": (
            "The team",
            "The FisioHub Lugano team: Luca Gilardoni, Simone Vaccani, Carola"
            " Isella and Federico Monzoni.",
        ),
        "insta.html": (
            "Social",
            "Follow FisioHub Lugano on Instagram.",
        ),
        "contatti.html": (
            "Contact",
            "Contact details and address of FisioHub SA, Via Carlo Maderno 26,"
            " 6900 Lugano. WhatsApp, phone and email.",
        ),
    },
}
