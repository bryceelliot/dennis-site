#!/usr/bin/env python3
"""Generate static pages for Outdoor Adventures BC from a template + page data."""
import os, json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def header(rel_root="/"):
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><span>Outdoor Adventures BC</span></a><button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul><li><a class="navlink" href="/kelowna-fishing-charters.html">Charters</a></li><li><a class="navlink" href="/sightseeing-tours.html">Sightseeing</a></li><li><a class="navlink" href="/pricing.html">Pricing</a></li><li><a class="navlink" href="/blog/">Blog</a></li><li><a class="navlink" href="/reviews.html">Reviews</a></li><li><a class="btn btn-primary" href="/contact.html">Book</a></li></ul></div></header>'''

FOOTER = '''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><img src="/assets/img/outdoor-adventures-bc-logo-coloured.png" alt="Outdoor Adventures BC"/><p>Kelowna-based fishing charters and sightseeing tours on Okanagan, Shuswap and Arrow Lakes.</p><p style="margin-top:8px"><a href="tel:+12509028323" style="color:#fff;font-weight:600">250-902-8323</a></p></div><div><h4>Charters</h4><ul><li><a href="/kelowna-fishing-charters.html">Fishing Charters</a></li><li><a href="/charters/half-day-charter.html">Half-day charter</a></li><li><a href="/charters/full-day-charter.html">Full-day charter</a></li><li><a href="/charters/sunset-cruise.html">Sunset cruise</a></li><li><a href="/charters/corporate-charter.html">Corporate charter</a></li><li><a href="/charters/family-fishing-trip.html">Family trips</a></li><li><a href="/gift-certificates.html">Gift certificates</a></li></ul></div><div><h4>Lakes & areas</h4><ul><li><a href="/lakes/okanagan-lake.html">Okanagan Lake</a></li><li><a href="/lakes/shuswap-lake.html">Shuswap Lake</a></li><li><a href="/lakes/arrow-lake.html">Arrow Lakes</a></li><li><a href="/areas/west-kelowna.html">West Kelowna</a></li><li><a href="/areas/vernon.html">Vernon</a></li><li><a href="/areas/peachland.html">Peachland</a></li></ul></div><div><h4>Company</h4><ul><li><a href="/about.html">About</a></li><li><a href="/captain.html">The captain</a></li><li><a href="/reviews.html">Reviews</a></li><li><a href="/faq.html">FAQ</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact.html">Contact</a></li><li><a href="https://www.instagram.com/outdooradventure.bc" rel="noopener">Instagram</a></li></ul></div></div><div class="footer-bottom"><span>© <span data-year></span> Outdoor Adventures BC · Kelowna, BC</span><span><a href="/legal/privacy.html">Privacy</a> · <a href="/legal/terms.html">Terms</a> · <a href="/legal/cancellation-policy.html">Cancellations</a></span></div></div></footer>

<a href="tel:+12509028323" class="fab-call" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.8 12.8 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.8 12.8 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></a>

<!-- Mobile sticky booking bar -->
<div class="sticky-book" aria-hidden="false">
  <div class="sticky-book-inner"><span><strong>$200/hr</strong> · Kelowna charter</span><a href="/contact.html" class="btn btn-primary">Book</a></div>
</div>

<script src="/assets/js/main.js" defer></script>'''


PAGE_TEMPLATE = '''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<meta name="robots" content="index,follow,max-image-preview:large"/>
<meta name="theme-color" content="#0B4F6C"/>
<link rel="canonical" href="https://outdooradventuresbc.ca{url}"/>
<meta property="og:type" content="{og_type}"/>
<meta property="og:title" content="{og_title}"/>
<meta property="og:description" content="{og_description}"/>
<meta property="og:image" content="https://outdooradventuresbc.ca{og_image}"/>
<meta property="og:url" content="https://outdooradventuresbc.ca{url}"/>
<meta name="twitter:card" content="summary_large_image"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap"/>
<link rel="icon" type="image/png" href="/assets/img/outdoor-adventures-bc-logo-coloured.png"/>
<link rel="stylesheet" href="/assets/css/styles.css"/>
<link rel="alternate" type="application/rss+xml" title="Outdoor Adventures BC" href="/rss.xml"/>
{head_schema}
</head>
<body data-page="{slug}">

{header}

<main id="main">
{body}
</main>

{footer}
</body></html>'''


def render_page(meta, body):
    head_schema = meta.get("head_schema", "")
    return PAGE_TEMPLATE.format(
        title=meta["title"],
        description=meta["description"],
        og_type=meta.get("og_type", "article"),
        og_title=meta.get("og_title", meta["title"]),
        og_description=meta.get("og_description", meta["description"]),
        og_image=meta.get("og_image", "/assets/img/okanagan-lake-1024x682.jpg"),
        url=meta["url"],
        slug=meta.get("slug", ""),
        head_schema=head_schema,
        header=header(),
        body=body,
        footer=FOOTER,
    )


# ---------- Hero helper ----------
def hero(eyebrow, h1, lede, bg, min_height="min(65vh,520px)", breadcrumbs=""):
    return f'''<section class="hero" style="--hero-img:url('{bg}'); min-height:{min_height}">
  <div class="container hero-inner">
    {f'<nav class="breadcrumbs" style="color:rgba(255,255,255,.8)">{breadcrumbs}</nav>' if breadcrumbs else ''}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="hero-cta">
      <a class="btn btn-primary btn-lg" href="/contact.html">Book a Charter</a>
      <a class="btn btn-ghost btn-lg" style="color:#fff;border-color:#fff" href="tel:+12509028323">Call 250-902-8323</a>
    </div>
  </div>
</section>'''


def cta_band(title, sub="$200/hr · 7 days a week · up to 6 guests"):
    return f'''<section class="section" style="padding-top:0"><div class="container"><div class="price-band"><div><h2>{title}</h2><p style="opacity:.9;margin:0">{sub}</p></div><div class="cta-col"><a class="btn btn-primary btn-lg" href="/contact.html">Request a Booking</a><a class="btn" style="color:#fff" href="tel:+12509028323">Call 250-902-8323</a></div></div></div></section>'''


# ---------- PAGE DEFINITIONS ----------

PAGES = []

# ----- TRIP TYPE PAGES -----
PAGES.append({
    "meta": {
        "url": "/charters/half-day-charter.html",
        "title": "Half-Day Kelowna Fishing Charter (4 Hours) — $800 | Outdoor Adventures BC",
        "description": "Half-day Kelowna fishing charter: 4 hours on Okanagan Lake for up to 6 guests. $800 total. Kokanee, rainbow and lake trout — gear included.",
        "og_image": "/assets/img/boat6.jpg",
        "slug": "half-day-charter",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"Half-Day Kelowna Fishing Charter","description":"4-hour private guided fishing charter on Okanagan Lake from Kelowna.","image":"https://outdooradventuresbc.ca/assets/img/boat6.jpg","offers":{"@type":"Offer","price":"800.00","priceCurrency":"CAD","availability":"https://schema.org/InStock"}}</script>',
    },
    "body": hero("Charter · 4 hours", "Half-Day Kelowna Fishing Charter", "Four hours on Okanagan Lake — enough to target one species properly, land a few fish, and still be home for lunch.", "/assets/img/boat6.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Charters › Half-day') + '''
<section class="section"><div class="container"><div class="split"><div class="prose">
<span class="eyebrow">Who it's for</span><h2>The sweet spot for first-timers</h2>
<p>A half-day charter is our most booked trip. It's long enough to get out to real fishing water, set lines, land a few fish, and call it a day without kids melting down. It's also the right window for a morning kokanee bite or an evening rainbow troll.</p>
<div class="facts-box"><h3>Trip summary</h3><dl>
<dt>Duration</dt><dd>4 hours on the water</dd>
<dt>Price</dt><dd>$800 CAD total (up to 6 guests)</dd>
<dt>Typical start</dt><dd>6:00 AM (morning) or 4:00 PM (evening)</dd>
<dt>Target</dt><dd>Kokanee salmon, rainbow trout, lake trout</dd>
<dt>Includes</dt><dd>Captain, boat, fuel, rods, reels, tackle, bait, life jackets</dd>
<dt>Bring</dt><dd>BC fishing licence, layers, cooler</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/boat3.jpg" alt="Half-day Kelowna fishing charter" loading="lazy"/></div></div></div></section>
''' + cta_band("Book a half-day charter"),
})

PAGES.append({
    "meta": {
        "url": "/charters/full-day-charter.html",
        "title": "Full-Day Kelowna Fishing Charter (8 Hours) — $1,600 | Outdoor Adventures BC",
        "description": "Full-day Kelowna fishing charter: 8 hours on Okanagan Lake for up to 6 guests. $1,600 total. Target multiple species with a lunch break onboard.",
        "og_image": "/assets/img/boat1.jpg",
        "slug": "full-day-charter",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"Full-Day Kelowna Fishing Charter","description":"8-hour private guided fishing charter on Okanagan Lake from Kelowna.","image":"https://outdooradventuresbc.ca/assets/img/boat1.jpg","offers":{"@type":"Offer","price":"1600.00","priceCurrency":"CAD","availability":"https://schema.org/InStock"}}</script>',
    },
    "body": hero("Charter · 8 hours", "Full-Day Kelowna Fishing Charter", "A full working day on Okanagan Lake — change locations, switch species, and spend real time fishing the best structure.", "/assets/img/boat1.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Charters › Full-day') + '''
<section class="section"><div class="container"><div class="split reverse"><div class="prose">
<span class="eyebrow">Who it's for</span><h2>Serious anglers and milestone trips</h2>
<p>Eight hours lets us fish morning and afternoon bites, move between spots, and target more than one species. This is the trip for serious anglers, corporate days, or milestone occasions where you want the water to yourselves for the day.</p>
<div class="facts-box"><h3>Trip summary</h3><dl>
<dt>Duration</dt><dd>8 hours on the water</dd>
<dt>Price</dt><dd>$1,600 CAD total (up to 6 guests)</dd>
<dt>Typical start</dt><dd>6:00 AM</dd>
<dt>Target</dt><dd>Multi-species — kokanee, rainbow, lake trout</dd>
<dt>Includes</dt><dd>Captain, boat, fuel, rods, reels, tackle, bait, life jackets</dd>
<dt>Add-ons</dt><dd>Lunch + beverage service, fish cleaning, trophy photos</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/boat8.jpg" alt="Full-day Kelowna fishing charter Okanagan Lake" loading="lazy"/></div></div></div></section>
''' + cta_band("Book a full-day charter"),
})

PAGES.append({
    "meta": {
        "url": "/charters/sunset-cruise.html",
        "title": "Okanagan Sunset Cruise from Kelowna — Private Boat | Outdoor Adventures BC",
        "description": "Private Okanagan Lake sunset cruise from Kelowna aboard a 26' Kingfisher. Heated cabin, wine-country coastlines, 2–3 hours on the water.",
        "og_image": "/assets/img/mountain-and-lake-at-sunset-135157.jpg",
        "slug": "sunset-cruise",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"TouristTrip","name":"Okanagan Lake Sunset Cruise","description":"Private captained sunset cruise on Okanagan Lake from Kelowna.","offers":{"@type":"Offer","price":"400.00","priceCurrency":"CAD"}}</script>',
    },
    "body": hero("Tour · 2 hours", "Okanagan Sunset Cruise", "The way the Okanagan is meant to be seen. Two hours of golden light along the cliffs and vineyards — heated cabin onboard if the breeze picks up.", "/assets/img/mountain-and-lake-at-sunset-135157.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Tours › Sunset cruise') + '''
<section class="section"><div class="container"><div class="split"><div class="prose">
<span class="eyebrow">What's on offer</span><h2>Private, quiet, cinematic</h2>
<p>Our sunset cruise is a private charter for your group only. We push off about an hour before sundown, run the shoreline past Bear Creek and Knox Mountain, and drift under a spectacular Okanagan sky. Bring your own wine — we've got the ice, the glasses, and the speakers.</p>
<div class="facts-box"><h3>Details</h3><dl>
<dt>Duration</dt><dd>2 hours (3 hours on request)</dd>
<dt>Price</dt><dd>$400 CAD total</dd>
<dt>Capacity</dt><dd>Up to 6 guests</dd>
<dt>Features</dt><dd>Heated cabin, fridge, full head, Bluetooth audio</dd>
<dt>Great for</dt><dd>Anniversaries, proposals, birthdays, out-of-town visitors</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/mountain-and-lake-at-sunset-135157.jpg" alt="Okanagan Lake sunset cruise" loading="lazy"/></div></div></div></section>
''' + cta_band("Book a sunset cruise", sub="$400 · 2 hours · up to 6 guests"),
})

PAGES.append({
    "meta": {
        "url": "/charters/corporate-charter.html",
        "title": "Corporate Fishing Charters & Team Building — Kelowna BC | Outdoor Adventures BC",
        "description": "Corporate fishing charters and private team-building trips on Okanagan Lake from Kelowna. Group packages, custom catering and fully managed experiences.",
        "og_image": "/assets/img/boat8.jpg",
        "slug": "corporate-charter",
    },
    "body": hero("Private · full-service", "Corporate Fishing Charters", "Team days, client entertaining and executive offsites — run from Kelowna on one of the Okanagan's most comfortable charter boats.", "/assets/img/boat8.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Charters › Corporate') + '''
<section class="section"><div class="container"><div class="split reverse"><div class="prose">
<span class="eyebrow">Built for business</span><h2>Entertaining that actually makes memories</h2>
<p>Forget the boardroom. A private corporate charter puts your clients or team on Okanagan Lake for a day that people actually talk about later. We handle the whole day end-to-end: catering, licences, transport logistics, even trophy photo delivery the next morning.</p>
<ul class="pill-list"><li>Fully catered</li><li>Branded photography</li><li>Multi-boat coordination on request</li><li>Flexible invoicing</li><li>Non-disclosure available</li></ul>
<div class="facts-box"><h3>Options</h3><dl>
<dt>Half-day corporate</dt><dd>$800 per boat + catering</dd>
<dt>Full-day corporate</dt><dd>$1,600 per boat + catering</dd>
<dt>Multi-boat</dt><dd>We coordinate partner vessels for groups of 10–30</dd>
<dt>Extras</dt><dd>Waterfront welcome, branded swag, custom printed photo albums</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/boat1.jpg" alt="Corporate charter Kelowna" loading="lazy"/></div></div></div></section>
''' + cta_band("Plan a corporate charter"),
})

PAGES.append({
    "meta": {
        "url": "/charters/family-fishing-trip.html",
        "title": "Family Fishing Trips Kelowna — Kid-Friendly Charter | Outdoor Adventures BC",
        "description": "Family-friendly Kelowna fishing charters on Okanagan Lake. Heated cabin, full bathroom, kid-sized rods and life jackets. $200/hr, up to 6 guests.",
        "og_image": "/assets/img/boat4.jpg",
        "slug": "family-fishing-trip",
    },
    "body": hero("Kid-friendly", "Family Fishing Trips from Kelowna", "The most comfortable charter boat on Okanagan Lake for families — heated cabin, bathroom onboard, kid-sized gear, and a captain who loves teaching first-timers.", "/assets/img/boat4.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Charters › Family') + '''
<section class="section"><div class="container"><div class="split"><div class="prose">
<span class="eyebrow">Why families love it</span><h2>Designed for kids who've never fished</h2>
<p>Family charters are our favourite trips. The Kingfisher 2525 is set up for comfort — a heated cabin when the wind picks up, a proper bathroom onboard, a fridge stocked with juice boxes, and plenty of safe deck space. We keep sets short, fish lands fast, and every kid leaves with a photo of their first catch.</p>
<div class="facts-box"><h3>What we provide</h3><dl>
<dt>Kid-sized rods</dt><dd>Yes — lightweight setups scaled for small hands</dd>
<dt>Life jackets</dt><dd>Infant through adult sizes onboard</dd>
<dt>Snacks</dt><dd>Fridge, crackers & water always aboard; full lunch on request</dd>
<dt>Licence</dt><dd>Kids under 16 don't need a licence in BC</dd>
<dt>Trip length</dt><dd>3–4 hour half-days are the sweet spot for kids</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/boat4.jpg" alt="Family fishing trip Kelowna" loading="lazy"/></div></div></div></section>
''' + cta_band("Book a family trip"),
})

# ----- AREA PAGES -----
for area in [
    ("west-kelowna", "West Kelowna", "West Kelowna", "West Kelowna fishing charters on Okanagan Lake — just across the bridge. $200/hr private trips with pickup at West Kelowna boat ramps.", "Right across the bridge from Kelowna, West Kelowna has some of Okanagan Lake's most productive kokanee water. We launch from the West Kelowna side regularly — no extra charge, same $200/hr.", "49.8638, -119.5833"),
    ("vernon", "Vernon", "Vernon", "Vernon fishing charters on Okanagan and Kalamalka Lakes. Guided trips with Outdoor Adventures BC — $200/hr, up to 6 guests.", "Vernon sits at the north end of Okanagan Lake, and right beside the spectacular Kalamalka Lake. We run Vernon-based trips on both, with pickup from north Okanagan launches.", "50.2670, -119.2720"),
    ("peachland", "Peachland", "Peachland", "Peachland fishing charters on Okanagan Lake. Guided Kelowna-area charters serving Peachland and the south Okanagan. $200/hr.", "Peachland overlooks some of the clearest, most productive water on Okanagan Lake. We'll meet you at the Peachland launch or pick up in Kelowna — your call.", "49.7700, -119.7300"),
]:
    slug, name, city, desc, body_para, geo = area
    PAGES.append({
        "meta": {
            "url": f"/areas/{slug}.html",
            "title": f"{city} Fishing Charters on Okanagan Lake — Outdoor Adventures BC",
            "description": desc,
            "og_image": "/assets/img/okanagan-lake-1024x682.jpg",
            "slug": slug,
            "head_schema": f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{city} Fishing Charter","provider":{{"@type":"LocalBusiness","name":"Outdoor Adventures BC","telephone":"+1-250-902-8323"}},"areaServed":{{"@type":"City","name":"{city}, BC"}},"offers":{{"@type":"Offer","price":"200.00","priceCurrency":"CAD","priceSpecification":{{"@type":"UnitPriceSpecification","price":"200.00","priceCurrency":"CAD","unitText":"HOUR"}}}}}}</script>',
        },
        "body": hero(f"{city} · Okanagan Lake", f"{city} Fishing Charters", body_para, "/assets/img/okanagan-lake-1024x682.jpg",
            breadcrumbs=f'<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › Areas › {city}') + f'''
<section class="section"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<span class="eyebrow">About {city} charters</span>
<h2>What to expect</h2>
<p>Every charter is private — your group, your captain, your pace. On Okanagan Lake we target kokanee salmon, rainbow trout and lake trout, with tactics adapted to season. {city}-area trips launch from the closest ramp to you; we'll confirm exactly where when you book.</p>
<div class="facts-box"><h3>{city} charter details</h3><dl>
<dt>Rate</dt><dd>$200 CAD / hour, up to 6 guests</dd>
<dt>Duration</dt><dd>4, 6 or 8 hours</dd>
<dt>Species</dt><dd>Kokanee salmon, rainbow trout, lake trout</dd>
<dt>Launch</dt><dd>{city} or Kelowna ramp (whichever suits you)</dd>
<dt>Included</dt><dd>Captain, boat, rods, reels, tackle, bait, life jackets</dd>
</dl></div>
</div></div></section>
''' + cta_band(f"Book a {city} fishing charter"),
    })

# ----- SIMPLE PAGES -----
PAGES.append({
    "meta": {
        "url": "/pricing.html",
        "title": "Kelowna Fishing Charter Pricing — $200/hr | Outdoor Adventures BC",
        "description": "Transparent pricing for Kelowna fishing charters and sightseeing tours. $200 CAD/hour, up to 6 guests, all gear included. Half-day and full-day packages.",
        "og_image": "/assets/img/boat1.jpg",
        "slug": "pricing",
    },
    "body": '''<section class="section" style="padding-top:56px"><div class="container"><nav class="breadcrumbs"><a href="/">Home</a> › Pricing</nav>
<div class="section-head reveal"><span class="eyebrow">Transparent pricing</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Kelowna Fishing Charter Pricing</h1><p>Simple flat rate. No hidden fees. What you see is what you pay.</p></div>

<div class="grid grid-3">
  <div class="card reveal"><div class="card-body"><span class="card-meta">Most booked</span><h3>Half-day</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary);margin:0">$800</p><p style="color:var(--muted);font-size:.9rem">4 hours · up to 6 guests</p><p>Perfect for kokanee mornings and family trips. Gear, bait and tackle included.</p><a class="btn btn-secondary" href="/contact.html">Book half-day</a></div></div>
  <div class="card reveal delay-1"><div class="card-body"><span class="card-meta">Serious anglers</span><h3>Full-day</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary);margin:0">$1,600</p><p style="color:var(--muted);font-size:.9rem">8 hours · up to 6 guests</p><p>Multi-species fishing with lunch break. Target kokanee AM, switch to lake trout PM.</p><a class="btn btn-secondary" href="/contact.html">Book full-day</a></div></div>
  <div class="card reveal delay-2"><div class="card-body"><span class="card-meta">Special occasion</span><h3>Sunset cruise</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary);margin:0">$400</p><p style="color:var(--muted);font-size:.9rem">2 hours · up to 6 guests</p><p>Private Okanagan sunset cruise with heated cabin and Bluetooth audio.</p><a class="btn btn-secondary" href="/contact.html">Book sunset</a></div></div>
</div>

<table class="species-table" style="margin-top:40px">
<thead><tr><th>What's included</th><th>Half-day</th><th>Full-day</th><th>Sunset</th></tr></thead>
<tbody>
<tr><td>Captain & boat</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td>Fuel</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td>Rods, reels, tackle, bait</td><td>✓</td><td>✓</td><td>—</td></tr>
<tr><td>Life jackets (all sizes)</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td>Fish cleaning</td><td>✓</td><td>✓</td><td>—</td></tr>
<tr><td>Lunch / catering</td><td>Add-on</td><td>Add-on</td><td>Add-on</td></tr>
<tr><td>BC fishing licence</td><td>You</td><td>You</td><td>—</td></tr>
</tbody></table>

<div class="facts-box reveal" style="margin-top:40px"><h3>Fine print</h3><dl>
<dt>Deposit</dt><dd>50% at booking to hold your date</dd>
<dt>Balance</dt><dd>Due at launch (cash, card or e-transfer)</dd>
<dt>Cancellations</dt><dd>Full refund 48+ hours out. See <a href="/legal/cancellation-policy.html">full policy</a>.</dd>
<dt>Weather</dt><dd>Free reschedule if we call the day for safety</dd>
<dt>Taxes</dt><dd>5% GST not included</dd>
<dt>Gratuity</dt><dd>Optional, appreciated, 15–20% is standard</dd>
</dl></div>
</div></section>
''' + cta_band("Ready to book?"),
})

PAGES.append({
    "meta": {
        "url": "/gift-certificates.html",
        "title": "Kelowna Fishing Charter Gift Certificates — Outdoor Adventures BC",
        "description": "Give the gift of an Okanagan Lake fishing charter or sunset cruise. Digital gift certificates delivered by email. Redeem anytime within 12 months.",
        "og_image": "/assets/img/mountain-and-lake-at-sunset-135157.jpg",
        "slug": "gift-certificates",
        "og_type": "product",
    },
    "body": '''<section class="section" style="padding-top:56px"><div class="container"><nav class="breadcrumbs"><a href="/">Home</a> › Gift certificates</nav>
<div class="section-head reveal"><span class="eyebrow">Gift certificates</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Give a day on Okanagan Lake</h1><p>A charter, a sunset cruise, or any dollar amount toward a future trip. Delivered by email, printable, and valid for 12 months.</p></div>

<div class="grid grid-3">
  <div class="card reveal"><img src="/assets/img/boat3.jpg" alt="Half-day gift certificate" loading="lazy"/><div class="card-body"><h3>Half-day charter</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary)">$800</p><p>4 hours of guided fishing for up to 6. Great for birthdays and family gifts.</p><a class="btn btn-secondary" href="/contact.html?gift=half-day">Buy gift</a></div></div>
  <div class="card reveal delay-1"><img src="/assets/img/boat1.jpg" alt="Full-day gift certificate" loading="lazy"/><div class="card-body"><h3>Full-day charter</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary)">$1,600</p><p>The big-milestone gift. 8 hours multi-species on Okanagan Lake.</p><a class="btn btn-secondary" href="/contact.html?gift=full-day">Buy gift</a></div></div>
  <div class="card reveal delay-2"><img src="/assets/img/mountain-and-lake-at-sunset-135157.jpg" alt="Sunset cruise gift certificate" loading="lazy"/><div class="card-body"><h3>Sunset cruise</h3><p style="font-family:var(--serif);font-size:2rem;color:var(--primary)">$400</p><p>Two-hour private Okanagan sunset. Anniversary or proposal-perfect.</p><a class="btn btn-secondary" href="/contact.html?gift=sunset">Buy gift</a></div></div>
</div>

<div class="facts-box reveal" style="margin-top:40px;max-width:640px;margin-left:auto;margin-right:auto"><h3>How it works</h3><dl>
<dt>1. Request</dt><dd>Email us with the amount and recipient's name</dd>
<dt>2. Pay</dt><dd>Credit card or e-transfer</dd>
<dt>3. Deliver</dt><dd>We email a printable PDF within 24 hours</dd>
<dt>Validity</dt><dd>12 months from issue date</dd>
<dt>Transferable</dt><dd>Yes</dd>
</dl></div>
</div></section>
''' + cta_band("Request a gift certificate", sub="We'll reply within a few hours"),
})

PAGES.append({
    "meta": {
        "url": "/captain.html",
        "title": "Meet Your Kelowna Fishing Charter Captain — Outdoor Adventures BC",
        "description": "Meet the captain behind Outdoor Adventures BC — a Kelowna-based charter guide who fishes Okanagan, Shuswap and Arrow lakes year-round.",
        "og_image": "/assets/img/boat5.jpg",
        "slug": "captain",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"The Captain — Outdoor Adventures BC","jobTitle":"Charter fishing captain","worksFor":{"@type":"LocalBusiness","name":"Outdoor Adventures BC"},"knowsAbout":["Kokanee salmon","Rainbow trout","Lake trout","Gerrard rainbow","Downrigger trolling","Okanagan Lake","Shuswap Lake","Arrow Lake"]}</script>',
    },
    "body": hero("The captain", "The guy behind the wheel", "Kelowna-based, year-round on the water, and genuinely obsessed with getting you into fish.", "/assets/img/boat5.jpg",
        breadcrumbs='<a href="/" style="color:rgba(255,255,255,.8)">Home</a> › The captain') + '''
<section class="section"><div class="container"><div class="split"><div class="prose">
<span class="eyebrow">About your captain</span><h2>Years on BC water, and still learning</h2>
<p>Outdoor Adventures BC is owner-captained. That means every charter you book, you're getting the same guy — the one who knows exactly which point is holding kokanee this week, which lake to pick when the wind's up, and which hoochie colour is killing it right now.</p>
<p>The goal on every trip is simple: show you a version of the Okanagan you can't see from shore, and put you on fish. Newcomer, experienced angler, family of five — we'll tune the day to you.</p>
<p><em>Want the captain's personal story, photo and certifications added here? Send over the details and we'll publish it right on this page.</em></p>
<div class="facts-box"><h3>Credentials</h3><dl>
<dt>Licensing</dt><dd>Transport Canada ROC-M certified operator</dd>
<dt>Insurance</dt><dd>Fully insured commercial charter operator</dd>
<dt>Home water</dt><dd>Okanagan Lake — fished since childhood</dd>
<dt>Known for</dt><dd>Kokanee trolling, lake trout structure, family patience</dd>
</dl></div></div>
<div class="split-media"><img src="/assets/img/boat5.jpg" alt="Outdoor Adventures BC captain" loading="lazy"/></div></div></div></section>
''' + cta_band("Book with the captain"),
})

# ----- LEGAL -----
PAGES.append({
    "meta": {
        "url": "/legal/privacy.html",
        "title": "Privacy Policy — Outdoor Adventures BC",
        "description": "Privacy policy for Outdoor Adventures BC — how we handle booking information, website analytics and communications.",
        "og_image": "/assets/img/okanagan-lake-1024x682.jpg",
        "slug": "privacy",
    },
    "body": '''<section class="section" style="padding-top:56px"><div class="container"><nav class="breadcrumbs"><a href="/">Home</a> › Privacy</nav>
<div class="prose" style="max-width:760px;margin:0 auto">
<h1>Privacy Policy</h1>
<p><em>Last updated: 2026</em></p>
<p>Outdoor Adventures BC ("we", "our") operates this website and provides fishing charter and sightseeing services from Kelowna, British Columbia. This policy explains what information we collect and how we use it.</p>
<h2>Information we collect</h2>
<ul>
<li><strong>Contact info you give us</strong> — name, email, phone, dates and party size when you submit a booking request.</li>
<li><strong>Website analytics</strong> — anonymous page views and general location (country/region) via Vercel Analytics. We do not use tracking cookies.</li>
<li><strong>Communications</strong> — emails and text messages you send us.</li>
</ul>
<h2>How we use it</h2>
<ul>
<li>To respond to booking enquiries and confirm your trip.</li>
<li>To send you safety and weather updates about your charter.</li>
<li>To improve our website and service quality.</li>
</ul>
<h2>We do not</h2>
<ul>
<li>Sell or rent your information to anyone.</li>
<li>Share data with advertisers.</li>
<li>Store payment card details (payments are handled by e-transfer or third-party processors).</li>
</ul>
<h2>Your rights</h2>
<p>You can request access to, correction of, or deletion of your data any time by emailing <a href="mailto:info@outdooradventuresbc.ca">info@outdooradventuresbc.ca</a>.</p>
<h2>Contact</h2>
<p>Outdoor Adventures BC · Kelowna, BC · 250-902-8323 · info@outdooradventuresbc.ca</p>
</div></div></section>''',
})

PAGES.append({
    "meta": {
        "url": "/legal/terms.html",
        "title": "Terms of Service — Outdoor Adventures BC",
        "description": "Terms of service and charter booking terms for Outdoor Adventures BC, Kelowna BC.",
        "og_image": "/assets/img/okanagan-lake-1024x682.jpg",
        "slug": "terms",
    },
    "body": '''<section class="section" style="padding-top:56px"><div class="container"><nav class="breadcrumbs"><a href="/">Home</a> › Terms</nav>
<div class="prose" style="max-width:760px;margin:0 auto">
<h1>Terms of Service</h1>
<p><em>Last updated: 2026</em></p>

<h2>Booking & payment</h2>
<ul>
<li>A 50% deposit is required at booking to secure your charter date.</li>
<li>Remaining balance is due on the day of departure.</li>
<li>Prices are in Canadian dollars (CAD). 5% GST is added to all charters.</li>
</ul>

<h2>Cancellations</h2>
<p>See our <a href="/legal/cancellation-policy.html">full cancellation policy</a>. In short: free cancellation up to 48 hours before departure.</p>

<h2>Safety & conduct</h2>
<ul>
<li>Captain's decisions regarding safety, weather, and route are final.</li>
<li>Life jackets must be worn at all times per Transport Canada regulations for children under 12, and as instructed by the captain for all guests in rough conditions.</li>
<li>Alcohol: legal drinking consumption is permitted for guests, not the captain. Guests impaired to the point of risk may be returned to shore without refund.</li>
<li>Illegal substances are not permitted onboard.</li>
</ul>

<h2>Fishing regulations</h2>
<p>Anglers 16 and over must hold a valid BC freshwater fishing licence. All fish retained must comply with the current BC Freshwater Fishing Regulations Synopsis.</p>

<h2>Liability</h2>
<p>Charter fishing and boating carry inherent risk. By booking, you acknowledge these risks and release Outdoor Adventures BC from liability for losses not caused by gross negligence. Guests are responsible for their personal belongings.</p>

<h2>Photo & video</h2>
<p>We may photograph your trip for marketing purposes. Tell us at the start of the trip if you'd prefer not to be photographed.</p>
</div></div></section>''',
})

PAGES.append({
    "meta": {
        "url": "/legal/cancellation-policy.html",
        "title": "Cancellation & Weather Policy — Outdoor Adventures BC",
        "description": "Cancellation and rescheduling policy for Outdoor Adventures BC Kelowna fishing charters. Free cancellation 48+ hours out, weather reschedules always free.",
        "og_image": "/assets/img/okanagan-lake-1024x682.jpg",
        "slug": "cancellation-policy",
    },
    "body": '''<section class="section" style="padding-top:56px"><div class="container"><nav class="breadcrumbs"><a href="/">Home</a> › Cancellation policy</nav>
<div class="prose" style="max-width:760px;margin:0 auto">
<h1>Cancellation & Weather Policy</h1>
<p>We want booking with us to feel low-risk. Here's exactly how cancellations work.</p>

<div class="facts-box"><h3>At a glance</h3><dl>
<dt>48+ hours out</dt><dd>Free cancellation, full refund of deposit</dd>
<dt>24–48 hours out</dt><dd>Deposit held as credit toward a future trip (12-month expiry)</dd>
<dt>Under 24 hours</dt><dd>Deposit non-refundable; balance not charged</dd>
<dt>Weather call by us</dt><dd>Free reschedule OR full refund — your choice</dd>
<dt>Weather call by you</dt><dd>Free reschedule if we agree conditions are unsafe; otherwise standard policy</dd>
</dl></div>

<h2>How we make weather calls</h2>
<p>We monitor wind, wave forecast and lightning risk daily. If conditions are going to be unsafe or genuinely miserable, we'll contact you 12–24 hours ahead to reschedule. Your safety and enjoyment matter more than getting the trip off.</p>

<h2>Sick kids, last-minute life stuff</h2>
<p>If something unexpected comes up in the 24-hour window, call us. We're reasonable people running a small business, and we'd rather move your trip than take your money and feel bad about it. Just tell us what's going on.</p>

<h2>How to cancel or reschedule</h2>
<p>Call <a href="tel:+12509028323">250-902-8323</a> or email <a href="mailto:info@outdooradventuresbc.ca">info@outdooradventuresbc.ca</a>.</p>
</div></div></section>''',
})

# ----- BLOG POSTS -----
def blog_article(title, published, lede, content_html, og_image):
    return f'''<article class="section" style="padding-top:56px"><div class="container"><div class="prose" style="max-width:760px;margin:0 auto">
<nav class="breadcrumbs"><a href="/">Home</a> › <a href="/blog/">Blog</a> › {title}</nav>
<h1>{title}</h1>
<p style="color:var(--muted);font-size:.9rem">Published {published} · Outdoor Adventures BC</p>
<p class="lede" style="font-size:1.15rem;color:var(--ink-2)">{lede}</p>
<img src="{og_image}" alt="{title}" style="border-radius:var(--radius);margin:20px 0" loading="lazy"/>
{content_html}
<hr/>
<p><strong>Ready to put this into practice?</strong> <a href="/contact.html">Book a Kelowna fishing charter</a> with Outdoor Adventures BC — we'll rig it all for you.</p>
</div></div></article>'''

PAGES.append({
    "meta": {
        "url": "/blog/kelowna-fishing-report.html",
        "title": "Kelowna Fishing Report — What's Biting This Month | Outdoor Adventures BC",
        "description": "Live Kelowna fishing report for Okanagan Lake. Current species, depths, lures and conditions from a working charter guide. Updated monthly.",
        "og_image": "/assets/img/okanagan-lake-1024x682.jpg",
        "slug": "fishing-report",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Kelowna Fishing Report","author":{"@type":"Organization","name":"Outdoor Adventures BC"},"datePublished":"2026-04-01","dateModified":"2026-04-22","image":"https://outdooradventuresbc.ca/assets/img/okanagan-lake-1024x682.jpg"}</script>',
    },
    "body": blog_article(
        "Kelowna Fishing Report — April 2026",
        "April 2026 (updated weekly)",
        "Here's what's happening on Okanagan, Shuswap and Arrow Lakes right now, straight from the downrigger. We update this page every week during the season.",
        """<h2>Okanagan Lake — this week</h2>
<p><strong>Kokanee:</strong> Starting to show. Fish are suspended 30–60 ft down over 80–120 ft of water. Best trolling speed 1.2–1.6 mph. Pink and UV hoochies behind small dodgers doing most of the damage.</p>
<p><strong>Rainbow trout:</strong> Shallower than the kokanee — 15–30 ft. Bucktails and Apex plugs in rainbow trout patterns. Mornings are dramatically better than afternoons right now.</p>
<p><strong>Lake trout:</strong> Pre-turnover, still tight to bottom in 80–150 ft. Jigging heavy white tubes in the South Arm producing.</p>

<h2>Shuswap — this week</h2>
<p>Water is still cold. Early season — winter burbot jigging is wrapping up, chinook trolling hasn't kicked in. Best arm right now: Salmon Arm.</p>

<h2>Arrow Lakes — this week</h2>
<p>Gerrard rainbow tail end of spawn. If you want a trophy shot, next two weeks are the window. Trolling big plugs near the Lardeau River mouth.</p>

<h2>What we're rigging</h2>
<ul>
<li>12-lb mono leaders on kokanee setups</li>
<li>2-oz downrigger balls, 3-ft leads</li>
<li>Needlefish spoons in 50/50 brass for rainbow</li>
</ul>

<h2>Want this trip?</h2>
<p>Book a Kelowna charter for the next two weeks and we'll put you right on the current bite. Conditions change fast in April — call us the day before and we'll tell you exactly what's firing.</p>""",
        "/assets/img/okanagan-lake-1024x682.jpg"),
})

PAGES.append({
    "meta": {
        "url": "/blog/best-time-fish-okanagan-lake.html",
        "title": "Best Time to Fish Okanagan Lake — Month by Month Guide",
        "description": "A month-by-month guide to fishing Okanagan Lake. What's biting, where, and when — from a Kelowna charter captain who fishes it year-round.",
        "og_image": "/assets/img/mountain-and-lake-at-sunset-135157.jpg",
        "slug": "best-time",
        "head_schema": '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Best Time to Fish Okanagan Lake","author":{"@type":"Organization","name":"Outdoor Adventures BC"},"datePublished":"2026-03-15"}</script>',
    },
    "body": blog_article(
        "Best Time to Fish Okanagan Lake — A Month-by-Month Guide",
        "March 15, 2026 · 7 min read",
        "Okanagan Lake fishes year-round, but every month has its own pattern. Here's how a charter captain who fishes it 200+ days a year thinks about the calendar.",
        """<h2>January – February: Lake trout prime time</h2>
<p>Cold, quiet, and criminally under-rated. Lake trout are high in the water column (40–80 ft) chasing kokanee schools. Jigging tubes and trolling flashers both work. You'll have the lake to yourself.</p>

<h2>March: Transition</h2>
<p>Water starts warming, lakers spread out. Kokanee begin suspending in classic summer patterns. Good month for multi-species days.</p>

<h2>April – May: Kokanee kickoff</h2>
<p>Kokanee bite turns on. Mornings are gold. This is when we start running daily charters again after winter.</p>

<h2>June – July: Peak kokanee</h2>
<p>Prime season. Kokanee are thick, fat, and happy to hit trolled hoochies behind dodgers. Book early — weekends fill up months ahead.</p>

<h2>August: Hot and sharp</h2>
<p>Kokanee still on, but they move deeper (60–100 ft). Early mornings and late evenings are the ticket. Afternoons are for swimming.</p>

<h2>September: Shoulder season gem</h2>
<p>Water cooling, fish moving. Lake trout start coming up the water column again. Last call for easy kokanee. Shuswap chinook season.</p>

<h2>October – November: Lake trout and rainbow</h2>
<p>Kokanee wrapping up. Rainbow bite strong in cooler water. Lake trout feeding aggressively. This is a secret window — locals know.</p>

<h2>December: Winter specialty</h2>
<p>Quieter month. Cold-weather lake trout trips still produce. Sightseeing tours wind down. Gift certificates start selling hard for Christmas.</p>

<h2>My pick if you only come once</h2>
<p>Early June. Fish are eating, weather is stable, and the lake isn't yet crowded. Book your charter by March for early-June dates.</p>""",
        "/assets/img/mountain-and-lake-at-sunset-135157.jpg"),
})

PAGES.append({
    "meta": {
        "url": "/blog/kokanee-trolling-setup-guide.html",
        "title": "Kokanee Trolling Setup Guide — Okanagan Lake Specifics",
        "description": "The downrigger, leader, dodger and hoochie setup we run for Okanagan Lake kokanee salmon. Speeds, depths, colour picks from a working Kelowna charter.",
        "og_image": "/assets/img/boat6.jpg",
        "slug": "kokanee-setup",
    },
    "body": blog_article(
        "Kokanee Trolling Setup Guide — Okanagan Lake Specifics",
        "April 1, 2026 · 9 min read",
        "Kokanee salmon are the kings of Okanagan Lake. Catching them consistently is about rigging small, trolling slow, and trusting the depth finder. Here's the exact setup we run on the Kingfisher.",
        """<h2>The short version</h2>
<p><strong>Downrigger trolling, 1.2–1.6 mph, 30–80 feet deep, small dodger + hoochie combo, 4–6 foot leader, light gear.</strong> Everything else is nuance.</p>

<h2>The rod & reel</h2>
<p>Light action 7'6" trolling rod. Anything heavier and you miss bites. Level-wind reel with 12-lb monofilament as mainline.</p>

<h2>The release</h2>
<p>Scotty downrigger with a pinch-pad release, set loose. Kokanee have soft mouths — you want the rod to load up slowly as they eat, not yank the hook through them.</p>

<h2>The business end</h2>
<ul>
<li><strong>Dodger:</strong> 4-inch Mack's Sling Blade or similar in silver, UV purple, or chrome. This is the attractor — it's the flash that pulls fish in.</li>
<li><strong>Leader:</strong> 4–6 feet of 12-lb fluorocarbon tied directly dodger to hoochie. No snubber (too stiff with a light dodger).</li>
<li><strong>Hoochie:</strong> 1.5-inch mini-squid in pink, UV purple, or glow white. Thread a single #6 octopus hook through the top of the skirt.</li>
<li><strong>Bait:</strong> Tip the hook with a tiny piece of Pautzke Fire Corn. This is the secret.</li>
</ul>

<h2>Speed</h2>
<p>1.2–1.6 mph over ground. Below 1.0 is too slow — the dodger quits wobbling. Above 1.8 is too fast — the hoochie spins instead of pulsing.</p>

<h2>Depth</h2>
<p>Let the fish finder do the work. Kokanee school — once you mark them, set your ball 5 ft below the school mark. Adjust as they move.</p>

<h2>The bite</h2>
<p>Rod tip loads up gradually. No dramatic slam. When it's loaded — take the rod out of the holder, count to three, then reel tight. Kokanee have paper mouths; keep constant pressure, no pumping.</p>

<h2>Where on Okanagan Lake</h2>
<p>Mid-lake basins in 100–200 ft of water. We like the stretch between Knox Mountain and Bear Creek. The South Arm also produces.</p>

<h2>If you want to skip the whole setup</h2>
<p>Book a half-day charter — we'll have the rods rigged, balls set, and fish on before your coffee's cold.</p>""",
        "/assets/img/boat6.jpg"),
})

PAGES.append({
    "meta": {
        "url": "/blog/kelowna-fishing-licence-guide.html",
        "title": "BC Fishing Licence — 3-Minute Guide for Kelowna Charters",
        "description": "Short guide to buying a BC freshwater fishing licence online before your Kelowna charter. Costs, types, and who needs one.",
        "og_image": "/assets/img/green-grass-field-and-mountain-1034887.jpg",
        "slug": "bc-licence",
    },
    "body": blog_article(
        "BC Fishing Licence — The 3-Minute Guide",
        "March 20, 2026 · 4 min read",
        "You need a BC freshwater fishing licence to fish on any of our charters. Here's exactly what to buy, where, and how long it takes.",
        """<h2>Who needs one</h2>
<p>Everyone <strong>16 years and older</strong>. Kids under 16 fish for free.</p>

<h2>Where to buy</h2>
<p>Online at the <strong>Province of BC's fishing licence portal</strong>: gov.bc.ca/FreshwaterFishing. Takes about 3 minutes. Print the confirmation or save it to your phone.</p>

<h2>Which licence</h2>
<ul>
<li><strong>1-day licence:</strong> $10 (BC resident) / $20 (non-resident) — for a single charter</li>
<li><strong>8-day licence:</strong> $20 / $50 — if you're here on vacation</li>
<li><strong>Annual licence:</strong> $36 / $80 — if you'll fish more than twice this year</li>
</ul>

<h2>Optional add-ons</h2>
<p>If you plan to keep salmon, you'll also need a <strong>Salmon Conservation Stamp</strong> ($6.42). We'll tell you when it applies based on your target species.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Buying a tidal licence by accident.</strong> Okanagan is freshwater. Make sure you're on the freshwater portal.</li>
<li><strong>Wrong date.</strong> The licence activates on the start date you choose. Pick your charter day.</li>
<li><strong>Forgetting to print it.</strong> Conservation officers do check. Save a screenshot at minimum.</li>
</ul>

<h2>Having trouble?</h2>
<p>Give us a call — we've walked dozens of first-time visitors through it. <a href="tel:+12509028323">250-902-8323</a>.</p>""",
        "/assets/img/green-grass-field-and-mountain-1034887.jpg"),
})

PAGES.append({
    "meta": {
        "url": "/blog/what-to-bring-kelowna-charter.html",
        "title": "What to Bring on a Kelowna Fishing Charter — Packing Checklist",
        "description": "The short packing list for a Kelowna fishing charter on Okanagan Lake. What to bring, what to skip, what we already have onboard.",
        "og_image": "/assets/img/boat3.jpg",
        "slug": "what-to-bring",
    },
    "body": blog_article(
        "What to Bring on a Kelowna Fishing Charter",
        "March 10, 2026 · 3 min read",
        "First-time charter guests over-pack every single time. Here's the actual list — short, specific, and based on 20 years of watching people load boats.",
        """<h2>Must bring</h2>
<ul>
<li><strong>BC fishing licence</strong> (on your phone is fine)</li>
<li><strong>Polarized sunglasses</strong> — sunset on Okanagan Lake is brutal without them</li>
<li><strong>Hat</strong> with a strap or brim, preferably secured</li>
<li><strong>Sunscreen</strong> — the water reflection doubles what hits your face</li>
<li><strong>Layers</strong> — it's 10°C cooler on the water than in town</li>
<li><strong>Water</strong> — a couple bottles per person</li>
</ul>

<h2>Good to bring</h2>
<ul>
<li>Windbreaker or light rain shell (even in July)</li>
<li>Phone + charger — there's USB onboard</li>
<li>Camera — some fish deserve a proper photo</li>
<li>Cooler (for the fish you'll take home)</li>
<li>Cash for tip, if you're into that</li>
</ul>

<h2>Don't bring</h2>
<ul>
<li><strong>Hard-shell suitcases</strong> — use a soft duffel</li>
<li><strong>Bananas</strong> — no, seriously, we're not taking chances</li>
<li><strong>Rods</strong> — we have everything. Bringing your own is fine, but not needed.</li>
<li><strong>Dress shoes</strong> — closed-toe, non-marking soles only</li>
</ul>

<h2>Already on the boat</h2>
<ul>
<li>Rods, reels, lures, bait, tackle</li>
<li>Life jackets in every size including infant</li>
<li>Heated cabin</li>
<li>Full head (bathroom)</li>
<li>Fridge</li>
<li>Coffee for morning trips</li>
<li>Snacks and water</li>
<li>Bluetooth speaker</li>
</ul>""",
        "/assets/img/boat3.jpg"),
})

PAGES.append({
    "meta": {
        "url": "/blog/first-fishing-trip-kids.html",
        "title": "Kid's First Fishing Trip in Kelowna — A Parent's Guide",
        "description": "How to set up a Kelowna fishing charter that kids actually love. Trip length, timing, gear and tips from a guide who runs dozens of family trips a season.",
        "og_image": "/assets/img/boat4.jpg",
        "slug": "kids-first-trip",
    },
    "body": blog_article(
        "A Kid's First Fishing Trip — How to Set It Up Right",
        "April 8, 2026 · 6 min read",
        "The difference between a kid who hates fishing forever and a kid who asks to go again is almost always the setup of the first trip. Here's how to get it right.",
        """<h2>Keep it short</h2>
<p>Three to four hours is the sweet spot for kids under 10. Go longer and the fun curve starts pointing down. Half-day charters exist for exactly this reason.</p>

<h2>Morning trips are better</h2>
<p>Kids are fresher. Fish are often more active. You're back in time for lunch and a nap.</p>

<h2>Manage expectations</h2>
<p>Fishing isn't always action-packed. Tell the kid in advance: "We'll see some beautiful water, maybe see some eagles, and hopefully catch some fish." Not "We'll definitely catch lots!" — the Okanagan has bad days.</p>

<h2>Snacks. More than you think.</h2>
<p>A well-fed kid is a patient kid. Pack twice what you'd bring. The fridge is onboard.</p>

<h2>Let them do the work</h2>
<p>Once a fish is on, hand the rod to the kid. Don't hijack their fight. Even if it takes 10 minutes and the hook pulls — they land it (or lose it) themselves.</p>

<h2>The photo matters</h2>
<p>Get a proper photo of the kid with their first fish. Held right, smiling, fish in focus. It's a picture they'll look at for 30 years.</p>

<h2>What the boat brings</h2>
<p>Our Kingfisher is genuinely set up for families — heated cabin if they get cold, real bathroom, enclosed deck space. On our charters, kids under 16 don't need a licence.</p>

<h2>When to go bigger</h2>
<p>Once the kid's 12+ and has done a half-day or two, consider a full-day trip. That's when we'll target lake trout and switch species mid-day.</p>""",
        "/assets/img/boat4.jpg"),
})


# ---------- WRITE ALL PAGES ----------
def write_page(meta, body):
    out = ROOT / meta["url"].lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    html = render_page(meta, body)
    out.write_text(html, encoding="utf-8")
    print(f"  -> {meta['url']}")


print("Generating pages...")
for p in PAGES:
    write_page(p["meta"], p["body"])
print(f"Done. {len(PAGES)} pages written.")
