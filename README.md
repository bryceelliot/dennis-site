# Outdoor Adventures BC — site

Static multi-page marketing site for **Outdoor Adventures BC**, a Kelowna fishing charter & sightseeing tour company.

## Stack
Plain HTML + CSS + vanilla JS. No build step. Deploys anywhere (Vercel, Netlify, GitHub Pages, S3).

## Pages
- `/` — home, primary SEO target for "Kelowna fishing charters"
- `/kelowna-fishing-charters.html`
- `/sightseeing-tours.html`
- `/our-boat.html`
- `/lakes/okanagan-lake.html`, `/lakes/shuswap-lake.html`, `/lakes/arrow-lake.html`
- `/reviews.html`, `/about.html`, `/faq.html`, `/contact.html`
- `/404.html`

## SEO
- Canonical, OG, Twitter, theme-color on every page
- LocalBusiness, Service, Product, FAQPage, BreadcrumbList, TouristTrip, TouristAttraction schema
- `sitemap.xml`, `robots.txt`, `llms.txt` (GEO)

## Local preview
```
python -m http.server 4280
```

## Deploy
`vercel.json` sets cache-control + security headers. Push to Vercel or `vercel --prod` from this directory.

## Replace before launch
- Captain name & bio in `about.html`
- Real Google reviews (current are sample testimonials — replace when actual Google reviews come in)
- Street address / launch-ramp address if making public
