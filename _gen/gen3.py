#!/usr/bin/env python3
"""Phase 3 expansion: Stay+Fish, species pages, new charter specialties, new areas + lakes, pillar pages."""
import pathlib

ROOT = pathlib.Path(__file__).parent.parent
AIRBNB = "https://www.airbnb.ca/rooms/1546682788737611961?unique_share_id=bcc7551a-fb6e-4e6c-874c-aebdf391579b"

NAV = '''<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><span>Outdoor Adventures BC</span></a><button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul><li><a class="navlink" href="/kelowna-fishing-charters.html">Charters</a></li><li><a class="navlink" href="/sightseeing-tours.html">Sightseeing</a></li><li><a class="navlink" href="/pricing.html">Pricing</a></li><li><a class="navlink" href="/blog/">Blog</a></li><li><a class="navlink" href="/reviews.html">Reviews</a></li><li><a class="btn btn-primary" href="/contact.html">Book</a></li></ul></div></header>'''

FOOTER = '''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><p>Kelowna-based fishing charters and sightseeing tours on Okanagan, Shuswap and Arrow Lakes.</p><p style="margin-top:8px"><a href="tel:+12509028323" style="color:#fff;font-weight:600">250-902-8323</a></p></div><div><h4>Charters</h4><ul><li><a href="/kelowna-fishing-charters.html">Fishing Charters</a></li><li><a href="/charters/half-day-charter.html">Half-day</a></li><li><a href="/charters/full-day-charter.html">Full-day</a></li><li><a href="/charters/sunset-cruise.html">Sunset cruise</a></li><li><a href="/charters/proposal-cruise.html">Proposal cruise</a></li><li><a href="/charters/bachelor-party-charter.html">Bachelor/ette</a></li><li><a href="/charters/birthday-charter.html">Birthday charter</a></li><li><a href="/gift-certificates.html">Gift certificates</a></li></ul></div><div><h4>Lakes & species</h4><ul><li><a href="/species/">Species guide</a></li><li><a href="/species/kokanee-salmon.html">Kokanee salmon</a></li><li><a href="/species/rainbow-trout.html">Rainbow trout</a></li><li><a href="/species/lake-trout.html">Lake trout</a></li><li><a href="/lakes/okanagan-lake.html">Okanagan Lake</a></li><li><a href="/lakes/shuswap-lake.html">Shuswap Lake</a></li><li><a href="/lakes/arrow-lake.html">Arrow Lakes</a></li></ul></div><div><h4>Plan your trip</h4><ul><li><a href="/things-to-do-kelowna.html">Things to do in Kelowna</a></li><li><a href="/stay-fish.html">Stay + Fish</a></li><li><a href="/guides/">Local guides</a></li><li><a href="/catches/">Recent catches</a></li><li><a href="/captain.html">Meet Dennis</a></li><li><a href="/refer.html">Refer a friend</a></li><li><a href="/waiver.html">Digital waiver</a></li><li><a href="/contact.html">Contact</a></li><li><a href="''' + AIRBNB + '''" rel="noopener" target="_blank">Stay+Fish Airbnb</a></li></ul></div></div><div class="footer-bottom"><span>© <span data-year></span> Outdoor Adventures BC · Kelowna, BC · Built by <a href="https://elliotdigital.ca" rel="noopener" style="color:#fff">Elliot Digital</a></span><span><a href="/legal/privacy.html">Privacy</a> · <a href="/legal/terms.html">Terms</a> · <a href="/legal/cancellation-policy.html">Cancellations</a></span></div></div></footer>'''

TAIL = '''<a href="tel:+12509028323" class="fab-call" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.8 19.8 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72 12.8 12.8 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.8 12.8 0 002.81.7A2 2 0 0122 16.92z"/></svg></a>
<div class="sticky-book"><div class="sticky-book-inner"><span><strong>$200/hr</strong> · Kelowna charter</span><a href="/contact.html" class="btn btn-primary">Book</a></div></div>
<script src="/assets/js/main.js" defer></script>'''

HEAD = '''<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#0E3B4F"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap"/><link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png"/><link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16.png"/><link rel="apple-touch-icon" sizes="180x180" href="/assets/img/favicon-180.png"/><link rel="manifest" href="/site.webmanifest"/><link rel="stylesheet" href="/assets/css/styles.css"/>'''

def page(title, desc, url, body, schema="", og_image="/assets/img/captain-trophy-rainbow.jpg"):
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

def hero(eyebrow, h1, lede, bg, breadcrumbs=""):
    return f'''<section class="hero" style="--hero-img:url('{bg}'); min-height:min(65vh,520px)"><div class="container hero-inner">
{f'<nav class="breadcrumbs" style="color:rgba(255,255,255,.8)">{breadcrumbs}</nav>' if breadcrumbs else ''}
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="hero-cta"><a class="btn btn-primary btn-lg" href="/contact.html">Book a Charter</a><a class="btn btn-ghost btn-lg" style="color:#fff;border-color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div>
</div></section>'''

def cta_band(title, sub="$200/hr · 7 days a week · up to 6 guests"):
    return f'''<section class="section" style="padding-top:0"><div class="container"><div class="price-band"><div><h2>{title}</h2><p style="opacity:.9;margin:0">{sub}</p></div><div class="cta-col"><a class="btn btn-primary btn-lg" href="/contact.html">Request a Booking</a><a class="btn" style="color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div></div></div></section>'''

def write(path, html):
    p = ROOT / path.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print(f"+ {path}")

PAGES = []

# ========= STAY + FISH DEDICATED PAGE =========
stay_fish_body = f'''{hero("Stay + Fish · Kelowna", "Kelowna Fishing Accommodation", "Book the charter, book the stay — both hosted by the same local. Dennis's Kelowna Airbnb is the easiest way to turn a fishing trip into a proper Okanagan weekend.", "/assets/img/moonlit-dock.jpg",
breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Stay + Fish')}

<section class="section"><div class="container"><div class="split"><div class="prose">
<span class="eyebrow">Where to stay for a Kelowna fishing trip</span>
<h2>One host. One captain. Zero logistics.</h2>
<p>Most visiting anglers waste their first morning figuring out logistics — where to launch, where the captain is meeting you, where to stash the cooler, how to get back to the hotel. Stay+Fish removes all of it.</p>
<p>Dennis Barnes is both the captain of Outdoor Adventures BC <em>and</em> the host of a Kelowna Airbnb built specifically for visiting anglers and families. Book both in one conversation and you get a smoother trip at a bundled rate.</p>
<h2>Why anglers pick Stay+Fish</h2>
<ul>
<li><strong>Early-morning check-in compatible</strong> — no 4 pm hotel lockout stopping your dawn launch</li>
<li><strong>Same host as your charter</strong> — one text thread for the whole trip</li>
<li><strong>Cooler / catch storage</strong> — fridge space for the fish you take home</li>
<li><strong>Quiet location</strong> — sleep well, fish well</li>
<li><strong>Bundle pricing</strong> — discount when you book stay + charter together</li>
</ul>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:20px"><a class="btn btn-primary btn-lg" href="{AIRBNB}" target="_blank" rel="noopener">View the Airbnb on Airbnb</a><a class="btn btn-secondary btn-lg" href="/contact.html?bundle=stay-fish">Ask about the bundle</a></div>
</div><div class="split-media"><img src="/assets/img/moonlit-dock.jpg" alt="Dennis's Kelowna Airbnb — lakeside stay a short drive from the boat launch" loading="lazy"/></div></div></div></section>

<section class="section" style="padding-top:0"><div class="container">
<div class="section-head reveal"><span class="eyebrow">How it works</span><h2>Three simple steps</h2></div>
<div class="grid grid-3">
<div class="card reveal"><div class="card-body"><span class="card-meta">Step 1</span><h3>Book the stay</h3><p>View the <a href="{AIRBNB}" target="_blank" rel="noopener">Airbnb listing</a> and book your dates directly.</p></div></div>
<div class="card reveal delay-1"><div class="card-body"><span class="card-meta">Step 2</span><h3>Book the charter</h3><p>Mention Stay+Fish when you request your <a href="/contact.html">charter</a> and we'll apply the bundle discount.</p></div></div>
<div class="card reveal delay-2"><div class="card-body"><span class="card-meta">Step 3</span><h3>Show up, fish</h3><p>Check in, sleep well, walk to the boat ramp. The whole experience is coordinated by one person.</p></div></div>
</div>
</div></section>

{cta_band("Plan a Kelowna fishing weekend", sub="Stay + charter, one host, one text thread.")}
'''

# JSON-LD: Accommodation schema
stay_schema = f'''<script type="application/ld+json">{{
"@context":"https://schema.org","@type":"LodgingBusiness",
"name":"Outdoor Adventures BC Stay+Fish Airbnb",
"description":"Kelowna short-term rental hosted by Dennis Barnes, owner of Outdoor Adventures BC fishing charters. Purpose-built for visiting anglers and families.",
"url":"{AIRBNB}","image":"https://outdooradventuresbc.ca/assets/img/moonlit-dock.jpg",
"address":{{"@type":"PostalAddress","addressLocality":"Kelowna","addressRegion":"BC","addressCountry":"CA"}},
"geo":{{"@type":"GeoCoordinates","latitude":49.888,"longitude":-119.496}},
"priceRange":"$$"
}}</script>'''

PAGES.append(("/stay-fish.html", page(
    "Stay + Fish Kelowna — Fishing Trip Accommodation | Outdoor Adventures BC",
    "Kelowna fishing accommodation hosted by captain Dennis Barnes. Book the charter + stay bundle for a smoother Okanagan Lake fishing weekend.",
    "/stay-fish.html", stay_fish_body, stay_schema, og_image="/assets/img/moonlit-dock.jpg")))

# ========= SPECIES HUB =========
species_hub_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Species guide</nav>
<div class="section-head reveal"><span class="eyebrow">What we catch</span><h1 style="font-size:clamp(2rem,4vw,3rem)">BC interior-lake species guide</h1><p>Everything we target on a Kelowna fishing charter — how to catch each, when they bite, and where they live on Okanagan, Shuswap and Arrow Lakes.</p></div>
<div class="grid grid-3">
  <a class="card reveal" href="/species/kokanee-salmon.html"><img src="/assets/img/trophy-rainbow-in-net.jpg" alt="Kokanee salmon" loading="lazy"/><div class="card-body"><span class="card-meta">Okanagan Lake · May–Aug</span><h3>Kokanee salmon</h3><p>Landlocked sockeye. The flagship fish of Okanagan Lake.</p><span class="link">Read species page →</span></div></a>
  <a class="card reveal delay-1" href="/species/rainbow-trout.html"><img src="/assets/img/captain-trophy-rainbow.jpg" alt="Rainbow trout" loading="lazy"/><div class="card-body"><span class="card-meta">Year-round</span><h3>Rainbow trout</h3><p>Okanagan's bread-and-butter trout. Aggressive, acrobatic, everywhere.</p><span class="link">Read species page →</span></div></a>
  <a class="card reveal delay-2" href="/species/lake-trout.html"><img src="/assets/img/stern-trolling-okanagan.jpg" alt="Lake trout" loading="lazy"/><div class="card-body"><span class="card-meta">Spring / Fall</span><h3>Lake trout</h3><p>Deep, cold-water predator. Trophy fish in the 10+ lb range.</p><span class="link">Read species page →</span></div></a>
  <a class="card reveal" href="/species/gerrard-rainbow.html"><img src="/assets/img/arrow-lake-1024x682.jpg" alt="Gerrard rainbow trout" loading="lazy"/><div class="card-body"><span class="card-meta">Arrow Lakes · trophy</span><h3>Gerrard rainbow</h3><p>BC's famed landlocked giant — 20+ lb possible.</p><span class="link">Read species page →</span></div></a>
  <a class="card reveal delay-1" href="/species/bull-trout.html"><img src="/assets/img/mountain-and-lake-at-sunset-135157.jpg" alt="Bull trout" loading="lazy"/><div class="card-body"><span class="card-meta">Arrow / Shuswap · Fall</span><h3>Bull trout</h3><p>Big, toothy, aggressive. A fall favourite on Arrow Lake.</p><span class="link">Read species page →</span></div></a>
  <a class="card reveal delay-2" href="/species/chinook-burbot.html"><img src="/assets/img/shuswap-lake-1024x682.jpg" alt="Chinook and burbot" loading="lazy"/><div class="card-body"><span class="card-meta">Shuswap · seasonal</span><h3>Chinook & burbot</h3><p>Shuswap specialties: summer chinook, winter burbot.</p><span class="link">Read species page →</span></div></a>
</div></div></section>'''
PAGES.append(("/species/index.html", page("BC Interior Lake Species Guide — Outdoor Adventures BC",
    "Complete species guide for Kelowna fishing charters — kokanee, rainbow, lake trout, Gerrard rainbow, bull trout, chinook, burbot.",
    "/species/", species_hub_body)))

# ---- Species pages ----
def species_page(slug, name, latin, habitat, size, season, tactic, lede, body_html, img):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Taxon","name":"{name}","scientificName":"{latin}","parentTaxon":{{"@type":"Taxon","name":"Salmonidae"}}}}</script>'
    body = f'''{hero(f"{name} · {season}", f"{name} — Okanagan & BC Interior", lede, img,
        breadcrumbs=f'<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › <a href="/species/" style="color:rgba(255,255,255,.8)">Species</a> › {name}')}
<section class="section"><div class="container"><div class="prose" style="max-width:820px;margin:0 auto">
<div class="facts-box"><h3>Quick facts</h3><dl>
<dt>Scientific name</dt><dd><em>{latin}</em></dd>
<dt>Habitat</dt><dd>{habitat}</dd>
<dt>Typical size</dt><dd>{size}</dd>
<dt>Peak season</dt><dd>{season}</dd>
<dt>How we catch them</dt><dd>{tactic}</dd>
</dl></div>
{body_html}
<hr/>
<p><strong>Want to catch one?</strong> <a href="/contact.html">Book a Kelowna charter</a> and we'll put you on them.</p>
</div></div></section>
{cta_band(f"Book a {name} trip")}'''
    return page(f"{name} Fishing — Okanagan Lake & BC Interior | Outdoor Adventures BC",
        f"How to catch {name.lower()} on Okanagan, Shuswap and Arrow Lakes — tactics, season, size and where they live. From a Kelowna charter captain.",
        f"/species/{slug}.html", body, schema, og_image=img)

PAGES.append(("/species/kokanee-salmon.html", species_page(
    "kokanee-salmon", "Kokanee salmon", "Oncorhynchus nerka", "Deep, clear, cold-water lakes. Okanagan and Kootenay systems.",
    "1–3 lbs typical, 4+ lbs trophy", "May–August", "Downrigger trolling at 1.2–1.6 mph with small dodgers + hoochies",
    "Kokanee are landlocked sockeye salmon — the flagship species of Okanagan Lake and the fish most Kelowna charters are built around.",
    """<h2>What makes them special</h2>
<p>Kokanee are the freshwater-locked form of the Pacific sockeye. They grow up, mature and die all in lakes like Okanagan, never touching saltwater. They're smaller than ocean-run sockeye — usually 1–3 lbs — but they fight hard and the flesh is the same brilliant orange.</p>
<h2>Where they live in Okanagan Lake</h2>
<p>In summer, kokanee suspend over the mid-lake basins at 40–80 ft down over 150–250 ft of water. They follow thermoclines and baitfish schools. The stretch from Knox Mountain south to Peachland is the classic summer kokanee zone.</p>
<h2>How we fish them</h2>
<p>Downrigger trolling is the only reliable method. We run 4-inch Mack's Sling Blade dodgers in silver, chrome or UV purple, with 4–6 ft leaders to mini-hoochies in pink, purple, or UV white. Tipped with Pautzke Fire Corn. Speed 1.2–1.6 mph.</p>
<h2>The bite</h2>
<p>Kokanee have soft mouths — the rod loads up gradually, there's no big slam. We set releases loose and fight fish with constant pressure; pumping tears the hook through their paper-thin jaw.</p>
<h2>Eating</h2>
<p>Kokanee are outstanding on the grill or smoked. The fat content is higher than rainbow; a brine + alder smoke is the Okanagan classic.</p>
<h2>See also</h2>
<ul><li><a href="/blog/kokanee-trolling-setup-guide.html">The exact kokanee setup we run</a></li><li><a href="/lakes/okanagan-lake.html">Fishing Okanagan Lake</a></li><li><a href="/blog/best-time-fish-okanagan-lake.html">Best time to fish Okanagan Lake</a></li></ul>""",
    "/assets/img/trophy-rainbow-in-net.jpg")))

PAGES.append(("/species/rainbow-trout.html", species_page(
    "rainbow-trout", "Rainbow trout", "Oncorhynchus mykiss", "Cold, clean lakes and rivers across BC.",
    "2–6 lbs typical, 10+ lbs trophy", "Year-round, peaks spring & fall", "Trolling spoons, bucktails, Apex plugs at 25–40 ft",
    "The Okanagan's most-caught sportfish. Aggressive, acrobatic, and feeding year-round.",
    """<h2>Why they're everywhere</h2>
<p>Rainbow trout are BC's most stocked and most-fished species. Native to the Pacific Northwest, they've adapted to nearly every cold-water system in the interior. On Okanagan Lake, they're the species you can count on every month of the year.</p>
<h2>Where</h2>
<p>Rainbow feed shallower than kokanee — the 20–40 ft shelf along the east shore from the Mission to Gellatly is textbook trolling water. Creek mouths (Mission Creek, Mill Creek, Bear Creek) concentrate baitfish and hold fish at first light.</p>
<h2>How we fish them</h2>
<p>Trolling is primary — Needlefish spoons in chrome, Apex plugs in rainbow-trout colours, bucktails behind small flashers. On our charters we typically run 2 rods rigged differently and let the fish tell us what they want that day.</p>
<h2>The fight</h2>
<p>Rainbows jump. Often multiple times. The fight is acrobatic, not deep — they stay near the surface and thrash. Keep the rod tip up and let the drag do the work.</p>
<h2>See also</h2>
<ul><li><a href="/catches/">Recent rainbow-trout catch reports</a></li><li><a href="/lakes/okanagan-lake.html">Okanagan Lake rainbow spots</a></li><li><a href="/guides/where-to-fish-okanagan-lake.html">Where to fish Okanagan Lake</a></li></ul>""",
    "/assets/img/captain-trophy-rainbow.jpg")))

PAGES.append(("/species/lake-trout.html", species_page(
    "lake-trout", "Lake trout", "Salvelinus namaycush", "Deep, cold Canadian lakes. Okanagan, Shuswap.",
    "5–12 lbs typical, 20+ lbs trophy", "Spring (pre-turnover), Fall (post-turnover), Winter",
    "Deep jigging 80–180 ft with white tubes; downrigger trolling cooler months",
    "Okanagan's deep-water predator. The biggest fish most guests will catch on our boat.",
    """<h2>What they are</h2>
<p>Lake trout (also called mackinaw, lakers, or grey trout) are the largest char native to North America. They live deep, grow slow, and can easily hit 15–20 lbs in Okanagan Lake.</p>
<h2>Seasonality matters</h2>
<p>Lake trout are cold-water fish. In summer when surface temps climb above 18°C they retreat to the 100–200 ft zone and become a dedicated-trip species. In spring and fall they're higher in the column — sometimes at 30–50 ft — and far more catchable on standard gear.</p>
<h2>How we fish them</h2>
<p>Two methods dominate. <strong>Deep jigging</strong>: 2-oz white tubes or airplane jigs dropped to bottom in 80–180 ft. Lift and drop, pause on the drop — 80% of bites come as the jig falls. <strong>Downrigger trolling</strong>: large plugs in rainbow or kokanee patterns behind flashers, 80–150 ft down.</p>
<h2>Handling trophies</h2>
<p>Big lakers are old fish. We practice quick, in-water releases on anything over 10 lbs. Unhook in the net, photograph while the fish is still supported in the water, and send it back.</p>
<h2>See also</h2>
<ul><li><a href="/lakes/okanagan-lake.html">Lake-trout spots on Okanagan Lake</a></li><li><a href="/blog/best-time-fish-okanagan-lake.html">Best time for lake trout</a></li></ul>""",
    "/assets/img/stern-trolling-okanagan.jpg")))

PAGES.append(("/species/gerrard-rainbow.html", species_page(
    "gerrard-rainbow", "Gerrard rainbow trout", "Oncorhynchus mykiss (Gerrard strain)", "Upper Arrow Lake and Kootenay Lake systems.",
    "8–15 lbs typical, 25+ lbs trophy", "Spring (spawn run), Fall",
    "Big-bait trolling near Lardeau River mouth; trophy-targeted trips",
    "BC's most famous trophy rainbow. A genetically distinct strain that grows to 25+ lbs.",
    """<h2>Why they're legendary</h2>
<p>The Gerrard rainbow is a unique strain of rainbow trout found in the Kootenay/Arrow Lake system. Unlike most rainbow which max out around 10 lbs, Gerrards can exceed 25 lbs — the second-largest rainbow trout in the world after the Kamloops strain in the same region.</p>
<h2>The feeding biology</h2>
<p>Gerrards grow big because they feed on kokanee — a high-fat food source that lets them pack on weight fast. Where there are dense kokanee populations, Gerrards follow.</p>
<h2>When we fish them</h2>
<p>Late winter through spring, as they stage for the Lardeau River spawn. Also fall, when they're actively feeding heavy before winter. We time Gerrard charters to the conditions.</p>
<h2>How we fish them</h2>
<p>Big-bait trolling. Large plugs, 6-inch spoons, sometimes whole herring on downriggers. This is not a numbers game — the expectation is 1–2 bites on a good day, any of which could be a trip-of-a-lifetime fish.</p>
<h2>See also</h2>
<ul><li><a href="/lakes/arrow-lake.html">Arrow Lakes fishing</a></li><li><a href="/charters/full-day-charter.html">Full-day Arrow trips</a></li></ul>""",
    "/assets/img/arrow-lake-1024x682.jpg")))

PAGES.append(("/species/bull-trout.html", species_page(
    "bull-trout", "Bull trout", "Salvelinus confluentus", "Cold, clean BC rivers and lakes. Arrow and Shuswap systems.",
    "4–10 lbs typical, 15+ lbs trophy", "Fall peaks; year-round possible",
    "Trolling large plugs on downriggers; predator-pattern presentations",
    "Apex predator of BC cold water. Big, toothy, and aggressive — a favourite Arrow Lake fall species.",
    """<h2>What they are</h2>
<p>Bull trout are a native BC char — close cousins to lake trout and Dolly Varden. They're fish-eaters, purely predatory, and grow to trophy size in cold lakes with dense baitfish populations.</p>
<h2>Where</h2>
<p>Arrow Lakes hold the strongest populations in our charter area. They're less common on Okanagan Lake, though not absent. In Arrow, they hang near kokanee schools all year and move shallow in fall to feed aggressively.</p>
<h2>How we fish them</h2>
<p>Big-bait trolling. 5–7 inch plugs in rainbow, kokanee or whitefish patterns, run deep on downriggers. Bull trout attack — expect a violent rod-loading strike unlike the soft bite of a kokanee.</p>
<h2>Regulations</h2>
<p>Catch-and-release only in most waters where we fish them, with mandatory barbless hooks and careful handling. Check the current BC Freshwater Fishing Regulations Synopsis before your trip; we rig all our bull-trout gear to comply.</p>
<h2>See also</h2>
<ul><li><a href="/lakes/arrow-lake.html">Arrow Lakes bull-trout fishing</a></li></ul>""",
    "/assets/img/mountain-and-lake-at-sunset-135157.jpg")))

PAGES.append(("/species/chinook-burbot.html", species_page(
    "chinook-burbot", "Chinook & burbot", "Oncorhynchus tshawytscha & Lota lota", "Shuswap Lake system.",
    "Chinook 5–15 lbs, burbot 3–8 lbs", "Chinook summer; burbot winter",
    "Chinook: downrigger trolling. Burbot: winter jigging with heavy jigs + bait",
    "Shuswap specialties — summer chinook salmon trolling and winter burbot jigging.",
    """<h2>Landlocked chinook</h2>
<p>Shuswap Lake holds a landlocked population of chinook salmon — freshwater-adapted kings. They grow slower and smaller than ocean chinook but still hit 10+ lbs and put up a proper fight.</p>
<h2>When we fish them</h2>
<p>Summer. Specifically late June through August. Deep trolling (80–120 ft) with big Apex plugs or squid-pattern hoochies.</p>
<h2>Burbot (ling cod of the lake)</h2>
<p>Burbot are a freshwater cod. Ugly, weird, and absolutely delicious. They come alive in winter when surface temps are coldest and the rest of the lake slows down. We jig for them at 60–120 ft over structural drop-offs, heavy jigs tipped with cut bait, fished right on bottom.</p>
<h2>Burbot eating</h2>
<p>Often called "poor man's lobster" for a reason. Firm white flesh, similar to cod. Worth the weird-looking species photo.</p>
<h2>See also</h2>
<ul><li><a href="/lakes/shuswap-lake.html">Shuswap Lake fishing</a></li></ul>""",
    "/assets/img/shuswap-lake-1024x682.jpg")))

# ========= NEW CHARTER SPECIALTIES =========
def charter_specialty(slug, title, h1, lede, long_copy, og_image, price_note=""):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{h1}","provider":{{"@type":"LocalBusiness","name":"Outdoor Adventures BC"}},"areaServed":{{"@type":"City","name":"Kelowna, BC"}},"offers":{{"@type":"Offer","price":"200.00","priceCurrency":"CAD","priceSpecification":{{"@type":"UnitPriceSpecification","price":"200.00","priceCurrency":"CAD","unitText":"HOUR"}}}}}}</script>'
    body = f'''{hero(f"Private · Kelowna", h1, lede, og_image,
        breadcrumbs=f'<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Charters › {h1.split("—")[0].strip() if "—" in h1 else h1}')}
<section class="section"><div class="container"><div class="split"><div class="prose">
{long_copy}
{price_note}
</div><div class="split-media"><img src="{og_image}" alt="{h1}" loading="lazy"/></div></div></div></section>
{cta_band(f"Plan a {h1.split('—')[0].strip().lower() if '—' in h1 else h1.lower()}")}'''
    return page(title, lede, f"/charters/{slug}.html", body, schema, og_image)

PAGES.append(("/charters/bachelor-party-charter.html", charter_specialty(
    "bachelor-party-charter",
    "Bachelor & Bachelorette Boat Charters Kelowna — Outdoor Adventures BC",
    "Bachelor & Bachelorette Boat Charters",
    "Private captained boat for your Kelowna bachelor or bachelorette party. Sunset cruise, wine-country shoreline, heated cabin, Bluetooth audio — plus the photos to prove you had a better time than the bros who went to Vegas.",
    """<span class="eyebrow">Stag / stagette-ready</span><h2>A real Kelowna bachelor/ette weekend</h2>
<p>Kelowna is the best stag town in BC for a reason. Vineyards, lakes, beaches, patios. A private boat charter with Outdoor Adventures BC is the centerpiece — 2–4 hours on Okanagan Lake with your crew, heated cabin, fridge full of whatever you brought, Bluetooth audio, and a captain who's seen it all and judged none of it.</p>
<h2>What makes us different</h2>
<ul><li>Fully private — just your group, no strangers onboard</li><li>Up to 6 guests; split larger parties across 2 boats on request</li><li>Pickup from hotel waterfronts downtown — no rental-car logistics</li><li>Bring your own food, wine, cans, whatever your lawyer is comfortable with</li><li>Custom routes — we'll cruise wineries, sandy beaches, cliff jumps, whatever the group wants</li></ul>
<div class="facts-box"><h3>Typical trip</h3><dl><dt>Duration</dt><dd>2 hours (cocktail cruise) to 4 hours (afternoon on the lake)</dd><dt>Capacity</dt><dd>Up to 6 guests per boat</dd><dt>Rate</dt><dd>$400 for 2 hours / $800 for 4 hours</dd><dt>Add-ons</dt><dd>Catering, branded photos, custom Spotify playlist</dd></dl></div>""",
    "/assets/img/rods-sunset-trolling.jpg")))

PAGES.append(("/charters/birthday-charter.html", charter_specialty(
    "birthday-charter",
    "Kelowna Birthday Boat Charter — Private Okanagan Lake Cruise",
    "Kelowna Birthday Boat Charters",
    "Turn a Kelowna birthday into something people actually talk about. Private captained charter on Okanagan Lake — fishing, sightseeing, or sunset — your call.",
    """<span class="eyebrow">Milestone birthdays our specialty</span><h2>Birthdays on the water</h2>
<p>40th. 50th. 60th. Any big round number that deserves more than a restaurant reservation. We run private Kelowna birthday charters year-round — fishing, sightseeing, or a sunset cruise — fully tuned to what the birthday person actually wants.</p>
<h2>Popular birthday formats</h2>
<ul><li><strong>Half-day fishing</strong> — for the angler whose family finally asked what they really wanted</li><li><strong>Sunset cruise</strong> — for the family gathering where nobody wants to drink-and-drive home</li><li><strong>All-day</strong> — milestone trips where you want the full Kelowna experience on the water</li></ul>
<h2>We handle</h2>
<p>Candles, a cake-friendly flat surface (we have a proper dinette table inside), custom playlist, catering pickup from your favourite Kelowna spot. Tell us what the birthday person loves and we build the trip around it.</p>""",
    "/assets/img/okanagan-dusk-cruise.jpg")))

PAGES.append(("/charters/proposal-cruise.html", charter_specialty(
    "proposal-cruise",
    "Proposal Cruise Kelowna — Private Sunset Boat | Outdoor Adventures BC",
    "Proposal Cruises on Okanagan Lake",
    "Propose on a private sunset boat on Okanagan Lake. Champagne, heated cabin, golden-hour light, and zero strangers watching. We've done this before.",
    """<span class="eyebrow">Private · discreet</span><h2>The Kelowna proposal done right</h2>
<p>Restaurants are crowded. Vineyards are photographed by strangers. A private sunset cruise on Okanagan Lake is the best proposal venue in the Okanagan — and we've helped set up dozens of them.</p>
<h2>What we handle</h2>
<ul><li>Private 2-hour sunset cruise — just the two of you (or a small surprise party)</li><li>Champagne + ice + glasses onboard</li><li>Flowers and the perfect "drop the engine, walk to the bow" moment</li><li>A photographer / videographer if you want the moment captured — we partner with a local Kelowna photographer</li><li>Your playlist, ready to hit at the right second</li></ul>
<h2>How it works</h2>
<p>We plan the route so the sun is behind you at the moment you ask. We stage the boat in a quiet bay. We kill the engine and pretend we're fixing a fuse. You go get engaged. Takes 2–3 minutes. Everybody cries. Then we pop the cork.</p>
<div class="facts-box"><h3>Proposal package</h3><dl><dt>Duration</dt><dd>2 hours</dd><dt>Price</dt><dd>$400 base + optional add-ons</dd><dt>Add-ons</dt><dd>Champagne $75 · Flowers from $50 · Professional photography from $350 · Catering on request</dd><dt>Success rate</dt><dd>100% (she always says yes)</dd></dl></div>""",
    "/assets/img/rods-sunset-trolling.jpg")))

PAGES.append(("/charters/anniversary-charter.html", charter_specialty(
    "anniversary-charter",
    "Anniversary Cruise Kelowna — Private Sunset Boat Charter",
    "Kelowna Anniversary Cruises",
    "A private Okanagan Lake sunset cruise for your anniversary. Heated cabin, golden light, champagne optional. Adults-only, no strangers, just you two (or the family).",
    """<span class="eyebrow">Milestone-anniversary ready</span><h2>The Kelowna anniversary done properly</h2>
<p>You've done dinner. You've done the winery tour. A private sunset cruise is a fresh way to mark 10, 25, or 50 years together — on the water, in good light, with nobody else around.</p>
<ul><li>2-hour private cruise · $400</li><li>3-hour extended cruise · $600</li><li>Champagne + flowers add-ons</li><li>Family-anniversary option — bring the kids/grandkids for a daytime cruise instead</li></ul>
<p>Book a few weeks ahead for dates in late spring through early fall when the light is best.</p>""",
    "/assets/img/mountain-and-lake-at-sunset-135157.jpg")))

# ========= NEW AREAS =========
def area_page(slug, city, lat_lng, desc, copy):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{city} Fishing Charter","provider":{{"@type":"LocalBusiness","name":"Outdoor Adventures BC","telephone":"+1-250-902-8323"}},"areaServed":{{"@type":"City","name":"{city}, BC"}},"offers":{{"@type":"Offer","price":"200.00","priceCurrency":"CAD","priceSpecification":{{"@type":"UnitPriceSpecification","price":"200.00","priceCurrency":"CAD","unitText":"HOUR"}}}}}}</script>'
    body = f'''{hero(f"{city} · Okanagan", f"{city} Fishing Charters", desc, "/assets/img/okanagan-lake-1024x682.jpg",
        breadcrumbs=f'<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Areas › {city}')}
<section class="section"><div class="container"><div class="prose" style="max-width:820px;margin:0 auto">
<span class="eyebrow">About {city} charters</span><h2>What to expect</h2>
{copy}
<div class="facts-box"><h3>{city} charter details</h3><dl>
<dt>Rate</dt><dd>$200 CAD / hour, up to 6 guests</dd>
<dt>Duration</dt><dd>4, 6 or 8 hours</dd>
<dt>Target species</dt><dd>Kokanee salmon, rainbow trout, lake trout</dd>
<dt>Launch</dt><dd>{city} or Kelowna ramp (whichever suits you)</dd>
<dt>Included</dt><dd>Captain, boat, rods, reels, tackle, bait, life jackets</dd>
</dl></div>
</div></div></section>
{cta_band(f"Book a {city} fishing charter")}'''
    return page(f"{city} Fishing Charters on Okanagan Lake — Outdoor Adventures BC",
        f"Guided {city} fishing charters on Okanagan Lake. $200/hr, up to 6 guests, all gear included. Outdoor Adventures BC.",
        f"/areas/{slug}.html", body, schema)

PAGES.append(("/areas/lake-country.html", area_page(
    "lake-country", "Lake Country",
    "50.0476,-119.4029",
    "Lake Country fishing charters on Okanagan Lake — the north end's kokanee and rainbow water. $200/hr with Outdoor Adventures BC.",
    """<p>Lake Country sits on the north end of Okanagan Lake — the quieter, less-developed stretch of shoreline with some of the best kokanee water in the valley. We regularly launch from Lake Country when the wind favours the north basin or when guests are staying in the Oyama / Winfield / Carr's Landing area.</p>
<p>The north end fishes slightly differently than Kelowna — cooler surface temps in summer push kokanee higher in the column, and the bays near Oyama Isthmus hold feeding fish. A Lake Country charter is typically 4–8 hours on the water, same $200/hr rate, same boat.</p>""")))

PAGES.append(("/areas/naramata.html", area_page(
    "naramata", "Naramata",
    "49.7500,-119.5931",
    "Naramata fishing charters on Okanagan Lake — south basin water and Naramata Bench vineyard views. Guided trips with Outdoor Adventures BC.",
    """<p>Naramata is one of the Okanagan's most beautiful stretches of shoreline — the Naramata Bench vineyards rise steep from the east side of the south basin, and the water below holds rainbow trout, lake trout, and productive kokanee structure.</p>
<p>We run Naramata charters for guests staying on the bench or at Penticton-area hotels who want a half-day on the water without the drive up to Kelowna. Meet us at Skaha or Okanagan launches and we'll be fishing within 30 minutes.</p>""")))

PAGES.append(("/areas/summerland.html", area_page(
    "summerland", "Summerland",
    "49.5986,-119.6694",
    "Summerland fishing charters on Okanagan Lake — south Okanagan guided trips for kokanee and lake trout. Outdoor Adventures BC.",
    """<p>Summerland sits on the west side of the south basin of Okanagan Lake, between Peachland and Penticton. The south basin is deep, cool, and holds a resident population of lake trout year-round — plus kokanee on the summer troll.</p>
<p>Summerland-based charters can meet you at local launches or pick up from a Kelowna departure point if you'd rather combine the drive with the water.</p>""")))

# ========= NEW LAKES =========
def lake_page(slug, lake, lat_lng, desc, content):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TouristAttraction","name":"{lake}","description":"Guided Kelowna-area fishing on {lake} with Outdoor Adventures BC."}}</script>'
    body = f'''{hero(f"{lake} · BC", f"{lake} Fishing Charters", desc, "/assets/img/shuswap-lake-1024x682.jpg",
        breadcrumbs=f'<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Lakes › {lake}')}
<section class="section"><div class="container"><div class="prose" style="max-width:820px;margin:0 auto">
{content}
</div></div></section>
{cta_band(f"Book a {lake} trip")}'''
    return page(f"{lake} Fishing Charters — Outdoor Adventures BC Kelowna",
        f"{lake} fishing charters with a Kelowna-based guide. $200/hr, all gear included. Outdoor Adventures BC.",
        f"/lakes/{slug}.html", body, schema)

PAGES.append(("/lakes/kalamalka-lake.html", lake_page(
    "kalamalka-lake", "Kalamalka Lake",
    "50.2085,-119.2739",
    "Kalamalka Lake fishing charters — crystal-clear turquoise water north of Kelowna. Rainbow trout and lake trout with Outdoor Adventures BC.",
    """<span class="eyebrow">The lake of many colours</span>
<h2>Fishing the emerald lake</h2>
<p>Kalamalka Lake is famous for its surreal turquoise colour — the result of calcium carbonate crystals reflecting sunlight. It's also a serious fishery for rainbow trout and lake trout, with less pressure than Okanagan Lake and spectacular clarity that makes sight-fishing possible in the right conditions.</p>
<h2>What we target</h2>
<ul><li><strong>Rainbow trout</strong> — suspended trolling at 20–40 ft</li><li><strong>Lake trout</strong> — deeper water, 60–120 ft, structure-oriented</li><li><strong>Kokanee</strong> — present but smaller than Okanagan Lake kokanee</li></ul>
<h2>Booking a Kal trip</h2>
<p>We run Kalamalka charters on request, usually for guests staying in Vernon or Lake Country who want the novelty of a less-fished lake. Same $200/hr rate, same boat.</p>""")))

PAGES.append(("/lakes/mabel-lake.html", lake_page(
    "mabel-lake", "Mabel Lake",
    "50.5867,-118.7872",
    "Mabel Lake fishing charters — a remote eastern-BC trophy lake for rainbow, bull trout and kokanee. Guided trips with Outdoor Adventures BC.",
    """<span class="eyebrow">Remote · trophy water</span>
<h2>Off the beaten path</h2>
<p>Mabel Lake sits east of the Shuswap — remote, deep, surrounded by mountains. Less than an hour from Enderby but feels like backcountry. The fishery is serious: large rainbow trout, bull trout in fall, and a healthy kokanee population.</p>
<h2>Who Mabel is for</h2>
<p>Experienced anglers who want a full-day trophy-hunt without the pressure of Okanagan Lake. Mabel charters are by request only and usually book 2+ weeks ahead.</p>
<h2>What to expect</h2>
<p>Full-day (8 hour) trip, $1,600. Limited keep-it days — most Mabel trips are catch-and-release. Spectacular scenery. Sometimes the best fishing day of your life, sometimes a slower day; remote lakes fish that way.</p>""")))

# ========= PILLAR PAGES =========
things_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Things to do in Kelowna</nav>
<div class="section-head reveal"><span class="eyebrow">Kelowna visitor guide</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Things to do in Kelowna (by a local)</h1><p>Dennis's pick-list for anyone visiting Kelowna for the first time — written by someone who's lived here and guided visitors for years. Biased toward the water, unapologetic about it.</p></div>

<div class="prose" style="max-width:820px;margin:0 auto">
<h2>1. Get on Okanagan Lake</h2>
<p>Bias warning: we run a fishing charter company. But genuinely — most visitors see the Okanagan from the highway and miss the whole point. A <a href="/kelowna-fishing-charters.html">half-day fishing charter</a> or <a href="/charters/sunset-cruise.html">sunset cruise</a> is the single best use of 2–4 hours in Kelowna. Walk off your hotel dock or meet us at Cook Road in 10 minutes.</p>

<h2>2. Hike Knox Mountain at sunset</h2>
<p>Free. 30–45 min hike. Best view in town. Go right before sunset and you'll see the same shoreline our charters cruise past.</p>

<h2>3. Okanagan wine country</h2>
<p>Mission Hill, Quails' Gate, CedarCreek, Tantalus. Pick 2 for a day, not 5. Wineries are a marathon; pace yourself. Many are doable by bike tour if you want to avoid the rental car + designated driver problem.</p>

<h2>4. Kelowna Farmers' Market (Wed/Sat)</h2>
<p>One of the best in BC. 80+ vendors, stone-fruit season (July–Sept) is the peak experience. Morning is best.</p>

<h2>5. Mission Creek Greenway</h2>
<p>Quiet walking/biking trail along the creek. Low-key, good for rest-day mornings. Watch for kokanee spawning in September — red fish in shallow water is a classic Okanagan sight.</p>

<h2>6. Myra Canyon trestles</h2>
<p>Bike the old Kettle Valley Railway over 18 restored wooden trestles. 24 km round trip, mostly flat. Rent bikes at the trailhead. Half-day activity, spectacular photography.</p>

<h2>7. Big White (winter) or Apex (spring skiing)</h2>
<p>If you're here Dec–Apr, Big White is your mountain — 55 min from downtown Kelowna.</p>

<h2>8. Downtown Kelowna waterfront walk</h2>
<p>Stuart Park, Waterfront Park, Kerry Park, all connected by a walkway. Free, pretty, about 45 min end to end. Good morning option.</p>

<h2>9. Eat at a patio on the water</h2>
<p>Hotel Eldorado's patio, Bouchons, Rotten Grape, BNA Brewing. Kelowna does summer patios properly.</p>

<h2>10. Sleep at Dennis's Stay+Fish Airbnb</h2>
<p>If you're combining fishing with the trip, book Dennis's <a href="/stay-fish.html">Kelowna Airbnb</a> — one host for your stay AND your charter means zero trip-logistics friction.</p>

<hr/>
<h2>A one-day itinerary</h2>
<ol><li>6:30 am — meet the boat at Cook Road for a half-day charter</li><li>11:00 am — dock, shower at the Airbnb</li><li>12:30 pm — lunch at a lake-view patio</li><li>3:00 pm — winery #1 (drive out from Kelowna)</li><li>5:00 pm — Knox Mountain sunset hike</li><li>8:00 pm — dinner downtown</li></ol>
<p>Book the charter first — everything else is flexible.</p>
</div>
</div></section>''' + cta_band("Start with a fishing charter")
PAGES.append(("/things-to-do-kelowna.html", page(
    "Things to Do in Kelowna — Local's 10 Picks | Outdoor Adventures BC",
    "A Kelowna local's pick-list of the 10 best things to do on your visit — from lake fishing to wineries, Knox Mountain to the farmers' market.",
    "/things-to-do-kelowna.html", things_body)))

# ========= NEW GUIDES =========
def guide_page(slug, title, h1, lede, content):
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{h1}","author":{{"@type":"Person","name":"Dennis Barnes"}},"datePublished":"2026-04-22","publisher":{{"@type":"Organization","name":"Outdoor Adventures BC"}}}}</script>'
    body = f'''<section class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/guides/">Guides</a> › {h1}</nav>
<span class="eyebrow">Kelowna local guide</span>
<h1>{h1}</h1>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{lede}</p>
{content}
<hr/>
<p><strong>Skip the research — just book.</strong> <a href="/contact.html">Book a Kelowna fishing charter →</a></p>
</div></div></section>'''
    return page(title, lede, f"/guides/{slug}.html", body, schema)

PAGES.append(("/guides/what-to-wear-kelowna-fishing.html", guide_page(
    "what-to-wear-kelowna-fishing",
    "What to Wear on a Kelowna Fishing Charter — Complete Guide",
    "What to wear on a Kelowna fishing charter",
    "The simple layered-clothing guide for Okanagan Lake fishing — by season, for first-timers.",
    """<h2>The rule</h2>
<p>It's always 10°C cooler on the water than in downtown Kelowna. Dress for the water, not the town.</p>
<h2>Base layer</h2>
<p>Moisture-wicking T-shirt or long-sleeve. Not cotton. Sweat evaporates off cotton and chills you.</p>
<h2>Mid layer</h2>
<p>A fleece or light down jacket. You'll probably take it off by 10 am in July — keep it in your bag.</p>
<h2>Outer / windproof</h2>
<p>A windbreaker or light rain shell. Even in July, the wind across Okanagan Lake at 20 km/h drops perceived temperature fast.</p>
<h2>Bottoms</h2>
<p>Long pants, not shorts — sun reflection off water will cook your legs in 2 hours. Quick-dry hiking pants are ideal.</p>
<h2>Footwear</h2>
<p><strong>Closed-toe non-marking soles only.</strong> Boat shoes, light hikers, or running shoes. No black rubber soles — they mark the deck and we won't thank you.</p>
<h2>Accessories</h2>
<ul><li>Polarized sunglasses — required, not optional</li><li>Baseball cap or brimmed hat with a chin strap</li><li>Buff / neck gaiter for sun protection</li><li>Sunscreen, at least SPF 30</li><li>Lip balm with SPF</li></ul>
<h2>By season</h2>
<p><strong>June–August:</strong> T-shirt + light shell in the bag. Shorts not recommended unless you like sunburn.<br/>
<strong>April–May / September–October:</strong> Long sleeve + fleece + shell. Bring a beanie.<br/>
<strong>November–March:</strong> Full winter layers. Insulated jacket, gloves, wool hat. Heated cabin is available but deck is cold.</p>""")))

PAGES.append(("/guides/best-kokanee-lures.html", guide_page(
    "best-kokanee-lures",
    "Best Kokanee Lures for Okanagan Lake — Proven Picks",
    "The best kokanee lures for Okanagan Lake",
    "What actually catches kokanee on Okanagan Lake — from a guide who trolls for them 150+ days a year.",
    """<h2>The short answer</h2>
<p>Small hoochies in pink, UV purple, or glow white, behind a 4-inch dodger in silver or chrome, tipped with corn. That setup catches 80% of our kokanee.</p>
<h2>Dodgers</h2>
<p><strong>Mack's Sling Blade 4.0</strong> in silver, chrome, or UV purple. The Sling Blade is the industry standard for kokanee — predictable action, right size for a small trolling leader. Avoid oversized dodgers on Okanagan kokanee; they'll spook fish.</p>
<h2>Hoochies (squids)</h2>
<ul><li>1.5" pink micro-hoochie — best all-around summer kokanee colour</li><li>UV purple — killer in low-light or deeper water</li><li>Glow white — morning bite</li><li>Chartreuse — dirty water or bright sun</li></ul>
<h2>Spoons (when hoochies slow down)</h2>
<p>Needlefish spoons in 50/50 brass + fire stripe. Good for rainbow too — cover more species.</p>
<h2>Bait tipping</h2>
<p>Pautzke Fire Corn on every hook. The smell and the spin are equally important. Replace every fish or every 20 minutes.</p>
<h2>Leaders</h2>
<p>4–6 ft of 12-lb fluorocarbon from dodger to hoochie. Shorter leaders slow the hoochie; longer leaders let it spin freely.</p>
<h2>What not to waste money on</h2>
<ul><li>Giant flashers (too big for Okanagan kokanee)</li><li>Dodgers in clown / rainbow patterns (over-worked)</li><li>Scented gels (the corn already does the job)</li></ul>""")))

PAGES.append(("/guides/okanagan-lake-depth-map.html", guide_page(
    "okanagan-lake-depth-map",
    "Okanagan Lake Depth & Structure — Where the Fish Live",
    "Okanagan Lake depth map & fishing structure",
    "An overview of Okanagan Lake depth, structure and the spots that hold fish — by a working charter captain.",
    """<h2>The basics</h2>
<ul><li><strong>Length:</strong> ~135 km (Vernon to Penticton)</li><li><strong>Maximum depth:</strong> ~232 m (762 ft)</li><li><strong>Average depth:</strong> ~76 m</li><li><strong>Surface area:</strong> 351 km²</li></ul>
<h2>The three basins</h2>
<p>Okanagan Lake has three distinct basins, each with its own fishing personality:</p>
<h3>North basin (Vernon to Fintry)</h3>
<p>Shallower, warmer. Good spring rainbow fishing. Less kokanee.</p>
<h3>Central basin (Kelowna area)</h3>
<p>Deep, wide, productive. Best kokanee water. The stretch from Knox Mountain south to Peachland is our summer home.</p>
<h3>South basin (Peachland to Penticton)</h3>
<p>Deepest (~232 m at the deepest point near Squally Point). Best year-round lake-trout structure.</p>
<h2>Productive structure</h2>
<ul><li>Knox Mountain wall (deep drop right off the north-Kelowna cliff)</li><li>Mission Creek mouth (baitfish)</li><li>Bear Creek inflow (west side)</li><li>Peachland shoal (east-side shelf drop)</li><li>Squally Point (deepest water, trophy lakers)</li></ul>
<h2>Where to look on your fishfinder</h2>
<p>Kokanee: suspended schools over 150–250 ft water. Lake trout: structure-oriented over 80–200 ft. Rainbow: shelves at 20–40 ft.</p>""")))

PAGES.append(("/guides/winter-fishing-kelowna.html", guide_page(
    "winter-fishing-kelowna",
    "Winter Fishing in Kelowna — Year-Round Okanagan Charters",
    "Winter fishing in Kelowna",
    "Okanagan Lake doesn't close in winter. Here's what to expect from a cold-weather Kelowna fishing charter.",
    """<h2>Does Okanagan Lake freeze?</h2>
<p>No. Okanagan Lake is too deep and too long to freeze over — surface ice rarely forms even in the coldest winters. That means fishing is open 12 months a year.</p>
<h2>What bites in winter</h2>
<p><strong>Lake trout.</strong> Winter is arguably the best lake-trout season on Okanagan Lake. Cold water pushes them higher in the column — sometimes 40–80 ft instead of 150 ft — and they feed aggressively.</p>
<h2>What's different</h2>
<ul><li>You have the lake to yourself — crowds are zero</li><li>Heated cabin onboard matters (and we have one)</li><li>Trip length is usually 4–6 hours, not 8 — cold drains energy</li><li>Rate is still $200/hr</li></ul>
<h2>What to wear</h2>
<p>Full winter layering: insulated jacket, wool socks, beanie, gloves, windproof outer. See our <a href="/guides/what-to-wear-kelowna-fishing.html">clothing guide</a>.</p>
<h2>When to book</h2>
<p>We run winter charters Dec–March on request. Morning trips are typical; we launch after the frost burns off and fish the warmest window of the day.</p>""")))

# ========= REVIEWS LANDING =========
reviews_landing_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Kelowna fishing charter reviews</nav>
<div class="section-head reveal"><span class="eyebrow">Guest testimonials</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Kelowna Fishing Charter Reviews</h1><p>What real guests say about a day on the water with Outdoor Adventures BC. 5.0 stars on Google.</p></div>

<div class="reviews-header reveal">
<a class="google-badge" href="https://share.google/oQfowrUI3wFXEOYxG" target="_blank" rel="noopener">
<svg viewBox="0 0 48 48" aria-hidden="true" width="22" height="22"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
<span class="stars">★★★★★</span><span>5.0 on Google</span></a>
</div>

<p style="margin-top:28px"><a href="/reviews.html">See our full review page →</a></p>
</div></section>'''
PAGES.append(("/kelowna-fishing-charter-reviews.html", page(
    "Kelowna Fishing Charter Reviews — 5.0 ★ | Outdoor Adventures BC",
    "Real Kelowna fishing charter reviews for Outdoor Adventures BC. 5.0 stars on Google. Read what guests say about a day on Okanagan Lake with Dennis.",
    "/kelowna-fishing-charter-reviews.html", reviews_landing_body)))

# ========= PRESS PAGE =========
press_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Press</nav>
<div class="section-head reveal"><span class="eyebrow">Media kit</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Press & media</h1><p>Writing about Kelowna, Okanagan Lake, BC fishing, or outdoor tourism? Happy to help — here's everything you'd need.</p></div>

<div class="prose" style="max-width:760px;margin:0 auto">
<h2>Quick business info</h2>
<div class="facts-box"><h3>Facts</h3><dl>
<dt>Company name</dt><dd>Outdoor Adventures BC</dd>
<dt>Owner / Captain</dt><dd>Dennis Barnes</dd>
<dt>Based</dt><dd>Kelowna, British Columbia, Canada</dd>
<dt>Founded</dt><dd>2023</dd>
<dt>Boat</dt><dd>Kingfisher 2525 Weekender (26 ft aluminum cabin)</dd>
<dt>Lakes</dt><dd>Okanagan, Shuswap, Arrow Lakes</dd>
<dt>Species</dt><dd>Kokanee salmon, rainbow trout, lake trout, Gerrard rainbow, bull trout, chinook, burbot</dd>
<dt>Rating</dt><dd>5.0 on Google</dd>
<dt>Phone</dt><dd>250-902-8323</dd>
<dt>Email</dt><dd>info@outdooradventuresbc.ca</dd>
</dl></div>

<h2>Pitches we say yes to</h2>
<ul>
<li>Seasonal "what's biting" columns (spring/summer kickoff stories)</li>
<li>B-roll ride-alongs for local TV or YouTube creators</li>
<li>Destination tourism features on Okanagan Lake</li>
<li>Sustainability / conservation angle on catch-and-release practices</li>
<li>Family-travel / multi-generational trip features</li>
</ul>

<h2>Photos + video</h2>
<p>Hi-res photos of the boat, lakes, catches and captain available on request. Email for a download link.</p>

<h2>Contact for press</h2>
<p>Email <a href="mailto:info@outdooradventuresbc.ca">info@outdooradventuresbc.ca</a> with "Press — [your outlet]" in the subject line. We typically reply within a few hours.</p>
</div></div></section>'''
PAGES.append(("/press.html", page(
    "Press & Media — Outdoor Adventures BC Kelowna",
    "Press inquiries, media kit and B-roll for Outdoor Adventures BC — a Kelowna fishing charter company.",
    "/press.html", press_body)))

# ========= SEARCH PAGE =========
search_body = '''<section class="section" style="padding-top:56px"><div class="container">
<nav class="breadcrumbs"><a href="/">Home</a> › Search</nav>
<div class="section-head"><span class="eyebrow">Find anything</span><h1>Search the site</h1><p>Type to filter — charters, lakes, species, guides, catches.</p></div>

<input id="q" type="search" placeholder="Search…" autofocus style="width:100%;max-width:640px;padding:16px 18px;border:1px solid var(--line);border-radius:12px;font-size:1.1rem;margin-bottom:28px"/>

<ul id="results" style="list-style:none;padding:0;margin:0;max-width:760px;display:grid;gap:12px"></ul>
</div></section>

<script>
const IDX = [
  {t:"Kelowna Fishing Charters",u:"/kelowna-fishing-charters.html",k:"charter fishing kokanee rainbow lake trout half-day full-day"},
  {t:"Okanagan Sightseeing Tours",u:"/sightseeing-tours.html",k:"cruise sunset tour boat sightseeing"},
  {t:"Pricing",u:"/pricing.html",k:"pricing cost price rate half-day full-day sunset $200"},
  {t:"Half-day charter",u:"/charters/half-day-charter.html",k:"half day 4 hour $800"},
  {t:"Full-day charter",u:"/charters/full-day-charter.html",k:"full day 8 hour $1600"},
  {t:"Sunset cruise",u:"/charters/sunset-cruise.html",k:"sunset cruise evening golden hour"},
  {t:"Corporate charter",u:"/charters/corporate-charter.html",k:"corporate team-building business"},
  {t:"Family fishing trip",u:"/charters/family-fishing-trip.html",k:"family kids children kid-friendly"},
  {t:"Bachelor / bachelorette charter",u:"/charters/bachelor-party-charter.html",k:"bachelor bachelorette party stag stagette"},
  {t:"Birthday charter",u:"/charters/birthday-charter.html",k:"birthday milestone celebration"},
  {t:"Proposal cruise",u:"/charters/proposal-cruise.html",k:"proposal engagement romantic"},
  {t:"Anniversary cruise",u:"/charters/anniversary-charter.html",k:"anniversary couple"},
  {t:"Gift certificates",u:"/gift-certificates.html",k:"gift certificate voucher"},
  {t:"Our boat — Kingfisher 2525",u:"/our-boat.html",k:"boat kingfisher 2525 weekender vessel"},
  {t:"Meet Dennis Barnes",u:"/captain.html",k:"captain dennis barnes owner"},
  {t:"Reviews",u:"/reviews.html",k:"reviews testimonials google stars"},
  {t:"FAQ",u:"/faq.html",k:"faq questions answers"},
  {t:"Contact / book",u:"/contact.html",k:"contact book booking email phone"},
  {t:"Refer a friend",u:"/refer.html",k:"referral refer friend $50 $75"},
  {t:"Digital waiver",u:"/waiver.html",k:"waiver liability release sign"},
  {t:"Stay + Fish Airbnb",u:"/stay-fish.html",k:"stay fish airbnb accommodation lodging"},
  {t:"Things to do in Kelowna",u:"/things-to-do-kelowna.html",k:"things to do kelowna visitor guide activities"},
  {t:"Press / media",u:"/press.html",k:"press media journalist"},
  {t:"Okanagan Lake",u:"/lakes/okanagan-lake.html",k:"okanagan lake kokanee rainbow"},
  {t:"Shuswap Lake",u:"/lakes/shuswap-lake.html",k:"shuswap chinook burbot"},
  {t:"Arrow Lakes",u:"/lakes/arrow-lake.html",k:"arrow gerrard bull trout"},
  {t:"Kalamalka Lake",u:"/lakes/kalamalka-lake.html",k:"kalamalka vernon"},
  {t:"Mabel Lake",u:"/lakes/mabel-lake.html",k:"mabel remote"},
  {t:"Species guide",u:"/species/",k:"species fish guide"},
  {t:"Kokanee salmon",u:"/species/kokanee-salmon.html",k:"kokanee salmon"},
  {t:"Rainbow trout",u:"/species/rainbow-trout.html",k:"rainbow trout"},
  {t:"Lake trout",u:"/species/lake-trout.html",k:"lake trout laker"},
  {t:"Gerrard rainbow",u:"/species/gerrard-rainbow.html",k:"gerrard trophy"},
  {t:"Bull trout",u:"/species/bull-trout.html",k:"bull trout"},
  {t:"Chinook & burbot",u:"/species/chinook-burbot.html",k:"chinook burbot shuswap"},
  {t:"West Kelowna",u:"/areas/west-kelowna.html",k:"west kelowna"},
  {t:"Vernon",u:"/areas/vernon.html",k:"vernon north okanagan"},
  {t:"Peachland",u:"/areas/peachland.html",k:"peachland"},
  {t:"Lake Country",u:"/areas/lake-country.html",k:"lake country oyama winfield"},
  {t:"Naramata",u:"/areas/naramata.html",k:"naramata bench"},
  {t:"Summerland",u:"/areas/summerland.html",k:"summerland"},
  {t:"Blog",u:"/blog/",k:"blog guides reports"},
  {t:"Kelowna fishing report",u:"/blog/kelowna-fishing-report.html",k:"fishing report monthly"},
  {t:"Best time to fish Okanagan",u:"/blog/best-time-fish-okanagan-lake.html",k:"best time month season"},
  {t:"Kokanee trolling setup",u:"/blog/kokanee-trolling-setup-guide.html",k:"kokanee trolling setup rigging"},
  {t:"BC fishing licence guide",u:"/blog/kelowna-fishing-licence-guide.html",k:"licence license bc"},
  {t:"What to bring",u:"/blog/what-to-bring-kelowna-charter.html",k:"what to bring packing"},
  {t:"Kids first fishing trip",u:"/blog/first-fishing-trip-kids.html",k:"kids family first fishing"},
  {t:"Guides hub",u:"/guides/",k:"guides local"},
  {t:"Kelowna boat ramps",u:"/guides/kelowna-boat-ramps.html",k:"boat ramp launch"},
  {t:"Where to fish Okanagan",u:"/guides/where-to-fish-okanagan-lake.html",k:"where to fish spots"},
  {t:"Fishing near downtown Kelowna",u:"/guides/fishing-near-downtown-kelowna.html",k:"downtown walk-to-dock"},
  {t:"What to wear",u:"/guides/what-to-wear-kelowna-fishing.html",k:"clothing wear layers"},
  {t:"Best kokanee lures",u:"/guides/best-kokanee-lures.html",k:"lures hoochie dodger"},
  {t:"Okanagan Lake depth map",u:"/guides/okanagan-lake-depth-map.html",k:"depth map structure"},
  {t:"Winter fishing Kelowna",u:"/guides/winter-fishing-kelowna.html",k:"winter cold lake trout"},
  {t:"Recent catches",u:"/catches/",k:"catches catch reports recent"},
];
const q = document.getElementById('q'), R = document.getElementById('results');
function render(items){
  R.innerHTML = items.slice(0,20).map(i => `<li><a href="${i.u}" style="display:block;padding:14px 18px;background:#fff;border:1px solid var(--line);border-radius:10px;color:var(--ink);text-decoration:none"><strong>${i.t}</strong><div style="color:var(--muted);font-size:.85rem;margin-top:2px">${i.u}</div></a></li>`).join('');
}
render(IDX);
q.addEventListener('input', () => {
  const s = q.value.toLowerCase().trim();
  if (!s){ render(IDX); return; }
  const results = IDX.map(i => ({i, score: (i.t.toLowerCase().includes(s)?2:0) + (i.k.includes(s)?1:0)})).filter(r=>r.score>0).sort((a,b)=>b.score-a.score).map(r=>r.i);
  render(results);
});
</script>'''
PAGES.append(("/search.html", page(
    "Search — Outdoor Adventures BC",
    "Search the Outdoor Adventures BC site — charters, species, lakes, guides and catch reports.",
    "/search.html", search_body)))

# ---- WRITE ----
for path, html in PAGES:
    write(path, html)
print(f"\nphase 3: {len(PAGES)} pages")
