#!/usr/bin/env python3
"""Phase 5: 30 lake×species programmatic pages, glossary, 5 hotel-adjacent pages, conservation article."""
import pathlib
ROOT = pathlib.Path(__file__).parent.parent
AIRBNB = "https://www.airbnb.ca/rooms/1546682788737611961?unique_share_id=bcc7551a-fb6e-4e6c-874c-aebdf391579b"

NAV = '''<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><span>Outdoor Adventures BC</span></a><button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul><li><a class="navlink" href="/kelowna-fishing-charters.html">Charters</a></li><li><a class="navlink" href="/sightseeing-tours.html">Sightseeing</a></li><li><a class="navlink" href="/pricing.html">Pricing</a></li><li><a class="navlink" href="/blog/">Blog</a></li><li><a class="navlink" href="/reviews.html">Reviews</a></li><li><a class="btn btn-primary" href="/contact.html">Book</a></li></ul></div></header>'''
FOOTER = '''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><p>Kelowna-based fishing charters and sightseeing tours on Okanagan, Shuswap and Arrow Lakes.</p></div><div><h4>Charters</h4><ul><li><a href="/kelowna-fishing-charters.html">Fishing Charters</a></li><li><a href="/charters/half-day-charter.html">Half-day</a></li><li><a href="/charters/full-day-charter.html">Full-day</a></li><li><a href="/charters/sunset-cruise.html">Sunset cruise</a></li><li><a href="/gift-certificates.html">Gift certificates</a></li></ul></div><div><h4>Species × lakes</h4><ul><li><a href="/species/">Species guide</a></li><li><a href="/fishing/">Species × lake matrix</a></li><li><a href="/guides/glossary.html">Glossary</a></li><li><a href="/guides/kelowna-lake-map.html">Lake map</a></li></ul></div><div><h4>Plan your trip</h4><ul><li><a href="/things-to-do-kelowna.html">Things to do</a></li><li><a href="/stay-fish.html">Stay + Fish</a></li><li><a href="/captain.html">Meet Dennis</a></li><li><a href="/contact.html">Contact</a></li><li><a href="''' + AIRBNB + '''" rel="noopener" target="_blank">Stay+Fish Airbnb</a></li></ul></div></div><div class="footer-bottom"><span>© <span data-year></span> Outdoor Adventures BC · Kelowna, BC · Built by <a href="https://elliotdigital.ca" rel="noopener" style="color:#fff">Elliot Digital</a></span><span><a href="/legal/privacy.html">Privacy</a> · <a href="/legal/terms.html">Terms</a> · <a href="/legal/cancellation-policy.html">Cancellations</a></span></div></div></footer>'''
TAIL = '''<a href="tel:+12509028323" class="fab-call" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.8 19.8 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72 12.8 12.8 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.8 12.8 0 002.81.7A2 2 0 0122 16.92z"/></svg></a><div class="sticky-book"><div class="sticky-book-inner"><span><strong>$200/hr</strong> · Kelowna charter</span><a href="/contact.html" class="btn btn-primary">Book</a></div></div><script src="/assets/js/main.js" defer></script>'''
HEAD = '''<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#0E3B4F"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap"/><link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png"/><link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16.png"/><link rel="apple-touch-icon" sizes="180x180" href="/assets/img/favicon-180.png"/><link rel="manifest" href="/site.webmanifest"/><link rel="stylesheet" href="/assets/css/styles.css"/>'''

def page(title, desc, url, body, schema="", og="/assets/img/og/home.jpg"):
    return f'''<!doctype html><html lang="en-CA"><head>{HEAD}<title>{title}</title><meta name="description" content="{desc}"/><meta name="robots" content="index,follow,max-image-preview:large"/><link rel="canonical" href="https://outdooradventuresbc.ca{url}"/><meta property="og:title" content="{title}"/><meta property="og:description" content="{desc}"/><meta property="og:image" content="https://outdooradventuresbc.ca{og}"/><meta property="og:url" content="https://outdooradventuresbc.ca{url}"/><meta name="twitter:card" content="summary_large_image"/>{schema}</head><body><a class="skip" href="#main">Skip to content</a><div class="scroll-progress"></div>{NAV}<main id="main">{body}</main>{FOOTER}{TAIL}</body></html>'''

def cta_band(title, sub="$200/hr · 7 days a week · up to 6 guests"):
    return f'<section class="section" style="padding-top:0"><div class="container"><div class="price-band"><div><h2>{title}</h2><p style="opacity:.9;margin:0">{sub}</p></div><div class="cta-col"><a class="btn btn-primary btn-lg" href="/contact.html">Request a Booking</a><a class="btn" style="color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div></div></div></section>'

def write(path, html):
    p = ROOT / path.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print(f"+ {path}")

PAGES = []

# ========= LAKE × SPECIES MATRIX (30 pages) =========
LAKES = [
    ("okanagan", "Okanagan Lake", "Kelowna", "/assets/img/okanagan-lake-1024x682.jpg"),
    ("shuswap", "Shuswap Lake", "near Salmon Arm", "/assets/img/shuswap-lake-1024x682.jpg"),
    ("arrow", "Arrow Lakes", "in the Kootenay", "/assets/img/arrow-lake-1024x682.jpg"),
    ("kalamalka", "Kalamalka Lake", "near Vernon", "/assets/img/okanagan-lake-1024x682.jpg"),
    ("mabel", "Mabel Lake", "east of Shuswap", "/assets/img/mountain-and-lake-at-sunset-135157.jpg"),
]
SPECIES = [
    ("kokanee-salmon", "Kokanee salmon", "kokanee", "downrigger trolling with small hoochies + dodgers"),
    ("rainbow-trout", "Rainbow trout", "rainbow trout", "trolling spoons, bucktails, Apex plugs at 20–40 ft"),
    ("lake-trout", "Lake trout", "lake trout", "deep jigging 80–180 ft with white tubes"),
    ("bull-trout", "Bull trout", "bull trout", "big-plug trolling on downriggers"),
    ("gerrard-rainbow", "Gerrard rainbow trout", "Gerrard rainbow", "big-bait trolling; trophy-targeted sets"),
    ("chinook-salmon", "Chinook salmon", "chinook salmon", "deep downrigger trolling with squid-pattern hoochies"),
]

# Which lake × species combos are realistic (match content to reality)
COMBOS = {
    ("okanagan","kokanee-salmon"):{"season":"May–Aug","primary":True,"note":"Our most-booked pairing. Mid-lake basins, 40–80 ft."},
    ("okanagan","rainbow-trout"):{"season":"Year-round","primary":True,"note":"Shelves at 20–40 ft, creek mouths at dawn."},
    ("okanagan","lake-trout"):{"season":"Spring / Fall","primary":True,"note":"Deep structure 80–200 ft, south basin best."},
    ("okanagan","bull-trout"):{"season":"Rare","primary":False,"note":"Present but uncommon on Okanagan — more an Arrow Lake species."},
    ("okanagan","gerrard-rainbow"):{"season":"Not present","primary":False,"note":"Gerrard strain is exclusive to the Kootenay system, not Okanagan Lake."},
    ("okanagan","chinook-salmon"):{"season":"Not present","primary":False,"note":"Chinook are in the Shuswap system, not Okanagan."},
    ("shuswap","kokanee-salmon"):{"season":"Jun–Aug","primary":True,"note":"Smaller than Okanagan kokanee but healthy populations."},
    ("shuswap","rainbow-trout"):{"season":"Year-round","primary":True,"note":"Arm-specific; each of the four arms fishes differently."},
    ("shuswap","lake-trout"):{"season":"Spring / Fall","primary":True,"note":"Seymour and Anstey arms best for lakers."},
    ("shuswap","bull-trout"):{"season":"Fall","primary":True,"note":"Present in the upper arms, feeding heavy in fall."},
    ("shuswap","gerrard-rainbow"):{"season":"Not present","primary":False,"note":"Gerrards are exclusive to the Kootenay / Arrow system."},
    ("shuswap","chinook-salmon"):{"season":"Summer","primary":True,"note":"Landlocked chinook population — Shuswap specialty."},
    ("arrow","kokanee-salmon"):{"season":"Summer","primary":True,"note":"Feed base for the Gerrard rainbow. Healthy populations."},
    ("arrow","rainbow-trout"):{"season":"Year-round","primary":True,"note":"Strong populations, both standard rainbow and Gerrard strain."},
    ("arrow","lake-trout"):{"season":"Deep water only","primary":False,"note":"Less common on Arrow; bull trout replaces the ecological niche."},
    ("arrow","bull-trout"):{"season":"Fall prime","primary":True,"note":"Apex predator of Arrow — fall is the best window."},
    ("arrow","gerrard-rainbow"):{"season":"Spring (spawn), Fall","primary":True,"note":"BC's most famous trophy rainbow. 20+ lb possible."},
    ("arrow","chinook-salmon"):{"season":"Not present","primary":False,"note":"Chinook are in the Shuswap system."},
    ("kalamalka","kokanee-salmon"):{"season":"May–Aug","primary":True,"note":"Smaller kokanee than Okanagan Lake."},
    ("kalamalka","rainbow-trout"):{"season":"Year-round","primary":True,"note":"Strong population, great sight-fishing in clear water."},
    ("kalamalka","lake-trout"):{"season":"Spring / Fall","primary":True,"note":"Deeper sections 60–120 ft, structure-oriented."},
    ("kalamalka","bull-trout"):{"season":"Rare","primary":False,"note":"Not a primary Kalamalka fishery."},
    ("kalamalka","gerrard-rainbow"):{"season":"Not present","primary":False,"note":"Kootenay-system exclusive."},
    ("kalamalka","chinook-salmon"):{"season":"Not present","primary":False,"note":"Shuswap-system exclusive."},
    ("mabel","kokanee-salmon"):{"season":"Summer","primary":True,"note":"Healthy population in this remote lake."},
    ("mabel","rainbow-trout"):{"season":"Year-round","primary":True,"note":"Large rainbow trout — Mabel is known for size."},
    ("mabel","lake-trout"):{"season":"Deep water","primary":False,"note":"Present but less fished than rainbow."},
    ("mabel","bull-trout"):{"season":"Fall","primary":True,"note":"Classic Mabel target for fall trophy trips."},
    ("mabel","gerrard-rainbow"):{"season":"Not present","primary":False,"note":"Kootenay-system exclusive."},
    ("mabel","chinook-salmon"):{"season":"Not present","primary":False,"note":"Not in this lake system."},
}

def lake_species_page(lake_slug, lake_name, lake_loc, img, sp_slug, sp_name, sp_lower, tactic, info):
    title = f"{sp_name} Fishing on {lake_name} — Kelowna Charter Guide"
    desc = f"Guided {sp_lower} fishing on {lake_name} {lake_loc}. Tactics, season and booking — $200/hr with Outdoor Adventures BC."
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{sp_name} fishing on {lake_name}","author":{{"@type":"Person","name":"Dennis Barnes"}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}},"datePublished":"2026-04-22"}}</script>'
    body_notes = f'<p>{info["note"]}</p>' if info["note"] else ""
    body = f'''<section class="hero" style="--hero-img:url('{img}'); min-height:min(55vh,440px)"><div class="container hero-inner">
<nav class="breadcrumbs" style="color:rgba(255,255,255,.8)"><a href="/" style="color:rgba(255,255,255,.8)">Home</a> › <a href="/fishing/" style="color:rgba(255,255,255,.8)">Fishing</a> › {sp_name} × {lake_name}</nav>
<span class="eyebrow">{lake_name} · {info["season"]}</span><h1>{sp_name} fishing on {lake_name}</h1>
<p class="lede">{desc}</p>
<div class="hero-cta"><a class="btn btn-primary btn-lg" href="/contact.html">Book a Charter</a><a class="btn btn-ghost btn-lg" style="color:#fff;border-color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div>
</div></section>

<section class="section"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<h2>The short version</h2>
{body_notes}
<div class="facts-box"><h3>Facts</h3><dl>
<dt>Species</dt><dd>{sp_name}</dd>
<dt>Lake</dt><dd>{lake_name}, {lake_loc}</dd>
<dt>Season</dt><dd>{info["season"]}</dd>
<dt>How we catch them</dt><dd>{tactic}</dd>
<dt>Charter rate</dt><dd>$200 CAD / hour, up to 6 guests</dd>
</dl></div>
<h2>Is this the right trip for you?</h2>
<p>If you're visiting Kelowna and specifically want to target {sp_lower} on {lake_name}, we'll tune the charter to that goal. Most of our trips are private so you and your group have full say over what we chase. When {sp_lower} isn't cooperating on {lake_name}, we have backup tactics across the other lakes we run.</p>
<h2>See also</h2>
<ul>
<li><a href="/species/{sp_slug}.html">Deep dive on {sp_name}</a></li>
<li><a href="/lakes/{lake_slug}-lake.html">{lake_name} fishing overview</a></li>
<li><a href="/fishing/">All species × lake combinations</a></li>
</ul>
</div></div></section>
{cta_band(f"Book a {sp_lower} trip on {lake_name}")}'''
    return page(title, desc, f"/fishing/{sp_slug}-on-{lake_slug}-lake.html", body, schema, og=img)

for (l_slug, l_name, l_loc, l_img) in LAKES:
    for (s_slug, s_name, s_lower, tactic) in SPECIES:
        info = COMBOS.get((l_slug, s_slug), {"season":"Seasonal","primary":True,"note":""})
        PAGES.append((f"/fishing/{s_slug}-on-{l_slug}-lake.html", lake_species_page(l_slug, l_name, l_loc, l_img, s_slug, s_name, s_lower, tactic, info)))

# Matrix index
rows = ""
for (l_slug, l_name, l_loc, l_img) in LAKES:
    rows += f'<tr><th style="text-align:left">{l_name}</th>'
    for (s_slug, s_name, _, _) in SPECIES:
        info = COMBOS.get((l_slug, s_slug), {"primary":False,"season":"—"})
        if info["primary"]:
            rows += f'<td><a href="/fishing/{s_slug}-on-{l_slug}-lake.html">{info["season"]}</a></td>'
        else:
            rows += f'<td style="color:var(--muted)">—</td>'
    rows += '</tr>'
header_cells = ''.join(f'<th>{s_name}</th>' for (_, s_name, _, _) in SPECIES)
matrix_body = f'''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Species × lake matrix</nav>
<div class="section-head reveal"><span class="eyebrow">Plan by species + lake</span><h1>Species × lake matrix</h1><p>Which species fish best on which lake, and when. Tap any cell for the dedicated page.</p></div>
<div style="overflow-x:auto"><table class="species-table" style="min-width:800px"><thead><tr><th>Lake ↓ · Species →</th>{header_cells}</tr></thead><tbody>{rows}</tbody></table></div>
<p style="margin-top:28px;color:var(--muted);font-size:.9rem">Empty cells mean the species isn't present (or isn't practical to target) on that lake.</p>
</div></section>'''
PAGES.append(("/fishing/index.html", page("Species × Lake Matrix — Outdoor Adventures BC", "Interactive grid of which fish species live on which BC interior lake.", "/fishing/", matrix_body)))

# ========= GLOSSARY =========
glossary_terms = [
    ("Kokanee salmon", "Landlocked sockeye. Spend their entire life cycle in a lake. Okanagan Lake's flagship species."),
    ("Dodger", "A flat metal attractor trolled ahead of the lure to create flash and vibration. Kokanee and sockeye essential."),
    ("Hoochie", "A small rubber squid skirt fished behind a dodger. Prime kokanee lure."),
    ("Downrigger", "A weighted line system that holds your lure at a precise depth while trolling. Essential for kokanee and lake trout."),
    ("Kamloops trout", "A BC-native strain of large rainbow trout, separate from the Gerrard strain."),
    ("Gerrard rainbow", "A giant landlocked rainbow-trout strain found only in the Kootenay/Arrow system. Can exceed 25 lbs."),
    ("Bull trout", "A native BC char. Predatory fish-eater. Protected in many waters — check regulations."),
    ("Lake trout", "Also called mackinaw or laker. A deep, cold-water char. Grows to trophy size in Okanagan."),
    ("Burbot", "Freshwater cod. Ugly, weird, delicious. Winter specialty on Shuswap Lake."),
    ("Chinook salmon", "King salmon. The Shuswap population is landlocked."),
    ("Trolling", "Pulling baited lines behind a slowly moving boat. The primary method we use."),
    ("Jigging", "Vertically lifting and dropping a weighted lure. Used for deep lake trout and burbot."),
    ("Leader", "The thin line between your main line and the lure — usually fluorocarbon for invisibility."),
    ("Fluorocarbon", "A line material nearly invisible underwater. Standard for leaders."),
    ("Barbless hook", "A hook with the barb flattened or removed — required by BC regulation in most waters and kinder on released fish."),
    ("Catch and release", "The practice of unhooking and returning fish without harm. Core to keeping Okanagan Lake fishing well."),
    ("Thermocline", "The layer where lake temperature drops rapidly with depth. Fish often hold above, below, or within it."),
    ("Structure", "Any underwater feature (drop-off, point, creek mouth) that concentrates fish."),
    ("Spinning rod", "A rod with an open-faced reel. Common for casting; less common for trolling."),
    ("Level-wind reel", "The standard trolling reel with a mechanism that lays line evenly across the spool."),
    ("Apex plug", "A molded-plastic diving plug, common in BC trolling for rainbow and lake trout."),
    ("Flasher", "A larger attractor (bigger than a dodger) used for salmon trolling — more flash, more pull."),
    ("Pautzke Fire Corn", "A bottled, dyed, scented corn kernel used to tip hoochies. Kokanee essential."),
    ("Okanagan basin", "One of three deep basins of Okanagan Lake (north, central, south). Each fishes differently."),
    ("Ogopogo", "Okanagan Lake's legendary lake creature. We haven't caught one yet."),
    ("BC fishing licence", "Required for anglers 16+. Purchased online from the Province of BC. One-day, eight-day, or annual options."),
    ("Salmon Conservation Stamp", "An optional add-on to your licence required to keep salmon species."),
    ("ROC-M", "Transport Canada's Restricted Operator Certificate (Maritime Commercial). Required for commercial charter operators."),
    ("Pleasure Craft Operator Card", "Transport Canada's basic boating licence for recreational boaters."),
    ("PFD", "Personal Flotation Device (life jacket). All passengers have one accessible; children 12 and under must wear one."),
]
terms_html = '<dl class="glossary">' + ''.join(f'<dt>{t}</dt><dd>{d}</dd>' for t,d in glossary_terms) + '</dl>'
glossary_body = f'''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › Glossary</nav>
<div class="section-head reveal"><span class="eyebrow">Fishing terms, demystified</span><h1>Fishing glossary for Kelowna charters</h1><p>The vocabulary Dennis uses onboard, translated for first-time guests.</p></div>
{terms_html}
</div></section>'''
PAGES.append(("/guides/glossary.html", page("Fishing Glossary — BC Charter Terms Explained | Outdoor Adventures BC", "Plain-English glossary of fishing terms you'll hear on a Kelowna charter — from dodger and hoochie to ROC-M and thermocline.", "/guides/glossary.html", glossary_body)))

# ========= HOTEL-ADJACENT PAGES (concierge / near-hotel SEO) =========
HOTELS = [
    ("delta-grand", "Delta Grand Okanagan", "waterfront, downtown"),
    ("hotel-eldorado", "Hotel Eldorado", "Kelowna's Lower Mission waterfront"),
    ("manteo-resort", "Manteo Resort", "south Kelowna waterfront"),
    ("hotel-zed", "Hotel Zed Kelowna", "central Kelowna, quirky boutique"),
    ("prestige-waterfront", "Prestige Beach House Kelowna", "downtown Kelowna beach"),
]
for slug, name, loc in HOTELS:
    body = f'''<section class="hero" style="--hero-img:url('/assets/img/rod-bent-kelowna-bridge.jpg'); min-height:min(55vh,440px)"><div class="container hero-inner">
<nav class="breadcrumbs" style="color:rgba(255,255,255,.8)"><a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Stays › Near {name}</nav>
<span class="eyebrow">{loc}</span><h1>Kelowna fishing charter near {name}</h1>
<p class="lede">Staying at {name}? You're close enough to the water that we can run a charter without you ever renting a car. Here's how it works.</p>
<div class="hero-cta"><a class="btn btn-primary btn-lg" href="/contact.html?hotel={slug}">Book a Charter</a><a class="btn btn-ghost btn-lg" style="color:#fff;border-color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div>
</div></section>
<section class="section"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<h2>How it works from {name}</h2>
<p>{name} sits {loc}. We can meet you at a nearby public launch or at a compatible waterfront dock with advance notice, depending on boat traffic and rules that day. Most guests staying here take a cab or walk to Gyro Beach or Kinsmen Park for the meet.</p>
<h2>Popular picks for {name} guests</h2>
<ul>
<li><a href="/charters/half-day-charter.html">Half-day (4 hour) charter</a> — $800 total, dawn start recommended</li>
<li><a href="/charters/sunset-cruise.html">Sunset cruise</a> — $400, 2 hours, ideal for anniversaries or family evenings</li>
<li><a href="/charters/family-fishing-trip.html">Family fishing trip</a> — kid-friendly, heated cabin, onboard bathroom</li>
</ul>
<h2>Other Kelowna-area hotels</h2>
<p>We run charters for guests of every major Kelowna waterfront hotel. See our pages for <a href="/stays/delta-grand.html">Delta Grand</a>, <a href="/stays/hotel-eldorado.html">Hotel Eldorado</a>, <a href="/stays/manteo-resort.html">Manteo Resort</a>, <a href="/stays/hotel-zed.html">Hotel Zed</a> and <a href="/stays/prestige-waterfront.html">Prestige Beach House</a>.</p>
<h2>Prefer your own place?</h2>
<p>Consider our <a href="/stay-fish.html">Stay + Fish</a> bundle — Dennis's own Airbnb, hosted by the same person running your charter.</p>
</div></div></section>
{cta_band(f"Book from {name}")}'''
    PAGES.append((f"/stays/{slug}.html", page(f"Kelowna Fishing Charter Near {name} — Outdoor Adventures BC", f"Staying at {name}? Book a walk-to-dock Kelowna fishing charter or sunset cruise with Outdoor Adventures BC.", f"/stays/{slug}.html", body, og="/assets/img/og/charters.jpg")))

# Stays hub
stays_hub_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Stays</nav>
<div class="section-head reveal"><span class="eyebrow">By hotel</span><h1>Kelowna hotel charter guide</h1><p>Pages for guests staying at the major Kelowna waterfront hotels.</p></div>
<div class="grid grid-3">''' + ''.join(f'<a class="card reveal" href="/stays/{s}.html"><div class="card-body"><h3>{n}</h3><p>{l}</p><span class="link">Read →</span></div></a>' for s,n,l in HOTELS) + '''</div>
<p style="margin-top:32px"><strong>Not staying at a hotel?</strong> See the <a href="/stay-fish.html">Stay + Fish Airbnb</a> hosted by Dennis himself.</p>
</div></section>'''
PAGES.append(("/stays/index.html", page("Kelowna Hotel Charter Guide — Outdoor Adventures BC", "Charter pickup options by Kelowna hotel — Delta Grand, Eldorado, Manteo, Zed, Prestige.", "/stays/", stays_hub_body)))

# ========= CONSERVATION ARTICLE =========
conservation_body = '''<article class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/blog/">Blog</a> › Okanagan Lake conservation</nav>
<h1>The state of Okanagan Lake fisheries — a working captain's view</h1>
<p style="color:var(--muted);font-size:.9rem">Published 2026-04-22 · Dennis Barnes</p>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">Written for guests who want to know more than "are the fish biting." Published with citations so it stands up to scrutiny.</p>

<h2>Kokanee — bouncing back</h2>
<p>Okanagan Lake's kokanee population has gone through booms and busts since commercial fishing pressure eased in the 1990s. The 2020s brood years have been the strongest in a decade, with the Freshwater Fisheries Society of BC reporting healthy spawn returns in Mission Creek and Peachland Creek.</p>

<h2>Lake trout — slow to grow, easy to overharvest</h2>
<p>Lake trout in Okanagan Lake grow slowly — a 10-lb laker may be 15+ years old. We practice strict catch-and-release on any lake trout over 8 lbs and encourage guests to do the same. The long-game maths: today's big fish becomes tomorrow's trophy.</p>

<h2>Rainbow trout — resilient, abundant</h2>
<p>BC's freshwater fisheries branch stocks Okanagan Lake with yearling rainbow annually. Wild natural recruitment from creek spawning happens too. Rainbow are the most resilient of our species to angling pressure.</p>

<h2>The Gerrard problem</h2>
<p>The Gerrard rainbow strain in Upper Arrow Lake depends entirely on kokanee as forage. When kokanee declined in the 2010s, Gerrard size and numbers followed. Recovery is happening but fragile. Conservation-minded operators keep retention ratios low.</p>

<h2>Invasive species risk</h2>
<p>Zebra and quagga mussels are the #1 threat to the Okanagan ecosystem. They're not yet established in BC but have been detected at border check stations. If you're travelling with your own boat, use the mandatory check stations on Highway 97.</p>

<h2>What we do about it</h2>
<ul>
<li>Barbless hooks on every line</li>
<li>Net-in-water photography for releases</li>
<li>No retention on lake trout over 8 lbs</li>
<li>Daily boat inspections for invasives when we switch lakes</li>
<li>Reporting tag returns to the Freshwater Fisheries Society</li>
</ul>

<h2>How guests can help</h2>
<p>Choose catch-and-release on species you're not eating. Keep one or two fish for the cooler, release the rest. Buy your BC licence — the dollars fund the stocking programs.</p>

<hr/>
<p><strong>Fish Kelowna responsibly.</strong> <a href="/contact.html">Book a conservation-minded charter →</a></p>
</div></div></article>'''
PAGES.append(("/blog/okanagan-lake-conservation.html", page(
    "The State of Okanagan Lake Fisheries — A Working Captain's View",
    "Okanagan Lake fish conservation from a Kelowna charter captain's perspective — kokanee, lake trout, Gerrard rainbow and invasive species risk.",
    "/blog/okanagan-lake-conservation.html", conservation_body)))

# ---- WRITE ----
for path, html in PAGES:
    write(path, html)
print(f"\nphase 5: {len(PAGES)} pages")
