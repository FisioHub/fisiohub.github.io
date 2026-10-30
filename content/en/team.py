"""Team: bios, credentials glossary and banner on team.html (English).

"credentials" are the short titles shown as tags; "areas" are each
therapist's areas of reference. Keep slug, name and photo identical across
languages."""

CREDENTIALS_GLOSSARY = [
    (
        "OMPT",
        "Orthopaedic Manipulative Physical Therapist",
        "Internationally recognised title awarded by the IFOMPT, obtained through"
        " a university master’s degree in rehabilitation of musculoskeletal"
        " disorders. It indicates advanced training in manual therapy, therapeutic"
        " exercise and clinical reasoning.",
    ),
    (
        "CAS",
        "Certificate of Advanced Studies",
        "Postgraduate university qualification from the Swiss system. Luca has"
        " obtained the CAS in Musculoskeletal Physiotherapy at SUPSI.",
    ),
    (
        "CSCS",
        "Certified Strength and Conditioning Specialist",
        "International certification from the NSCA (National Strength and"
        " Conditioning Association) for designing strength and conditioning"
        " training, from injury prevention to performance.",
    ),
    (
        "Maitland",
        "Maitland Concept of manual therapy",
        "A training pathway in manual therapy that combines mobilisation techniques"
        " with structured clinical reasoning and continuous reassessment of"
        " results.",
    ),
    (
        "Running Injury Specialist",
        "The Running Clinic",
        "International certification dedicated to the prevention and treatment of"
        " running injuries.",
    ),
    (
        "Master",
        "Postgraduate university master’s degree",
        "Advanced university training after a physiotherapy degree: in our team, in"
        " lymphatic drainage and in clinical and sports biomechanics.",
    ),
]

TEAM_MEMBERS = [
    {
        "slug": "luca-gilardoni",
        "name": "Luca Gilardoni",
        "photo": "assets/images/LUCA_GILARDONI.jpg",
        "credentials": ['OMPT', 'CAS SUPSI'],
        "areas": ['Shoulder', 'Cervical spine', 'TMJ'],
        "paragraphs": [
            (
                "Luca, born in Sorengo in 1991 and raised in Valsolda on the shores"
                " of Lake Lugano, has always been passionate about sport. After"
                " around twenty years of football, a few injuries drew him towards"
                " the world of physiotherapy. A lover of the mountains, he skied for"
                " many years and from 2015 devoted himself to mountain running,"
                " racing from 2016 with ASD Atletica Pidaggia 1528 and standing out"
                " in long distances on the Italian and international Skyrunning"
                " circuit."
            ),
            (
                "He graduated in physiotherapy from the University of Insubria and"
                " subsequently obtained the OMPT title through the master’s degree in"
                " rehabilitation of musculoskeletal disorders at the University of"
                " Genoa, an experience that gave him a highly evidence-based approach"
                " to both his work and his training."
            ),
            (
                "He then continued his postgraduate university education by completing"
                " the CAS in Musculoskeletal Physiotherapy at SUPSI University in"
                " Lugano."
            ),
            (
                "He regularly attends continuing education courses in musculoskeletal"
                " and sports medicine, and has collaborated on various research"
                " studies with related publications."
            ),
            (
                "Luca began his career at the Istituto Ortopedico Gaetano Pini in"
                " Milan, working in orthopaedic and neurosurgical rehabilitation. From"
                " 2015 he has worked in Ticino at a practice specialising in"
                " musculoskeletal rehabilitation, where he discovered the chance to"
                " combine his two passions: sport and physiotherapy."
            ),
            (
                "From 2019 to 2022 he looked after the rehabilitation of the players of"
                " FC Gambarogno Contone, a club in the Swiss 2nd Liga Interregional."
                " He then broadened his experience in the sports sector, deepening his"
                " specialisation in the treatment of the shoulder, knee and cervical"
                " region."
            ),
            (
                "In his free time he spends time with his daughter Viola, enjoys"
                " reading, cheering on Como 1907 football club, spending time in nature"
                " to take in the landscapes, and travelling!"
            ),
        ],
    },
    {
        "slug": "simone-vaccani",
        "name": "Simone Vaccani",
        "photo": "assets/images/SIMONE_VACCANI.jpg",
        "credentials": ['Maitland', 'Running Injury Specialist', 'Certificate in Sports Physiotherapy'],
        "areas": ['Hip', 'Knee', 'Foot and ankle'],
        "paragraphs": [
            (
                "Simone, born in Busto Arsizio (VA) in 1981, has been passionate about"
                " sport since he was young."
            ),
            (
                "After amateur football, at the age of 18 he discovered swimming, which"
                " for over ten years became his main commitment, leading him to gain"
                " instructor qualifications and to compete on the master swimming"
                " circuit, both in the pool and in open water."
            ),
            (
                "He still practises several sports at amateur level, including open"
                " water swimming, running, mountain biking and snowboarding, and in his"
                " free time he loves hiking in the mountains with his dogs and his"
                " family."
            ),
            (
                "Simone graduated in physiotherapy from the University of Varese with"
                " top marks, and immediately began his training in manual therapy"
                " according to the Maitland Concept, working alongside one of the most"
                " experienced lecturers in the method."
            ),
            (
                "Over the years he developed a solid expertise in orthopaedic and sports"
                " medicine, earning the international Running Injury Specialist"
                " certification from The Running Clinic, a master’s in sports"
                " physiotherapy and various courses on musculoskeletal problems of the"
                " hip and knee."
            ),
            (
                "In 2019 he moved to Ortisei, in South Tyrol, to work at Dolomiti"
                " Sportclinic, a centre of reference for sports trauma and winter"
                " sports. During the three years he spent there, he worked alongside"
                " surgeons in the operating theatre and followed the recovery of young"
                " athletes and high-level professionals on a daily basis, including"
                " hockey players, freestyle skiers, biathletes and figure skaters."
            ),
            (
                "From 2022 Simone has been living in Switzerland, where he continues to"
                " work in orthopaedic and sports rehabilitation, refining his skills in"
                " particular in the rehabilitation of the hip and knee joints."
            ),
        ],
    },
    {
        "slug": "carola-isella",
        "name": "Carola Isella",
        "photo": "assets/images/CAROLA_ISELLA.jpg",
        "credentials": ['CSCS', 'Maitland', "Master’s in Lymphatic Drainage", 'Pilates Reformer'],
        "areas": ['Sports physiotherapy', 'Strength &amp; Conditioning', 'Lymphatic drainage', 'Chronic pain and scoliosis'],
        "paragraphs": [
            (
                "Carola was born in Biella (BI) in 1996. She has always been an active"
                " person, with a strong passion for sport and nature. A former"
                " classical ballet dancer, she developed a deep interest in human"
                " movement and in recovery from injury, which led her to graduate in"
                " physiotherapy from the University of Insubria in Varese."
            ),
            (
                "After completing her studies, Carola deepened her training in the"
                " musculoskeletal field by following the Maitland pathway. She has also"
                " attended numerous sports physiotherapy courses, earned the CSCS"
                " (Certified Strength and Conditioning Specialist) certification and"
                " obtained a Master’s in lymphatic drainage. Over the course of her"
                " career she has further broadened her expertise, gaining specific"
                " qualifications in the treatment of scoliosis and chronic pain."
            ),
            (
                "Today Carola is on the other side of the lectern: she is a teaching"
                " assistant at LUDES University in Lugano."
            ),
            (
                "Carola began working straight away in musculoskeletal and sports"
                " rehabilitation, going on to become the lead physiotherapist for"
                " high-level rugby and basketball teams."
            ),
            (
                "Carola has gained wide experience across many sports, including rugby,"
                " basketball, volleyball and tennis, covering ATP tournaments and"
                " working in highly specialised clinics based on scientific evidence."
                " Over the course of her career she has also become a certified Pilates"
                " Reformer instructor."
            ),
            (
                "Carola’s approach is grounded in evidence-based practice, with a strong"
                " focus on guiding the patient towards a complete recovery. Great"
                " importance is placed on patient education, helping them understand"
                " their injury and manage it effectively in the long term."
            ),
        ],
    },
    {
        "slug": "federico-monzoni",
        "name": "Federico Monzoni",
        "photo": "assets/images/Federico-Monzoni.jpg",
        "credentials": ["Master’s in Clinical and Sports Biomechanics"],
        "areas": ['Biomechanical analysis and return-to-play training', 'Running specialist', 'Lumbar spine'],
        "paragraphs": [
            (
                "Federico, born in the Marche region in 1999, has always been passionate"
                " about sport and outdoor activities. Holidays spent in the Sibillini"
                " Mountains led him, from childhood, to develop a strong bond with the"
                " mountains and to take up mountain biking."
            ),
            (
                "He began downhill racing at a young age and, during his competitive"
                " career, took part in national and international competitions, winning"
                " two Italian titles in the youth categories and a Swiss title on the"
                " IXS Swiss Cup circuit. In 2016 he represented Italy at the Downhill"
                " World Championships in Val di Sole."
            ),
            (
                "Once his competitive career was over, he pursued a degree in"
                " physiotherapy at the University of Perugia, graduating with top marks"
                " in November 2021. During his studies he won an Erasmus+ scholarship,"
                " which allowed him to complete a clinical placement at the orthopaedic"
                " clinic of the University of Malaga."
            ),
            (
                "He began his clinical practice in Central Italy, looking after patients"
                " with musculoskeletal and neurological conditions, both in the acute and"
                " chronic phases."
            ),
            (
                "He then continued his training through further courses in Italy,"
                " Switzerland and England, focusing in particular on musculoskeletal and"
                " sports medicine."
            ),
            (
                "In 2025 he obtained the Master’s in Clinical and Sports Biomechanics at"
                " the University of Camerino, strengthening his interest in movement"
                " analysis and in the relationship between biomechanics, rehabilitation"
                " and performance."
            ),
            (
                "Early in 2026 he also published, as co-author, his first scientific"
                " article on the study of the lower limb, bringing a research dimension"
                " to his clinical practice."
            ),
            (
                "In his free time he enjoys travelling, outdoor sports and working on"
                " projects linked to the development of sport in the local area."
            ),
        ],
    },
]

TEAM_BANNER_COLUMNS = [
    (
        "Training",
        "Master’s degrees, OMPT, CAS and continuous professional development courses"
        " in musculoskeletal and sports medicine: learning never stops.",
    ),
    (
        "Teaching and research",
        "Carola is a teaching assistant at LUDES University in Lugano. Luca and"
        " Federico have collaborated on research studies with scientific"
        " publications.",
    ),
    (
        "Sport",
        "Football, rugby and basketball teams, ATP tournaments and a sports trauma"
        " clinic in the Dolomites. And as athletes themselves: skyrunning, master"
        " swimming, classical ballet and downhill at the World Championships.",
    ),
]
