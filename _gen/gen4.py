#!/usr/bin/env python3
"""Phase 4: 5 more catches, 2 more blog posts, 3 more guides, 1 map page, ReservationPackage schema."""
import pathlib
ROOT = pathlib.Path(__file__).parent.parent
AIRBNB = "https://www.airbnb.ca/rooms/1546682788737611961?unique_share_id=bcc7551a-fb6e-4e6c-874c-aebdf391579b"

NAV = '''<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><span>Outdoor Adventures BC</span></a><button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul><li><a class="navlink" href="/kelowna-fishing-charters.html">Charters</a></li><li><a class="navlink" href="/sightseeing-tours.html">Sightseeing</a></li><li><a class="navlink" href="/pricing.html">Pricing</a></li><li><a class="navlink" href="/blog/">Blog</a></li><li><a class="navlink" href="/reviews.html">Reviews</a></li><li><a class="btn btn-primary" href="/contact.html">Book</a></li></ul></div></header>'''

FOOTER = '''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><p>Kelowna-based fishing charters and sightseeing tours on Okanagan, Shuswap and Arrow Lakes.</p><p style="margin-top:8px"><a href="tel:+12509028323" style="color:#fff;font-weight:600">250-902-8323</a></p></div><div><h4>Charters</h4><ul><li><a href="/kelowna-fishing-charters.html">Fishing Charters</a></li><li><a href="/charters/half-day-charter.html">Half-day</a></li><li><a href="/charters/full-day-charter.html">Full-day</a></li><li><a href="/charters/sunset-cruise.html">Sunset cruise</a></li><li><a href="/charters/proposal-cruise.html">Proposal cruise</a></li><li><a href="/charters/bachelor-party-charter.html">Bachelor/ette</a></li><li><a href="/gift-certificates.html">Gift certificates</a></li></ul></div><div><h4>Lakes & species</h4><ul><li><a href="/species/">Species guide</a></li><li><a href="/lakes/okanagan-lake.html">Okanagan Lake</a></li><li><a href="/lakes/shuswap-lake.html">Shuswap Lake</a></li><li><a href="/lakes/arrow-lake.html">Arrow Lakes</a></li><li><a href="/guides/kelowna-lake-map.html">Lake coverage map</a></li></ul></div><div><h4>Plan your trip</h4><ul><li><a href="/things-to-do-kelowna.html">Things to do in Kelowna</a></li><li><a href="/stay-fish.html">Stay + Fish</a></li><li><a href="/catches/">Recent catches</a></li><li><a href="/captain.html">Meet Dennis</a></li><li><a href="/contact.html">Contact</a></li><li><a href="''' + AIRBNB + '''" rel="noopener" target="_blank">Stay+Fish Airbnb</a></li></ul></div></div><div class="footer-bottom"><span>© <span data-year></span> Outdoor Adventures BC · Kelowna, BC · Built by <a href="https://elliotdigital.ca" rel="noopener" style="color:#fff">Elliot Digital</a></span><span><a href="/legal/privacy.html">Privacy</a> · <a href="/legal/terms.html">Terms</a> · <a href="/legal/cancellation-policy.html">Cancellations</a></span></div></div></footer>'''

TAIL = '''<a href="tel:+12509028323" class="fab-call" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.8 19.8 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72 12.8 12.8 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.8 12.8 0 002.81.7A2 2 0 0122 16.92z"/></svg></a><div class="sticky-book"><div class="sticky-book-inner"><span><strong>$200/hr</strong> · Kelowna charter</span><a href="/contact.html" class="btn btn-primary">Book</a></div></div><script src="/assets/js/main.js" defer></script>'''

HEAD = '''<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#0E3B4F"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap"/><link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png"/><link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16.png"/><link rel="apple-touch-icon" sizes="180x180" href="/assets/img/favicon-180.png"/><link rel="manifest" href="/site.webmanifest"/><link rel="stylesheet" href="/assets/css/styles.css"/><link rel="search" type="application/opensearchdescription+xml" title="Outdoor Adventures BC" href="/opensearch.xml"/>'''

def page(title, desc, url, body, schema="", og_image="/assets/img/og/home.jpg"):
    return f'''<!doctype html><html lang="en-CA"><head>
{HEAD}
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow,max-image-preview:large"/>
<link rel="canonical" href="https://outdooradventuresbc.ca{url}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:image" content="https://outdooradventuresbc.ca{og_image}"/>
<meta property="og:image:width" content="1200"/><meta property="og:image:height" content="630"/>
<meta property="og:url" content="https://outdooradventuresbc.ca{url}"/>
<meta name="twitter:card" content="summary_large_image"/>
{schema}
</head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="scroll-progress"></div>
{NAV}
<main id="main">
{body}
</main>
{FOOTER}
{TAIL}
</body></html>'''

def cta_band(title, sub="$200/hr · 7 days a week · up to 6 guests"):
    return f'''<section class="section" style="padding-top:0"><div class="container"><div class="price-band"><div><h2>{title}</h2><p style="opacity:.9;margin:0">{sub}</p></div><div class="cta-col"><a class="btn btn-primary btn-lg" href="/contact.html">Request a Booking</a><a class="btn" style="color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div></div></div></section>'''

def write(path, html):
    p = ROOT / path.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print(f"+ {path}")

PAGES = []

# ========= MORE CATCH REPORTS =========
def catch(slug, date, title, summary, img, body):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"{date}","image":"https://outdooradventuresbc.ca{img}","author":{{"@type":"Person","name":"Dennis Barnes","sameAs":["https://www.linkedin.com/in/dennis-barnes-8b9061115/","https://www.facebook.com/dennis.barnes.5817/"]}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    b = f'''<article class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/catches/">Catches</a> › {title}</nav>
<h1>{title}</h1>
<p style="color:var(--muted);font-size:.9rem">Published {date} · Dennis Barnes</p>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{summary}</p>
<img src="{img}" alt="{title}" style="border-radius:var(--radius);margin:20px 0" loading="lazy"/>
{body}
<hr/><p><strong>Ready to put this into practice?</strong> <a href="/contact.html">Book a Kelowna fishing charter</a>.</p>
</div></div></article>'''
    return page(f"{title} · Catch Report · Outdoor Adventures BC", summary, f"/catches/{slug}.html", b, schema, img)

PAGES.append(("/catches/2026-05-first-kokanee.html", catch(
    "2026-05-first-kokanee", "2026-05-05", "First kokanee of the season",
    "Water's warmed to 11°C and the kokanee turned on overnight. Here's how the week went.",
    "/assets/img/stern-trolling-okanagan.jpg",
    """<h2>The setup</h2><p>Pink micro-hoochie, 4-inch chrome dodger, 12-lb fluorocarbon leader, 1.4 mph over 180 ft of water. Fire Corn tipped on a #6 Gamakatsu.</p>
<h2>The depth</h2><p>Fish are at 45 ft down right now — higher than they'll be by July. Set the rigger at 40 ft, screen marks at 35–50 ft confirmed it was right.</p>
<h2>The result</h2><p>Three kokanee in the cooler by 9 am, released another four smaller ones. Typical first-week-of-May pattern.</p>""")))

PAGES.append(("/catches/2026-05-sunset-rainbow.html", catch(
    "2026-05-sunset-rainbow", "2026-05-12", "Evening rainbow on Okanagan",
    "Slower morning, but the last hour before sunset produced. Shallow rainbow on a trolled spoon.",
    "/assets/img/rods-sunset-trolling.jpg",
    """<h2>Conditions</h2><p>Bluebird May afternoon. Water had calmed from a windy morning. Fish came up to the shelf edge.</p>
<h2>What worked</h2><p>Needlefish spoon, 50/50 brass, trolled at 20 ft on the rigger along the 40-ft contour. Speed 1.8 mph — faster than the kokanee program.</p>
<h2>The fish</h2><p>Three-pound rainbow, clean release. Picked up two more before dark. Evening bite on Okanagan in May is underrated.</p>""")))

# ========= NEW BLOG POSTS =========
def blog_post(slug, title, date, summary, og_image, body):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"{date}","image":"https://outdooradventuresbc.ca{og_image}","author":{{"@type":"Person","name":"Dennis Barnes"}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    b = f'''<article class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/blog/">Blog</a> › {title}</nav>
<h1>{title}</h1>
<p style="color:var(--muted);font-size:.9rem">Published {date} · Dennis Barnes</p>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{summary}</p>
<img src="{og_image}" alt="{title}" style="border-radius:var(--radius);margin:20px 0" loading="lazy"/>
{body}
<hr/><p><strong>Book a trip?</strong> <a href="/contact.html">Call or text Dennis.</a></p>
</div></div></article>'''
    return page(f"{title} · Outdoor Adventures BC", summary, f"/blog/{slug}.html", b, schema, og_image)

PAGES.append(("/blog/summer-kokanee-forecast.html", blog_post(
    "summer-kokanee-forecast",
    "Summer Kokanee Forecast — Okanagan Lake 2026",
    "2026-05-20", "What to expect on the kokanee front for the next 90 days.",
    "/assets/img/stern-trolling-okanagan.jpg",
    """<h2>The short version</h2><p>Strong brood class in 2023. Fish should be 12–14 inches, up from 10–12 last year. Bite window moving deeper by July as surface warms.</p>
<h2>Week-by-week</h2>
<h3>Late May</h3><p>Fish 40–50 ft. Pink hoochies dominate. Best bite 7–10 am.</p>
<h3>June</h3><p>Kokanee suspend to 50–70 ft. Experiment with UV colours as light changes.</p>
<h3>July</h3><p>Peak. 60–90 ft. Corn on every hook. First-light window critical.</p>
<h3>August</h3><p>Deepest: 80–110 ft. Water warming makes fish lethargic — slow to 1.1 mph.</p>
<h2>Book now</h2><p>June and July weekends fill in April–May. Don't wait.</p>""")))

PAGES.append(("/blog/fall-lake-trout-tactics.html", blog_post(
    "fall-lake-trout-tactics",
    "Fall Lake Trout Tactics — Okanagan Lake",
    "2026-09-08", "When kokanee wind down, lakers come up. Here's how we fish them.",
    "/assets/img/mountain-and-lake-at-sunset-135157.jpg",
    """<h2>Why fall</h2><p>Surface temps drop below 16°C and lake trout migrate higher in the water column. Instead of chasing them at 150 ft we can get them at 60–90 ft.</p>
<h2>Method 1 — Vertical jigging</h2><p>2-oz white tube jig over submerged points. Lift, drop, pause. Most strikes on the drop.</p>
<h2>Method 2 — Big-plug trolling</h2><p>5-inch Apex plug in rainbow pattern, downrigger at 60–80 ft, slow (1.2 mph) pace along structure edges.</p>
<h2>Where</h2><p>South arm near Squally Point is classic. Knox Mountain wall holds fish too.</p>
<h2>Expect</h2><p>Not numbers, size. Fall lakers are the biggest fish most guests will ever land.</p>""")))

# ========= NEW GUIDES =========
def guide(slug, title, h1, lede, content):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{h1}","author":{{"@type":"Person","name":"Dennis Barnes"}},"publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    b = f'''<section class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › {h1}</nav>
<span class="eyebrow">Kelowna local guide</span><h1>{h1}</h1>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{lede}</p>
{content}
<hr/><p><a href="/contact.html">Book a Kelowna fishing charter →</a></p>
</div></div></section>'''
    return page(title, lede, f"/guides/{slug}.html", b, schema, "/assets/img/og/guides.jpg")

PAGES.append(("/guides/fishing-with-family-okanagan.html", guide(
    "fishing-with-family-okanagan",
    "Fishing with Family on Okanagan Lake — Parent's Guide",
    "Fishing with family on Okanagan Lake",
    "A practical guide for parents planning a Kelowna fishing charter with kids, in-laws, or a multi-generational group.",
    """<h2>Pick the right trip length</h2><p>Half-day (4 hours) is the sweet spot for families with kids under 12. Any longer and energy drops.</p>
<h2>Pick the right boat</h2><p>Our Kingfisher 2525 has a heated cabin, full bathroom, and bench seating — the three features that make or break a family trip on Okanagan Lake.</p>
<h2>Manage expectations</h2><p>Tell the kid it's possible we won't catch anything. Then everyone's happy if we do, and nobody's disappointed if we don't.</p>
<h2>Snacks strategy</h2><p>Pack twice what you think. Fishing burns snacks faster than soccer practice.</p>
<h2>The photo</h2><p>Every first-fish deserves a proper photo. Fish held two-handed under the belly, smile in focus, water in the background. We'll take it for you.</p>""")))

PAGES.append(("/guides/catch-and-release-okanagan.html", guide(
    "catch-and-release-okanagan",
    "Catch and Release on Okanagan Lake — Best Practices",
    "Catch and release — best practices on Okanagan Lake",
    "How we handle fish for release on every charter. Keeping Okanagan Lake fishing this way for another 20 years.",
    """<h2>Barbless hooks</h2><p>Required by BC regulation in most situations. We rig every charter barbless. Fish come off the hook easier, handling damage is minimized.</p>
<h2>Minimise air time</h2><p>A fish out of water more than 10 seconds starts to suffocate. Keep it in the net, in the water, as long as possible.</p>
<h2>Support the fish properly</h2><p>Two hands. One under the belly, one loosely around the tail. Never squeeze the gills.</p>
<h2>Don't touch gills</h2><p>Ever. Most-cited cause of post-release mortality.</p>
<h2>Revive before release</h2><p>Hold the fish facing into the current (or moved gently forward in still water) until it kicks strongly. Then let go.</p>
<h2>When to keep</h2><p>Retention is fine within regulation. Plan ahead: bring a cooler with ice so kept fish chill immediately.</p>""")))

# ========= LAKE COVERAGE MAP PAGE =========
# Simple SVG-ish interactive lake-coverage page
map_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › Lake coverage map</nav>
<div class="section-head reveal"><span class="eyebrow">Where we fish</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Our lake-coverage map</h1><p>Every lake we run charters on, ranked by trip frequency. Interactive — tap a pin for the lake page.</p></div>

<div class="reveal" style="background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);padding:20px;position:relative">
<svg viewBox="0 0 800 520" style="width:100%;height:auto;display:block" role="img" aria-label="Map of British Columbia interior lakes fished by Outdoor Adventures BC">
<rect x="0" y="0" width="800" height="520" fill="#E0EBEF"/>
<!-- Mountains backdrop -->
<path d="M0 380 L120 280 L200 340 L320 260 L440 340 L560 240 L680 320 L800 280 L800 520 L0 520 Z" fill="#8FA8AE" opacity=".35"/>
<!-- Okanagan Lake (long vertical) -->
<path d="M320 120 Q340 250 320 400 Q340 440 320 480" stroke="#0E3B4F" stroke-width="14" fill="none" stroke-linecap="round" opacity=".9"/>
<!-- Shuswap (horizontal-ish northeast) -->
<path d="M500 110 Q560 90 620 130 Q680 100 690 160" stroke="#0E3B4F" stroke-width="10" fill="none" stroke-linecap="round" opacity=".9"/>
<!-- Arrow (diagonal southeast) -->
<path d="M660 280 Q700 360 720 460" stroke="#0E3B4F" stroke-width="12" fill="none" stroke-linecap="round" opacity=".9"/>
<!-- Kalamalka (small horizontal north Okanagan) -->
<path d="M340 150 Q380 140 420 160" stroke="#0E3B4F" stroke-width="6" fill="none" stroke-linecap="round" opacity=".8"/>
<!-- Mabel (small east of Shuswap) -->
<circle cx="700" cy="220" r="14" fill="#0E3B4F" opacity=".85"/>

<!-- Pins -->
<g font-family="Fraunces, Georgia, serif" font-weight="600" fill="#0C1315">
<a href="/lakes/okanagan-lake.html"><circle cx="322" cy="310" r="12" fill="#C2571A"/><text x="340" y="314" font-size="14">Okanagan Lake · Kelowna HQ</text></a>
<a href="/lakes/shuswap-lake.html"><circle cx="600" cy="120" r="10" fill="#C2571A"/><text x="618" y="124" font-size="13">Shuswap Lake</text></a>
<a href="/lakes/arrow-lake.html"><circle cx="700" cy="380" r="10" fill="#C2571A"/><text x="630" y="410" font-size="13">Arrow Lakes</text></a>
<a href="/lakes/kalamalka-lake.html"><circle cx="380" cy="150" r="8" fill="#E89F3B"/><text x="394" y="154" font-size="12">Kalamalka</text></a>
<a href="/lakes/mabel-lake.html"><circle cx="700" cy="220" r="8" fill="#E89F3B"/><text x="714" y="224" font-size="12">Mabel</text></a>
</g>

<!-- Labels for geography -->
<g font-family="Inter, system-ui, sans-serif" font-size="11" fill="#46545A" letter-spacing="0.1em">
<text x="20" y="40" font-weight="700">BC INTERIOR LAKES</text>
<text x="20" y="56">Scale approximate · not navigational</text>
<text x="322" y="500" text-anchor="middle" font-size="13" fill="#0E3B4F" font-weight="600">KELOWNA</text>
</g>
</svg>
<p style="color:var(--muted);font-size:.85rem;margin-top:12px;text-align:center">Tap any pin to explore that lake's fishery.</p>
</div>

<div class="grid grid-3" style="margin-top:40px">
<a class="card" href="/lakes/okanagan-lake.html"><img src="/assets/img/okanagan-lake-1024x682.jpg" alt="Okanagan Lake" loading="lazy"/><div class="card-body"><span class="card-meta">Home water · daily</span><h3>Okanagan Lake</h3><p>80% of our charters. Kokanee, rainbow, lake trout.</p><span class="link">Explore →</span></div></a>
<a class="card" href="/lakes/shuswap-lake.html"><img src="/assets/img/shuswap-lake-1024x682.jpg" alt="Shuswap Lake" loading="lazy"/><div class="card-body"><span class="card-meta">Multi-species</span><h3>Shuswap Lake</h3><p>Chinook, lake trout, rainbow, burbot.</p><span class="link">Explore →</span></div></a>
<a class="card" href="/lakes/arrow-lake.html"><img src="/assets/img/arrow-lake-1024x682.jpg" alt="Arrow Lakes" loading="lazy"/><div class="card-body"><span class="card-meta">Trophy water</span><h3>Arrow Lakes</h3><p>Gerrard rainbow, bull trout, kokanee.</p><span class="link">Explore →</span></div></a>
<a class="card" href="/lakes/kalamalka-lake.html"><img src="/assets/img/okanagan-lake-1024x682.jpg" alt="Kalamalka Lake" loading="lazy"/><div class="card-body"><span class="card-meta">On request</span><h3>Kalamalka Lake</h3><p>Turquoise water, lighter-pressured fishery.</p><span class="link">Explore →</span></div></a>
<a class="card" href="/lakes/mabel-lake.html"><img src="/assets/img/mountain-and-lake-at-sunset-135157.jpg" alt="Mabel Lake" loading="lazy"/><div class="card-body"><span class="card-meta">Remote · by request</span><h3>Mabel Lake</h3><p>Trophy rainbow and fall bull trout.</p><span class="link">Explore →</span></div></a>
</div>
</div></section>''' + cta_band("Pick a lake, book a trip")
PAGES.append(("/guides/kelowna-lake-map.html", page(
    "Kelowna Lake Coverage Map — Outdoor Adventures BC",
    "Interactive map of the BC interior lakes where Outdoor Adventures BC runs fishing charters: Okanagan, Shuswap, Arrow, Kalamalka, Mabel.",
    "/guides/kelowna-lake-map.html", map_body, og_image="/assets/img/og/lakes.jpg")))

# ---- WRITE ----
for path, html in PAGES:
    write(path, html)
print(f"\nphase 4: {len(PAGES)} pages")
