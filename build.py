#!/usr/bin/env python3
"""Static Site Generator for Fisio Hub Lugano.

Prototype hosted at https://fisiohub.github.io/; it will replace
https://fisiohub.ch/ once approved.

Generates every page of the site, in Italian and English, from a single
shared layout and the content files in content/<lang>/:

  index.html            Homepage (hero + one-page overview of every section)
  hub.html              Lo studio, il nostro approccio, gli strumenti
  servizi.html          I servizi spiegati + gli strumenti spiegati
  cosa-trattiamo.html   I casi che trattiamo + banner post-operatorio
  team.html             Biografie, sigle spiegate, formazione e sport
  insta.html            Feed Instagram
  contatti.html         Mappa, contatti, fisioterapia a domicilio

Italian pages are written to the site root, English pages to en/ with the
same file names. The IT / EN switch in the header links each page to its
counterpart in the other language.

  content/it/*.py       Italian text (the original)
  content/en/*.py       English translation, same structure
    ui.py               Header, buttons, headings, banners, page titles
    hub.py              HUB text and approach
    services.py         Services
    conditions.py       Conditions we treat
    tools.py            Equipment
    team.py             Bios, credentials glossary, team banner

Old URLs from the previous version of the site (terapie.html, dove.html, the
individual team pages and project/*.html) are regenerated as small redirect
pages so existing links and search results keep working.

Usage:
  python3 build.py
"""

import os
from types import SimpleNamespace

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# 1. Shared Site Configuration (Edit here to update across all pages)
#    Text shown to visitors (menu labels, WhatsApp message, buttons...) lives
#    in content/<lang>/ui.py.
# ==============================================================================
SITE_CONFIG = {
    # Public address of the site, used for the hreflang links between the
    # Italian and English version of each page. The prototype lives on GitHub
    # Pages; switch to "https://fisiohub.ch/" when the site moves to the real
    # domain, then run build.py again.
    "site_url": "https://fisiohub.github.io/",
    "company": "FisioHub SA",
    "address_line_1": "Via Carlo Maderno, 26",
    "address_line_2": "6900 Lugano",
    "phone_display": "079 839 69 00",
    # International format, digits only (no "+", no leading 0 of the Swiss
    # number): used for tel: and WhatsApp links.
    "phone_intl": "41798396900",
    "email": "fisiohub@hin.ch",
    # Where every "Prenota appuntamento" button points. For now it is the
    # contact page; replace with the online booking URL once it is live.
    "booking_url": "contatti.html",
    # {hl} is replaced with the page language (UI["map_hl"]).
    "map_embed_url": (
        "https://maps.google.com/maps?width=650&amp;height=450&amp;hl={hl}"
        "&amp;q=lugano%20Via%20Carlo%20Maderno%2C%2026&amp;t=&amp;z=15"
        "&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"
    ),
    "map_link_url": (
        "https://www.google.com/maps/search/?api=1&amp;query=FisioHub%20Via"
        "%20Carlo%20Maderno%2026%20Lugano"
    ),
    # Menu order; the labels are in content/<lang>/ui.py (UI["nav"]).
    "nav_items": [
        "hub.html",
        "servizi.html",
        "cosa-trattiamo.html",
        "team.html",
        "insta.html",
        "contatti.html",
    ],
}

# Languages: code -> (output folder, label on the switch, full name).
# The first one is the default language, served from the site root.
LANGUAGES = {
    "it": ("", "IT", "Italiano"),
    "en": ("en/", "EN", "English"),
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
# 2. Content loading
#    Each language has the same set of modules in content/<lang>/. While a page
#    is being rendered, L holds the current language's content and ROOT the
#    relative path back to the site root ("" for Italian, "../" for English).
# ==============================================================================
CONTENT_MODULES = ("ui", "hub", "services", "conditions", "tools", "team")

L = SimpleNamespace()
ROOT = ""
LANG = "it"


def load_content(lang: str) -> SimpleNamespace:
  data = {}
  for mod in CONTENT_MODULES:
    path = os.path.join(BASE_DIR, "content", lang, mod + ".py")
    ns = {}
    with open(path, encoding="utf-8") as f:
      exec(compile(f.read(), path, "exec"), ns)
    data.update({k: v for k, v in ns.items() if k.isupper()})
  return SimpleNamespace(**data)


def use_language(lang: str) -> None:
  global L, ROOT, LANG
  LANG = lang
  L = load_content(lang)
  folder = LANGUAGES[lang][0]
  ROOT = "../" * folder.count("/")


def asset(path: str) -> str:
  """Path to a file in assets/, css/ or js/ from the current language folder."""
  return ROOT + path


# ==============================================================================
# 3. Small HTML helpers
# ==============================================================================
def whatsapp_url() -> str:
  text = L.UI["whatsapp_text"].replace(" ", "%20")
  return f"https://wa.me/{SITE_CONFIG['phone_intl']}?text={text}"


def tel_url() -> str:
  return f"tel:+{SITE_CONFIG['phone_intl']}"


def mailto_url(subject: str = "") -> str:
  subject = (subject or L.UI["mail_subject"]).replace(" ", "%20")
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
        f'<figure class="photo {cls}"><img src="{asset(src)}" alt="{alt}"'
        ' loading="lazy"></figure>'
    )
  return (
      f'<figure class="photo photo-placeholder {cls}" role="img"'
      f' aria-label="{alt}"><span>{label}</span></figure>'
  )


def btn(href: str, label: str, style: str = "rose", extra: str = "") -> str:
  return f'<a class="btn btn-{style}" href="{href}"{extra}>→ {label}</a>'


def book_btn(style: str = "rose") -> str:
  return btn(SITE_CONFIG["booking_url"], L.UI["book"], style)


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
  for i, t in enumerate(L.TOOLS, 1):
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
          {section_title(L.UI["tools_title"])}
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
              <li><a href="{tel_url()}"><span class="contact-ico" aria-hidden="true">☎</span><span>{L.UI['phone_label']} <strong>{c['phone_display']}</strong></span></a></li>
              <li><a href="mailto:{c['email']}"><span class="contact-ico" aria-hidden="true">@</span><span>Email <strong>{c['email']}</strong></span></a></li>
            </ul>
          </div>"""


def map_embed() -> str:
  src = SITE_CONFIG["map_embed_url"].replace("{hl}", L.UI["map_hl"])
  return f"""<div class="map-wrap">
            <iframe title="{L.UI['map_title']} - {SITE_CONFIG['address_line_1']}" loading="lazy" src="{src}"></iframe>
          </div>"""


def lang_href(target: str, page: str) -> str:
  """Relative link from the current page to its version in `target`."""
  return ROOT + LANGUAGES[target][0] + page


def lang_switch(page: str) -> str:
  links = []
  for code, (_, short, full) in LANGUAGES.items():
    cur = ' aria-current="true"' if code == LANG else ""
    links.append(
        f'<a href="{lang_href(code, page)}" hreflang="{code}" lang="{code}"'
        f' aria-label="{full}"{cur}>{short}</a>'
    )
  return (
      f'<div class="lang-switch" role="group" aria-label="{L.UI["lang_switch_aria"]}">'
      + "".join(links) + "</div>"
  )


def hreflang_links(page: str) -> str:
  base = SITE_CONFIG["site_url"]
  slug = "" if page == "index.html" else page
  out = [
      f'  <link rel="alternate" hreflang="{code}" href="{base}{folder}{slug}">'
      for code, (folder, _, _) in LANGUAGES.items()
  ]
  default_folder = next(iter(LANGUAGES.values()))[0]
  out.append(
      f'  <link rel="alternate" hreflang="x-default" href="{base}{default_folder}{slug}">'
  )
  return "\n".join(out)


# ==============================================================================
# 4. Shared HTML Layout Template
# ==============================================================================
def render_page(
    *,
    page: str,
    title: str,
    description: str,
    theme_class: str,
    logo_file: str,
    body_html: str,
) -> str:
  """Wraps page content with the shared header, mobile menu and footer."""
  c = SITE_CONFIG
  ui = L.UI
  nav_lis = []
  overlay_lis = []
  for href in c["nav_items"]:
    label = ui["nav"][href]
    is_active = href == page
    cur = ' aria-current="page"' if is_active else ""
    act = ' class="active"' if is_active else ""
    nav_lis.append(f'          <li><a href="{href}"{act}{cur}>{label}</a></li>')
    overlay_lis.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
  nav_html = "\n".join(nav_lis)
  overlay_html = "\n".join(overlay_lis)
  wa_aria = ui["whatsapp_aria_phone"].replace("{phone}", c["phone_display"])

  return f"""<!DOCTYPE html>
<html lang="{ui['html_lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Fisio Hub Lugano</title>
  <meta name="description" content="{description}">
  <meta property="og:locale" content="{ui['og_locale']}">
  <meta property="og:site_name" content="{ui['site_name']}">
  <meta property="og:title" content="{title} - Fisio Hub Lugano">
  <meta property="og:description" content="{description}">
{hreflang_links(page)}
  <link rel="icon" href="{asset('assets/images/favicon-32x32.png')}" sizes="32x32">
  <link rel="icon" href="{asset('assets/images/favicon-192x192.png')}" sizes="192x192">
  <link rel="apple-touch-icon" href="{asset('assets/images/favicon-180x180.png')}">
  <link rel="stylesheet" href="{asset('css/styles.css')}">
</head>
<body class="{theme_class}">

  <!-- Shared Header & Navigation -->
  <header class="site-header">
    <div class="nav-container">
      <a class="nav-logo" href="index.html" aria-label="{ui['home_aria']}">
        <img class="logo-top" src="{asset('assets/logos/' + logo_file)}" alt="Fisio Hub">
        <img class="logo-scrolled" src="{asset('assets/logos/FisioHub_blu.svg')}" alt="" aria-hidden="true">
      </a>
      <nav class="nav-menu" aria-label="{ui['nav_aria']}">
        <ul class="nav-list">
{nav_html}
        </ul>
      </nav>
      <div class="nav-actions">
        {lang_switch(page)}
        <a class="nav-phone" href="{whatsapp_url()}" target="_blank" rel="noopener" aria-label="{wa_aria}">
          {WHATSAPP_ICON}<span class="nav-phone-num">{c['phone_display']}</span>
        </a>
        <button id="mobile-menu-open" class="hamburger-btn" aria-label="{ui['menu_open']}" aria-controls="mobile-overlay" aria-expanded="false">
          <span></span>
        </button>
      </div>
    </div>

    <!-- Mobile Overlay Menu -->
    <div id="mobile-overlay" class="mobile-overlay" aria-hidden="true">
      <button id="mobile-menu-close" class="overlay-close-btn" aria-label="{ui['menu_close']}">
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
  <a class="wa-float" href="{whatsapp_url()}" target="_blank" rel="noopener" aria-label="{ui['whatsapp_aria']}">
    <img src="{asset('assets/images/whatsapp.png')}" alt="">
  </a>

  <script src="{asset('js/main.js')}"></script>
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
# 5. Page Builders
# ==============================================================================
def build_home() -> str:
  c = SITE_CONFIG
  ui = L.UI

  service_rows = "\n".join(
      f"""          <a class="row-link" href="servizi.html#{s['id']}">
            <span class="row-num">{i:02d}</span>
            <span class="row-title">{s['title']}</span>
            <span class="row-text">{s['short']}</span>
            <span class="row-arrow" aria-hidden="true">→</span>
          </a>"""
      for i, s in enumerate(L.SERVICES, 1)
  )

  condition_tiles = "\n".join(
      f"""          <a class="tile" href="cosa-trattiamo.html#{x['id']}">
            <h3>{x['title']}</h3>
            <p>{x['short']}</p>
            <span class="tile-arrow" aria-hidden="true">→</span>
          </a>"""
      for x in L.CONDITIONS
  )

  team_cards = "\n".join(
      f"""          <a class="team-card" href="team.html#{m['slug']}">
            <img src="{asset(m['photo'])}" width="1000" height="1043" alt="{m['name']}">
            <h3><span class="accent-arrow">→</span> {m['name']}</h3>
            {chips(m['credentials'])}
            <p class="team-areas">{" · ".join(m['areas'])}</p>
          </a>"""
      for m in L.TEAM_MEMBERS
  )

  return f"""    <section class="hero-cover">
      <div class="hero-video-wrapper">
        <video class="hero-video" autoplay muted loop playsinline webkit-playsinline preload="auto"
               poster="{asset('assets/images/hero-poster.jpg')}"
               disablepictureinpicture disableremoteplayback aria-hidden="true" tabindex="-1">
          <source src="{asset('assets/video/Comp-1_12_mute-720.mp4')}" type="video/mp4" media="(max-width: 900px)">
          <source src="{asset('assets/video/Comp-1_12_mute.mp4')}" type="video/mp4">
        </video>
      </div>
      <div class="container hero-grid">
        <div class="hero-logo-col fade-in-up">
          <img src="{asset('assets/logos/FisioHub_blu.svg')}" alt="{ui['home_logo_alt']}">
        </div>
        <div class="hero-content-col">
          <h1 class="hero-title fade-in-up">
            <span class="text-rose">{ui['home_hero_kicker']}</span><br>
            <span class="text-navy">{ui['home_hero_title']}</span>
          </h1>
          <p class="hero-lead fade-in-up">
            {ui['home_hero_lead']}
          </p>
          <div class="hero-buttons fade-in-left">
            <a id="btn-book-home" class="btn-action btn-rose" href="{c['booking_url']}">→ {ui['home_btn_book']}</a>
            <a id="btn-approach-home" class="btn-action btn-rose btn-secondary" href="hub.html#approccio">→ {ui['home_btn_approach']}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="band band-navy" id="hub">
      <div class="container split">
        <div class="split-text">
          {section_title(ui['home_hub_title'])}
{paragraphs(L.HUB_PARAGRAPHS)}
            <p>{L.APPROACH_INTRO}</p>
          {btn("hub.html", ui['home_hub_cta'], "outline-light")}
        </div>
        <div class="split-media">
          {photo(STUDIO_PHOTOS['main'], ui['photo_studio_alt'], ui['photo_studio_label'])}
        </div>
      </div>
    </section>

    <section class="band band-teal" id="servizi">
      <div class="container">
        <div class="section-head">
          {section_title(ui['home_services_title'])}
          <p class="section-intro">{ui['home_services_intro']}</p>
        </div>
        <div class="row-list">
{service_rows}
        </div>
      </div>
    </section>

    <section class="band band-navy" id="cosa-trattiamo">
      <div class="container">
        <div class="section-head">
          {section_title(ui['home_conditions_title'])}
          <p class="section-intro">{ui['home_conditions_intro']}</p>
        </div>
        <div class="tile-grid">
{condition_tiles}
        </div>
      </div>
    </section>

{tools_band(False, ui['tools_intro_short'], btn("servizi.html#strumenti", ui['tools_cta'], "outline-light"), "teal")}

    <section class="band band-rose" id="team">
      <div class="container">
        <div class="section-head">
          {section_title(ui['home_team_title'])}
          <p class="section-intro">{ui['home_team_intro']}</p>
        </div>
        <div class="team-grid">
{team_cards}
        </div>
      </div>
    </section>

    <section class="band band-lake" id="dove">
      <div class="container split">
        <div class="split-text">
          {section_title(ui['dove_title'])}
          {contact_block()}
          {book_btn()}
        </div>
        <div class="split-media">
          {map_embed()}
        </div>
      </div>
    </section>"""


def build_hub() -> str:
  ui = L.UI
  pillars = "\n".join(
      f"""          <div class="pillar">
            <span class="card-num">{i:02d}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>"""
      for i, (t, d) in enumerate(L.APPROACH_PILLARS, 1)
  )
  gallery = "\n".join(
      "          " + photo(STUDIO_PHOTOS[k], ui['photo_studio_alt_short'], ui['photo_studio_label'])
      for k in ("gallery_1", "gallery_2", "gallery_3")
  )
  return f"""{page_hero(ui['hub_hero_title'], ui['hub_hero_lead'])}

    <section class="band band-white" id="studio">
      <div class="container split">
        <div class="split-text">
          {section_title(ui['hub_studio_title'])}
{paragraphs(L.HUB_PARAGRAPHS)}
        </div>
        <div class="split-media">
          {photo(STUDIO_PHOTOS['main'], ui['photo_studio_alt'], ui['photo_studio_label'])}
        </div>
      </div>
      <div class="container gallery">
{gallery}
      </div>
    </section>

    <section class="band band-navy" id="approccio">
      <div class="container">
        <div class="section-head">
          {section_title(ui['hub_approach_title'])}
          <p class="section-intro">{L.APPROACH_INTRO}</p>
        </div>
        <div class="pillar-grid">
{pillars}
        </div>
      </div>
    </section>

{tools_band(True, ui['tools_intro_detailed'], color="rose")}"""


def build_servizi() -> str:
  ui = L.UI
  blocks = []
  for i, s in enumerate(L.SERVICES, 1):
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
            {btn(SITE_CONFIG["booking_url"], ui['book_short'], "teal")}
          </div>
        </article>""")
  return f"""{page_hero(ui['services_hero_title'], "")}

    <section class="band band-white">
      <div class="container detail-list">
{chr(10).join(blocks)}
      </div>
    </section>

{tools_band(True, ui['tools_intro_detailed'], color="teal")}"""


def build_cosa_trattiamo() -> str:
  ui = L.UI
  blocks = []
  for i, x in enumerate(L.CONDITIONS, 1):
    blocks.append(f"""        <article class="detail" id="{x['id']}">
          <div class="detail-head">
            <span class="card-num">{i:02d}</span>
            <h2>{x['title']}</h2>
          </div>
          <div class="detail-body">
{paragraphs(x['paragraphs'])}
          </div>
          <div class="detail-side">
            <h3>{ui['conditions_examples_title']}</h3>
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
          <p class="banner-kicker">{ui['postop_kicker']}</p>
          <h2>{ui['postop_title']}</h2>
          <p>{ui['postop_text']}</p>
        </div>
        <div class="banner-actions">{book_btn("navy")}</div>
      </div>
    </section>

    <section class="banner banner-navy" id="sala-operatoria">
      <div class="container banner-inner banner-inner--media">
        <div>
          <p class="banner-kicker">{ui['or_kicker']}</p>
          <h2>{ui['or_title']}</h2>
          <p>{ui['or_text']}</p>
          {btn("team.html", ui['or_cta'], "outline-light")}
        </div>
        {photo(STUDIO_PHOTOS['sala_operatoria'], ui['or_photo_alt'], ui['or_photo_label'], "banner-photo")}
      </div>
    </section>

    <section class="band band-white">
      <div class="container detail-list">"""
  body = body.replace("        <!--BANNER_OPERATO-->", banner_operato)

  return f"""{page_hero(ui['conditions_hero_title'], ui['conditions_hero_lead'])}

    <section class="band band-white">
      <div class="container detail-list">
{body}
      </div>
    </section>

    <section class="banner banner-teal">
      <div class="container banner-inner">
        <h2>{ui['not_found_title']}</h2>
        <div class="banner-actions">{btn(whatsapp_url(), "WhatsApp", "outline-light", ' target="_blank" rel="noopener"')} {book_btn("navy")}</div>
      </div>
    </section>"""


def build_team() -> str:
  ui = L.UI
  bios = []
  for m in L.TEAM_MEMBERS:
    first, rest = m["paragraphs"][:2], m["paragraphs"][2:]
    bios.append(f"""        <article class="bio" id="{m['slug']}">
          <div class="bio-photo">
            <img src="{asset(m['photo'])}" width="1000" height="1043" alt="{m['name']}" loading="lazy">
          </div>
          <div class="bio-text">
            <h2><span class="accent-arrow">→</span> {m['name']}</h2>
            {chips(m['credentials'])}
            <p class="bio-areas"><strong>{ui['team_areas_label']}</strong> {" · ".join(m['areas'])}</p>
{paragraphs(first)}
            <details class="bio-more">
              <summary>{ui['team_read_more']}</summary>
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
      for abbr, full, desc in L.CREDENTIALS_GLOSSARY
  )
  banner_cols = "\n".join(
      f"""          <div>
            <h3><span class="accent-arrow">→</span> {t}</h3>
            <p>{d}</p>
          </div>"""
      for t, d in L.TEAM_BANNER_COLUMNS
  )

  return f"""{page_hero(ui['team_hero_title'], ui['team_hero_lead'])}

    <section class="band band-white">
      <div class="container bio-list">
{chr(10).join(bios)}
      </div>
    </section>

    <section class="band band-navy" id="sigle">
      <div class="container">
        <div class="section-head">
          {section_title(ui['glossary_title'])}
          <p class="section-intro">{ui['glossary_intro']}</p>
        </div>
        <div class="gloss-grid">
{glossary}
        </div>
      </div>
    </section>

    <section class="banner banner-rose" id="formazione">
      <div class="container">
        <h2 class="banner-title">{ui['team_banner_title']}</h2>
        <div class="banner-cols">
{banner_cols}
        </div>
      </div>
    </section>"""


def build_contatti() -> str:
  ui = L.UI
  return f"""{page_hero(ui['contact_hero_title'], ui['contact_hero_lead'])}

    <section class="band band-white">
      <div class="container split">
        <div class="split-text">
          {section_title(ui['dove_title'])}
          {contact_block()}
          <div class="btn-row">
            {btn(whatsapp_url(), ui['contact_btn_whatsapp'], "rose", ' target="_blank" rel="noopener"')}
            {btn(mailto_url(), ui['contact_btn_email'], "navy")}
          </div>
          <p class="small"><a href="{SITE_CONFIG['map_link_url']}" target="_blank" rel="noopener">→ {ui['contact_open_maps']}</a></p>
        </div>
        <div class="split-media">
          {map_embed()}
        </div>
      </div>
    </section>

    <section class="banner banner-rose" id="domicilio">
      <div class="container banner-inner">
        <div>
          <p class="banner-kicker">{ui['home_visit_kicker']}</p>
          <h2>{ui['home_visit_title']}</h2>
          <p>{ui['home_visit_text']}</p>
        </div>
        <div class="banner-actions">{btn("servizi.html#domicilio", ui['home_visit_cta'], "navy")}</div>
      </div>
    </section>"""


def build_insta() -> str:
  ui = L.UI
  return f"""{page_hero(ui['social_hero_title'], ui['social_hero_lead'])}

    <section class="band band-white">
      <div class="container">
        <script src="https://elfsightcdn.com/platform.js" async></script>
        <div class="elfsight-app-fbefbcda-4027-463d-99c1-13c3c4f3b81c" data-elfsight-app-lazy></div>
      </div>
    </section>"""


# page file -> (body class, header logo, builder)
PAGES = {
    "index.html": ("theme-home", "FisioHub_blu.svg", build_home),
    "hub.html": ("theme-hub", "FisioHub.svg", build_hub),
    "servizi.html": ("theme-servizi", "FisioHub_giallo.svg", build_servizi),
    "cosa-trattiamo.html": ("theme-trattiamo", "FisioHub_verde.svg",
                            build_cosa_trattiamo),
    "team.html": ("theme-team", "FisioHub_BLuw.svg", build_team),
    "insta.html": ("theme-insta", "FisioHub.svg", build_insta),
    "contatti.html": ("theme-contatti", "FisioHub.svg", build_contatti),
}


def build_all() -> None:
  for lang, (folder, _, _) in LANGUAGES.items():
    use_language(lang)
    for page, (theme, logo, builder) in PAGES.items():
      title, desc = L.UI["pages"][page]
      write_page(folder + page, render_page(
          page=page, title=title, description=desc, theme_class=theme,
          logo_file=logo, body_html=builder(),
      ))

  for old, new in REDIRECTS.items():
    write_page(old, render_redirect(old, new))


if __name__ == "__main__":
  build_all()
