#!/usr/bin/env python3
"""Phase 2 generator: catches + local guides + page hero tints."""
import pathlib

ROOT = pathlib.Path(__file__).parent.parent
HEADER = '''<a class="skip" href="#main">Skip to content</a>
<div class="scroll-progress"></div>
<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><span>Outdoor Adventures BC</span></a><button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul><li><a class="navlink" href="/kelowna-fishing-charters.html">Charters</a></li><li><a class="navlink" href="/sightseeing-tours.html">Sightseeing</a></li><li><a class="navlink" href="/pricing.html">Pricing</a></li><li><a class="navlink" href="/blog/">Blog</a></li><li><a class="navlink" href="/reviews.html">Reviews</a></li><li><a class="btn btn-primary" href="/contact.html">Book</a></li></ul></div></header>'''

FOOTER = '''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><p>Kelowna-based fishing charters and sightseeing tours on Okanagan, Shuswap and Arrow Lakes.</p><p style="margin-top:8px"><a href="tel:+12509028323" style="color:#fff;font-weight:600">250-902-8323</a></p></div><div><h4>Charters</h4><ul><li><a href="/kelowna-fishing-charters.html">Fishing Charters</a></li><li><a href="/charters/half-day-charter.html">Half-day</a></li><li><a href="/charters/full-day-charter.html">Full-day</a></li><li><a href="/charters/sunset-cruise.html">Sunset cruise</a></li><li><a href="/gift-certificates.html">Gift certificates</a></li></ul></div><div><h4>Lakes & guides</h4><ul><li><a href="/lakes/okanagan-lake.html">Okanagan Lake</a></li><li><a href="/lakes/shuswap-lake.html">Shuswap Lake</a></li><li><a href="/lakes/arrow-lake.html">Arrow Lakes</a></li><li><a href="/guides/kelowna-boat-ramps.html">Kelowna boat ramps</a></li><li><a href="/guides/where-to-fish-okanagan-lake.html">Where to fish Okanagan</a></li><li><a href="/guides/fishing-near-downtown-kelowna.html">Fishing near downtown</a></li></ul></div><div><h4>Company</h4><ul><li><a href="/captain.html">The captain</a></li><li><a href="/reviews.html">Reviews</a></li><li><a href="/catches/">Recent catches</a></li><li><a href="/refer.html">Refer a friend</a></li><li><a href="/waiver.html">Digital waiver</a></li><li><a href="/contact.html">Contact</a></li></ul></div></div><div class="footer-bottom"><span>© <span data-year></span> Outdoor Adventures BC · Kelowna, BC · Built by <a href="https://elliotdigital.ca" rel="noopener" style="color:#fff">Elliot Digital</a></span><span><a href="/legal/privacy.html">Privacy</a> · <a href="/legal/terms.html">Terms</a> · <a href="/legal/cancellation-policy.html">Cancellations</a></span></div></div></footer>'''

TAIL = '''<a href="tel:+12509028323" class="fab-call" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.8 19.8 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72 12.8 12.8 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.8 12.8 0 002.81.7A2 2 0 0122 16.92z"/></svg></a>
<div class="sticky-book"><div class="sticky-book-inner"><span><strong>$200/hr</strong> · Kelowna charter</span><a href="/contact.html" class="btn btn-primary">Book</a></div></div>
<script src="/assets/js/main.js" defer></script>'''

HEAD_COMMON = '''<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#0E3B4F"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap"/><link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png"/><link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16.png"/><link rel="apple-touch-icon" sizes="180x180" href="/assets/img/favicon-180.png"/><link rel="manifest" href="/site.webmanifest"/><link rel="stylesheet" href="/assets/css/styles.css"/>'''

def page(title, desc, url, body, schema=""):
    return f'''<!doctype html><html lang="en-CA"><head>
{HEAD_COMMON}
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow,max-image-preview:large"/>
<link rel="canonical" href="https://outdooradventuresbc.ca{url}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:image" content="https://outdooradventuresbc.ca/assets/img/captain-trophy-rainbow.jpg"/>
<meta property="og:url" content="https://outdooradventuresbc.ca{url}"/>
{schema}
</head><body>
{HEADER}
<main id="main">
{body}
</main>
{FOOTER}
{TAIL}
</body></html>'''

# ------- CATCHES HUB -------
catches_hub_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Recent catches</nav>
<div class="section-head reveal"><span class="eyebrow">Catch log</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Recent catches on Okanagan Lake</h1><p>A running log of what we're landing on recent Kelowna charters. Dated, photographed, honest.</p></div>

<div class="grid grid-3">
  <a class="card reveal" href="/catches/2026-04-rainbow.html"><img src="/assets/img/captain-trophy-rainbow.jpg" alt="April 2026 trophy rainbow trout" loading="lazy"/><div class="card-body"><span class="card-meta">April 2026 · Okanagan</span><h3>Trophy rainbow · pre-spawn</h3><p>Water temp 8°C, trolled a chrome needlefish 35 ft down off a deep structural edge.</p><span class="link">Read catch report →</span></div></a>
  <a class="card reveal delay-1" href="/catches/2026-04-bridge-rainbow.html"><img src="/assets/img/rod-bent-kelowna-bridge.jpg" alt="Rainbow trout near W.R. Bennett Bridge" loading="lazy"/><div class="card-body"><span class="card-meta">April 2026 · Kelowna</span><h3>Rainbow · under the bridge</h3><p>Downtown Kelowna trip. Rod loaded up within sight of the W.R. Bennett Bridge.</p><span class="link">Read catch report →</span></div></a>
  <a class="card reveal delay-2" href="/catches/2026-04-in-net.html"><img src="/assets/img/trophy-rainbow-in-net.jpg" alt="Rainbow trout in the landing net" loading="lazy"/><div class="card-body"><span class="card-meta">April 2026 · Okanagan</span><h3>Net-eye view</h3><p>Solid spring rainbow boat-side. Released clean.</p><span class="link">Read catch report →</span></div></a>
</div>

<p class="text-center" style="margin-top:36px;color:var(--muted)">Book a charter and your catch might be next on the board. <a href="/contact.html">Request a date →</a></p>
</div></section>'''

# Individual catch articles
def catch_article(date, title, summary, image, body_html, slug):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"{date}","image":"https://outdooradventuresbc.ca{image}","author":{{"@type":"Person","name":"Dennis Barnes","sameAs":["https://www.linkedin.com/in/dennis-barnes-8b9061115/","https://www.facebook.com/dennis.barnes.5817/"]}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    body = f'''<article class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/catches/">Catches</a> › {title}</nav>
<h1>{title}</h1>
<p style="color:var(--muted);font-size:.9rem">Published {date} · Dennis Barnes</p>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{summary}</p>
<img src="{image}" alt="{title}" style="border-radius:var(--radius);margin:20px 0" loading="lazy"/>
{body_html}
<hr/>
<p><strong>Want a day like this?</strong> <a href="/contact.html">Book a Kelowna fishing charter</a> with Dennis — we'll rig it all for you.</p>
</div></div></article>'''
    return page(f"{title} · Catch report · Outdoor Adventures BC", summary, f"/catches/{slug}.html", body, schema)

# ------- LOCAL GUIDES -------

guides = [
    {
        "url": "/guides/kelowna-boat-ramps.html",
        "title": "Kelowna Boat Ramps — Complete Launch Guide for Okanagan Lake",
        "desc": "A complete guide to Kelowna boat ramps on Okanagan Lake — locations, parking, fees, wake zones and which to use for fishing charters.",
        "h1": "Kelowna boat ramps — the complete launch guide",
        "lede": "Every public boat launch in the Kelowna area, ranked by fishing-charter usefulness from the captain who launches a boat here 200+ days a year.",
        "content": '''<h2>Cook Road / Hot Sands Beach launch</h2>
<p>North-end Kelowna, right off Highway 97. Two concrete ramps, deep enough for our Kingfisher 2525 in all water levels. <strong>Parking:</strong> ~40 trailer spots. Fill fast on July weekends. <strong>Fee:</strong> free at time of writing. <strong>Wake zone:</strong> 200m no-wake off the launch.</p>

<h2>Bear Creek Provincial Park launch</h2>
<p>West Kelowna side, 15 minutes from downtown Kelowna by boat. Great for Okanagan Lake west-shore trips. <strong>Parking:</strong> day-use parking fills, arrive early in summer. <strong>Fee:</strong> provincial park day-use.</p>

<h2>Gyro Beach / Kinsmen Park launch</h2>
<p>South Kelowna, closest launch to the Mission and downtown. Single concrete ramp. Good for sunset cruises and south-lake trips. <strong>Parking:</strong> limited, street parking overflow. <strong>Wake zone:</strong> tight restrictions — watch the buoys.</p>

<h2>Pritchard Road launch (Westside)</h2>
<p>West Kelowna, slightly quieter alternative to Bear Creek. Shallow at low water — we use this mid-summer.</p>

<h2>Summerland / Penticton</h2>
<p>Not Kelowna, but worth mentioning — if you're staying in the south Okanagan and want to meet us south rather than drive up, we can launch from Penticton's Skaha Lake or Sicamous Beach.</p>

<h2>Which ramp we use for your charter</h2>
<p>We pick the launch based on three things: <strong>where you're staying</strong>, <strong>where the fish are biting</strong>, and <strong>weather / wind direction</strong>. Most Kelowna charters meet at Cook Road by default; if the wind is north we shift to Bear Creek for lee water; for corporate downtown pickups we use Gyro.</p>

<h2>What to know before you arrive</h2>
<ul>
<li>Parking is for your vehicle for the day — we'll direct you</li>
<li>Arrive 15 minutes before your departure time</li>
<li>Public washrooms are at Cook and Bear Creek; Gyro has portables only</li>
<li>No glass containers on the boat</li>
</ul>'''
    },
    {
        "url": "/guides/where-to-fish-okanagan-lake.html",
        "title": "Where to Fish Okanagan Lake — Best Spots from a Kelowna Charter Captain",
        "desc": "A Kelowna fishing charter captain's guide to the best spots on Okanagan Lake — kokanee basins, lake-trout structure, rainbow shoreline.",
        "h1": "Where to fish on Okanagan Lake",
        "lede": "The productive structure on Okanagan Lake isn't random. Here's where kokanee, rainbow and lake trout actually live — broken down by species and season.",
        "content": '''<h2>Mid-lake kokanee basins</h2>
<p>From Knox Mountain south to Bear Creek is the classic summer kokanee zone. Water depth 150–250 ft. Fish suspend 40–80 ft down over the basin. This is where we spend 80% of June–August charter time.</p>

<h2>South arm lake-trout structure</h2>
<p>Between Peachland and Summerland, the south basin holds fish deeper year-round. Good for lake-trout jigging in spring/fall at 120–180 ft over submerged points.</p>

<h2>Rainbow-trout shoreline</h2>
<p>Rainbow feed shallower than kokanee — the 20–40 ft shelf along the east shore (Mission to Gellatly) is productive trolling water, especially mornings and evenings.</p>

<h2>Bay spots for first-light bites</h2>
<p>Mill Creek, Mission Creek and Bear Creek all flow into Okanagan Lake and concentrate baitfish in their outflow plumes. Great for dawn rainbow trolling.</p>

<h2>Seasonal summary</h2>
<ul>
<li><strong>Spring (Apr–May):</strong> Rainbow shallow, lake trout still up in the water column. East shore + creek mouths.</li>
<li><strong>Summer (Jun–Aug):</strong> Kokanee prime time. Mid-lake basins, downrigger trolling.</li>
<li><strong>Fall (Sep–Oct):</strong> Lake trout coming up. South arm structure.</li>
<li><strong>Winter (Nov–Mar):</strong> Lake trout deep, but up the water column. Whole lake is open.</li>
</ul>'''
    },
    {
        "url": "/guides/fishing-near-downtown-kelowna.html",
        "title": "Fishing Near Downtown Kelowna — Walk-to-Dock Charter Guide",
        "desc": "Staying in downtown Kelowna? Here's how to book a fishing charter you can walk to — Gyro Beach, Kinsmen Park and waterfront pickups.",
        "h1": "Fishing from downtown Kelowna",
        "lede": "Staying on the waterfront? You don't need a car to get on the water. Here's the no-drive option for a Kelowna fishing charter.",
        "content": '''<h2>Walk-to-dock options</h2>
<p>If you're staying in downtown Kelowna, the Mission, or anywhere along the waterfront, we can meet you at a launch within walking distance. No rental car needed.</p>

<h2>Gyro Beach pickup</h2>
<p>Under 10 minutes on foot from most downtown hotels. We'll idle up, you step on, we're fishing within 15 minutes of departure.</p>

<h2>Kelowna Yacht Club visitor dock</h2>
<p>For guests at the Delta Grand or the Eldorado, we can arrange a pickup right at the visitor dock. Most civilized start to a fishing day imaginable.</p>

<h2>The Kelowna bridge view</h2>
<p>Charters leaving from downtown immediately put you in sight of the iconic W.R. Bennett Bridge. Great photos, good fishing water — the bridge is over a productive ledge.</p>

<h2>What you'll see</h2>
<ul>
<li>The downtown Kelowna waterfront from the water</li>
<li>Knox Mountain cliffs</li>
<li>Bear Creek provincial park shoreline</li>
<li>Vineyards along the east shore</li>
<li>Possibly the Ogopogo if you're patient</li>
</ul>

<h2>Book a downtown pickup</h2>
<p>Call or text Dennis at <a href="tel:+12509028323">250-902-8323</a> and mention you'd like a downtown Kelowna meet. We'll confirm the exact dock a day ahead based on wind and water level.</p>'''
    },
]

# ------- WRITE -------
def write(path, html):
    p = ROOT / path.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print(f"+ {path}")

# Catches
write("/catches/index.html", page(
    "Recent Catches — Outdoor Adventures BC Kelowna",
    "Recent catch reports from Outdoor Adventures BC — Kelowna fishing charters on Okanagan Lake. Dated, photographed, honest.",
    "/catches/", catches_hub_body))

write("/catches/2026-04-rainbow.html", catch_article(
    "2026-04-20", "Trophy rainbow · Okanagan, April 2026",
    "April rainbow on a slow morning troll. Chrome needlefish, 35 ft down on the rigger, off a deep structural edge west of Knox Mountain.",
    "/assets/img/captain-trophy-rainbow.jpg",
    """<h2>Conditions</h2><p>Water 8°C, light south wind, flat overcast. Classic April rainbow weather.</p>
<h2>Setup</h2><p>12-lb mono leader, 4-ft drop behind a small silver dodger, chrome needlefish tipped with a tiny piece of worm. Rigger ball at 35 ft, boat speed 1.4 mph.</p>
<h2>The fight</h2><p>Rod loaded up gradually, no big slam — typical spring rainbow. Solid 3 minutes of clean runs before we got it to the net. Fat, healthy fish.</p>""", "2026-04-rainbow"))

write("/catches/2026-04-bridge-rainbow.html", catch_article(
    "2026-04-18", "Rainbow under the Kelowna bridge",
    "Downtown Kelowna charter. Hooked up within sight of the W.R. Bennett Bridge — rod bent just as we slid past.",
    "/assets/img/rod-bent-kelowna-bridge.jpg",
    """<h2>The spot</h2><p>Immediately north of the W.R. Bennett Bridge, on the deep side of the ledge. 60 ft of water, fish holding at 25 ft.</p>
<h2>Why the bridge?</h2><p>Structure concentrates baitfish. The bridge pilings + dredged channel create an edge that rainbow patrol morning and evening.</p>
<h2>Guests' reaction</h2><p>"We can literally see our hotel from here." Booking a downtown Kelowna charter hits different.</p>""", "2026-04-bridge-rainbow"))

write("/catches/2026-04-in-net.html", catch_article(
    "2026-04-15", "Net-eye view · April rainbow",
    "Clean release on a healthy spring rainbow. The net shot is always the best shot.",
    "/assets/img/trophy-rainbow-in-net.jpg",
    """<h2>Release protocol</h2><p>Barbless hook, fish stayed in the water the whole time, quick photo while still in the net, release. Healthy swim-off.</p>
<h2>Why it matters</h2><p>Responsible catch-and-release keeps Okanagan Lake fishing this way for the next 20 years. Every charter we run is conservation-minded.</p>""", "2026-04-in-net"))

# Guides
for g in guides:
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{g["title"]}","datePublished":"2026-04-22","author":{{"@type":"Person","name":"Dennis Barnes"}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    body = f'''<section class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › {g["h1"]}</nav>
<span class="eyebrow">Kelowna local guide</span>
<h1>{g["h1"]}</h1>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{g["lede"]}</p>
{g["content"]}
<hr/>
<p><strong>Skip the research — just book with someone who already knows.</strong> <a href="/contact.html">Book a Kelowna fishing charter →</a></p>
</div></div></section>'''
    write(g["url"], page(g["title"], g["desc"], g["url"], body, schema))

# Guides hub
guides_hub_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Local guides</nav>
<div class="section-head reveal"><span class="eyebrow">Local guides</span><h1>Kelowna local guides</h1><p>Practical, local-first guides to fishing, launching and exploring Okanagan Lake from someone who does it daily.</p></div>
<div class="grid grid-3">
  <a class="card reveal" href="/guides/kelowna-boat-ramps.html"><div class="card-body"><span class="card-meta">Launch guide</span><h3>Kelowna boat ramps</h3><p>Every public launch in the Kelowna area, ranked by charter-captain usefulness.</p><span class="link">Read guide →</span></div></a>
  <a class="card reveal delay-1" href="/guides/where-to-fish-okanagan-lake.html"><div class="card-body"><span class="card-meta">Species guide</span><h3>Where to fish Okanagan Lake</h3><p>Kokanee basins, lake-trout structure, rainbow shoreline — by season.</p><span class="link">Read guide →</span></div></a>
  <a class="card reveal delay-2" href="/guides/fishing-near-downtown-kelowna.html"><div class="card-body"><span class="card-meta">Downtown</span><h3>Fishing near downtown Kelowna</h3><p>Walk-to-dock charter options for guests staying on the waterfront.</p><span class="link">Read guide →</span></div></a>
</div>
</div></section>'''
write("/guides/index.html", page("Kelowna Local Fishing Guides — Outdoor Adventures BC", "Practical Kelowna local guides to fishing, launching and exploring Okanagan Lake.", "/guides/", guides_hub_body))

print("phase 2 gen done")
