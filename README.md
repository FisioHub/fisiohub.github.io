# Fisio Hub Lugano — Static Website

This is a clean, dependency-free static reproduction of [fisiohub.ch](https://fisiohub.ch/), converted from WordPress + Semplice 7 into pure semantic **HTML5 + Vanilla CSS + Vanilla JS**, paired with a lightweight zero-dependency Python generator ([`build.py`](build.py)) so shared headers, footers, team profiles, and therapy pages can be maintained in one place.

> **Prototype:** this site currently lives at **https://fisiohub.github.io/**. It will replace
> fisiohub.ch only after company approval. When it moves to the real domain, change
> `site_url` in `SITE_CONFIG` (`build.py`) to `https://fisiohub.ch/` and run `python3 build.py`.

---

## Project Structure

```text
fisiohub-web/
├── index.html            # Homepage: hero + Hub, Servizi, Come possiamo aiutarti,
│                         #   Cosa c'è in studio, Esperti in fisioterapia, Dove siamo
├── hub.html              # Lo studio (+ foto), il nostro approccio, strumenti spiegati
├── servizi.html          # I 5 servizi spiegati + strumenti spiegati
├── cosa-trattiamo.html   # 8 casi + banner "Ti hanno operato?" / "Dentro la sala operatoria"
├── team.html             # Biografie, sigle spiegate, banner "Formazione, insegnamento e sport"
├── insta.html            # Instagram feed
├── contatti.html         # Mappa, WhatsApp/email cliccabili, banner fisioterapia a domicilio
├── terapie.html, dove.html, <team>.html, project/*.html
│                         # Redirect pages from the old URLs (keep links/SEO working)
├── en/                   # English version of the 7 pages above (same file names)
├── css/styles.css
├── js/main.js            # Mobile menu, language switch, solid header on scroll
├── assets/
├── content/
│   ├── it/               # Italian text (original)
│   └── en/               # English translation, same structure
│       ├── ui.py         #   menu, buttons, headings, banners, page titles
│       ├── hub.py        #   HUB text + approach
│       ├── services.py   #   services
│       ├── conditions.py #   conditions we treat
│       ├── tools.py      #   equipment
│       └── team.py       #   bios, credentials glossary, team banner
├── check_parity.py       # Checks an English file matches its Italian one
└── build.py              # Generator: layout, settings and page templates
```

---

## Italian / English

The site is bilingual. Italian pages live at the root, English pages in `en/`
with the same file names. The **IT / EN** switch in the header links each page
to its counterpart in the other language (keeping the current `#section`).
Each page also declares its other-language version with `hreflang` links.

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

1. Edit [`build.py`] for settings shared by both languages:
   - **`SITE_CONFIG`**: phone, WhatsApp number, email, address, menu order, and
     **`booking_url`** (currently `contatti.html`; swap in the online booking link when ready).
   - **`STUDIO_PHOTOS`**: paths of the studio photos (placeholders are shown while empty).
   - **`REDIRECTS`**: old URL → new URL map.

   Edit the text in `content/it/` **and** the same entry in `content/en/`:
   - **`ui.py`**: menu labels, WhatsApp message, buttons, headings, banners, page titles.
   - **`hub.py`, `services.py`, `conditions.py`, `tools.py`**: page content.
   - **`team.py`**: bios, credentials, areas, glossary.

   After changing a translation, `python3 check_parity.py team` (or `ui`, `hub`, …)
   confirms the English file still has the same entries, ids and HTML as the Italian one.
2. Run:
   ```bash
   python3 build.py
   ```
   All pages (both languages) and redirects will regenerate in under 0.1 seconds.

---

## Improvements Over the Original WordPress Site

- **Zero WordPress / Plugin Bloat**: Removed ~1,200 lines per page of inline Semplice CSS, jQuery, MediaElement.js, XML-RPC, and WordPress emoji scripts.
- **Security & SEO Cleanup**: Removed a hidden third-party spam link (`sprunkiretake.net`) that had been injected into the `/dove` page via an external map embed snippet.
- **Fixed Copy-Paste Bugs**: Fixed the booking email subject lines on `/project/fisioterapia-a-domicilio` and `/project/taping-e-bendaggio-sportivo`, and normalized the `/project/terapia-strumentale` URL slug to lowercase.
