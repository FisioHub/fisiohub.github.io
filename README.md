# Fisio Hub Lugano — Static Website

This is a clean, dependency-free static reproduction of [fisiohub.ch](https://fisiohub.ch/), converted from WordPress + Semplice 7 into pure semantic **HTML5 + Vanilla CSS + Vanilla JS**, paired with a lightweight zero-dependency Python generator ([`build.py`](build.py)) so shared headers, footers, team profiles, and therapy pages can be maintained in one place.

---

## Project Structure

```text
random_stuff/
├── index.html                  # Homepage (video background + hero)
├── hub.html                    # L'HUB page
├── terapie.html                # Therapies index page
├── team.html                   # Team 2x2 grid page
├── luca-gilardoni.html         # Team bio: Luca Gilardoni
├── simone-vaccani.html         # Team bio: Simone Vaccani
├── carola-isella.html          # Team bio: Carola Isella
├── federico-monzoni-2.html     # Team bio: Federico Monzoni
├── insta.html                  # Instagram feed page
├── dove.html                   # Location, contact & Google Map page
├── project/                    # 14 individual therapy detail pages
│   ├── fisioterapia-ortopedica-e-sportiva.html
│   ├── fisioterapia-post-operatoria.html
│   └── ...
├── css/
│   └── styles.css              # Single unified stylesheet (~450 lines)
├── js/
│   └── main.js                 # Mobile menu toggle (~30 lines)
├── assets/
│   ├── fonts/                  # Self-hosted WOFF2 fonts (Regular, Medium, Bold, Inter, Satoshi)
│   ├── logos/                  # All 5 color-themed SVG logos
│   ├── images/                 # Background images, team photos, favicons, WhatsApp icon
│   └── video/                  # Homepage cover background MP4
└── build.py                    # Single-file static generator for shared layout & data
```

---

## How to Preview Locally

Run any static HTTP server from this directory:

```bash
python3 -m http.server 8080
```

Then open `http://martinsevilla.c.googlers.com:8080` in your browser.

---

## How to Maintain / Update Content

Instead of editing 24 separate HTML files when changing a phone number, email address, menu link, team member, or therapy description:

1. Edit [`build.py`](build.py):
   - **`SITE_CONFIG`**: Phone number, WhatsApp number, email, physical address, navigation items.
   - **`TEAM_MEMBERS`**: Team photos and biography paragraphs.
   - **`THERAPIES`**: Therapy titles, descriptions, treated pathologies, and email booking subjects.
2. Run:
   ```bash
   python3 build.py
   ```
   All 24 HTML files will regenerate in under 0.1 seconds.

---

## Improvements Over the Original WordPress Site

- **Zero WordPress / Plugin Bloat**: Removed ~1,200 lines per page of inline Semplice CSS, jQuery, MediaElement.js, XML-RPC, and WordPress emoji scripts.
- **Security & SEO Cleanup**: Removed a hidden third-party spam link (`sprunkiretake.net`) that had been injected into the `/dove` page via an external map embed snippet.
- **Fixed Copy-Paste Bugs**: Fixed the booking email subject lines on `/project/fisioterapia-a-domicilio` and `/project/taping-e-bendaggio-sportivo`, and normalized the `/project/terapia-strumentale` URL slug to lowercase.
