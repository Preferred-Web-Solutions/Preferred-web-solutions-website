#!/usr/bin/env python3
"""Builds the PWS company site (plain HTML/CSS/JS, no server-side step) from page definitions.
Run from anywhere:  python3 _build/build.py
Output goes to the repo root so GitHub Pages can serve it. The _build folder is ignored by Pages."""
import json, os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://preferredwebsolutionsllc.com"
CTA = "Get a free sample site today"
EMAIL = "preferredwebsolutions@gmail.com"
PHONE_DISPLAY = "(502) 702-1752"
PHONE_TEL = "+15027021752"
UPDATED = "2026-11-05"
SAMPLES = "https://preferred-web-solutions.github.io/restaurant-samples"

NAV = [("samples.html", "Samples"), ("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("about.html", "About"), ("contact.html", "Contact")]

LEGAL_OLD = json.load(open(os.path.join(ROOT, "_build", "legal_old.json")))


def head(title, desc, path, extra=""):
    url = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{H.escape(title)}</title><meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{url}">
<link rel="icon" type="image/png" href="logo.png"><link rel="preload" href="fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="styles.css">{extra}
</head><body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(path):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        links += f'<a href="{href}"{cur}>{label}</a>'
    return f"""<header class="site-header"><div class="wrap bar"><a class="brand" href="index.html"><img src="logo.png" alt="" width="36" height="36">Preferred Web Solutions</a>
<button type="button" class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Main">{links}<a class="btn btn--yellow btn--sm" href="contact.html">{CTA}</a></nav></div></header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html"><img src="logo.png" alt="" width="36" height="36">Preferred Web Solutions</a>
<p>Custom websites for restaurants and contractors. Built for your business, no templates, owned by you.</p>
<a class="btn btn--yellow btn--sm foot-cta" href="contact.html">{CTA}</a></div>
<div><h2>Pages</h2><ul><li><a href="index.html">Home</a></li><li><a href="samples.html">Samples</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h2>Contact</h2><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="contact.html">Cincinnati, Ohio, and other cities</a></li></ul></div>
<div><h2>Legal</h2><ul><li><a href="privacy.html">Privacy policy</a></li><li><a href="terms.html">Terms and conditions</a></li><li><a href="cookies.html">Cookie policy</a></li><li><a href="accessibility.html">Accessibility statement</a></li><li><a href="report.html">Report an issue</a></li><li><button type="button" data-cookie-settings>Cookie settings</button></li></ul></div>
</div>
<p class="legal-note">&copy; 2026 Preferred Web Solutions LLC. The sample sites shown here are for fictional businesses. Photos in the samples are for demonstration only.</p>
</div></footer>
<div class="callbar"><a class="btn btn--yellow" href="contact.html">{CTA}</a></div>
<script src="consent.js"></script><script src="site.js"></script><script src="forms.js"></script>
</body></html>
"""


def page(path, title, desc, body, extra_head=""):
    out = head(title, desc, path, extra_head) + header(path) + body + footer()
    with open(os.path.join(ROOT, path), "w") as f:
        f.write(out)


def frame(src, alt, label, w=1000, h=625, eager=False, href=None):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    img = f'<img src="{src}" width="{w}" height="{h}" {load} alt="{H.escape(alt)}">'
    inner = f'<div class="frame"><div class="frame-bar" aria-hidden="true"><i></i><i></i><i></i><span>{H.escape(label)}</span></div>{img}</div>'
    if href:
        return f'<a class="frame-link" href="{href}" target="_blank" rel="noopener" aria-label="Open the {H.escape(label.split(" | ")[0])} sample site (opens in a new tab)">{inner}</a>'
    return inner


S_DINER = dict(
    slug="diner", name="Hollis Street Diner", img="samples/diner.jpg",
    alt="Sample restaurant website for Hollis Street Diner, showing a first screen with a breakfast plate photo, the diner name in bold red type and an order button",
    kind="Neighborhood diner",
    blurb="Breakfast all day, a photo menu set like the counter menu, weekday specials and a pie pre-order form. Built to feel loud, warm and fast.",
    points=["Menu set as real text, readable at a glance", "Weekday specials up front", "Pie pre-order form"],
)
S_ASH = dict(
    slug="ashgrove", name="Ashgrove", img="samples/ashgrove.jpg",
    alt="Sample restaurant website for Ashgrove, showing a dark first screen with the restaurant name in italic type beside a photo of a plated dish",
    kind="Upscale tasting-menu restaurant",
    blurb="A dark, quiet first screen, a five-course tasting card, the room and cellar, and a private dining request. Built to feel like an evening out.",
    points=["Five-course tasting card", "The room and the cellar", "Private dining request"],
)
S_ZAF = dict(
    slug="zafiro", name="Cantina Zafiro", img="samples/zafiro.jpg",
    alt="Sample restaurant website for Cantina Zafiro, showing a full-width photo of tacos al pastor with the cantina name in bold magenta and marigold type",
    kind="Mexican cantina",
    blurb="A full-screen taco photo, a lotería-card menu, drinks, and catering and party requests. Built to feel like a Friday night.",
    points=["Lotería-card menu", "Drinks and happy hour", "Catering and party requests"],
)


def sample_url(s):
    return f"{SAMPLES}/{s['slug']}/"


# ---------------------------------------------------------------- home
def build_home():
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "Preferred Web Solutions", "url": SITE + "/", "email": EMAIL,
        "areaServed": "Cincinnati, Ohio, and other cities",
        "description": "Custom websites for restaurants and contractors.",
    })
    body = f"""
<section class="hero dark" aria-labelledby="h1"><div class="wrap hero-grid">
<div>
<span class="eyebrow" style="color:var(--yellow)">Websites for restaurants and contractors</span>
<h1 id="h1"><span>Built for your business.</span><span>No templates.</span><span class="y">Owned by you.</span></h1>
<p class="lede">Preferred Web Solutions designs and builds custom websites for restaurants and contractors, starting in the Cincinnati area. Each site is designed around your business, and we keep it running after launch.</p>
<div class="actions"><a class="btn btn--yellow" href="contact.html">{CTA}</a><a class="btn" href="samples.html">See sample sites</a></div>
<ul class="facts"><li>Custom design for your trade</li><li>You own your site</li><li>Free sample first</li><li>Cincinnati and other cities</li></ul>
</div>
<figure class="hero-shot" style="margin:0">
{frame(S_DINER['img'], S_DINER['alt'], 'Hollis Street Diner | sample site', eager=True)}
<figcaption>A sample site for a fictional diner. <a href="{sample_url(S_DINER)}" target="_blank" rel="noopener">Open it and click around<span class="sr"> (opens in a new tab)</span></a></figcaption>
</figure>
</div></section>

<section class="sec" aria-labelledby="why-h"><div class="wrap why-grid">
<div><span class="eyebrow">Why not a template</span><h2 id="why-h">A template makes every business look the same.</h2>
<div class="copy"><p>If customers cannot find you online, they call someone they can. Plenty of good local businesses still have no website at all.</p><p>Many of the ones that do use a template or an AI builder. The layout is the same as every other business on it, and the owner has little say in how it looks.</p><p>We start by learning your trade, your style, and what you want customers to do. Then we build your site around that.</p></div></div>
<div class="compare" role="group" aria-label="A template compared with a site built for your business">
<div><h3>A template</h3><ul><li>The same layout as other businesses<small>You pick from presets.</small></li><li>Look decided for you<small>Little say in how it turns out.</small></li><li>You manage it yourself<small>Problems are yours to solve.</small></li></ul></div>
<div><h3>Built for your business</h3><ul><li>Designed for your trade<small>Restaurants and contractors each get what they need.</small></li><li>You say how it looks<small>Your colors, photos and words.</small></li><li>We keep it running<small>Maintenance and problems are covered.</small></li></ul></div>
</div></div></section>

<section class="sec sec--soft" aria-labelledby="work-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Sample work</span><h2 id="work-h">See a site built for your kind of business.</h2><p>These are full sample sites for made-up restaurants. Open one and click around. Each is built around its own business, not copied from the others.</p></div>
<div class="shots">
<div class="main"><figure class="shot" style="margin:0">{frame(S_DINER['img'], S_DINER['alt'], 'Hollis Street Diner | sample site', href=sample_url(S_DINER))}<figcaption><span class="tag">Fictional sample</span><b>{S_DINER['name']}</b><span>{S_DINER['kind']}. {S_DINER['blurb']}</span></figcaption></figure>
<div class="shots-note"><b>More on the way.</b><span>Contractor sample sites are being built now.</span><a class="link-arrow" href="samples.html">See all sample sites &rarr;</a></div></div>
<div class="stack">
<figure class="shot" style="margin:0">{frame(S_ASH['img'], S_ASH['alt'], 'Ashgrove | sample site', href=sample_url(S_ASH))}<figcaption><span class="tag">Fictional sample</span><b>{S_ASH['name']}</b><span>{S_ASH['kind']}</span></figcaption></figure>
<figure class="shot" style="margin:0">{frame(S_ZAF['img'], S_ZAF['alt'], 'Cantina Zafiro | sample site', href=sample_url(S_ZAF))}<figcaption><span class="tag">Fictional sample</span><b>{S_ZAF['name']}</b><span>{S_ZAF['kind']}</span></figcaption></figure>
</div></div>
</div></section>

<section class="sec sec--dark dark" aria-labelledby="who-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow" style="color:var(--yellow)">Who we build for</span><h2 id="who-h">Two kinds of business. Two different kinds of site.</h2><p>A restaurant site and a contractor site have different jobs, so they are not built the same way.</p></div>
<div class="split">
<div class="panel"><h3>Restaurants</h3><p>A site that makes people hungry and makes it easy to order, reserve or ask about catering.</p><ul><li>Your menu as real text, with photos</li><li>Hours, location and a clear call or order button</li><li>Catering and party requests</li></ul></div>
<div class="panel"><h3>Contractors</h3><p>A site that shows your work and turns a visit into a call or a quote request.</p><ul><li>One page for each main service</li><li>Photos of finished jobs and your service area</li><li>A quote request and a call button on every page</li></ul><p class="note">Contractor sample sites are being built now.</p></div>
</div></div></section>

<section class="sec" aria-labelledby="steps-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">How it works</span><h2 id="steps-h">From first call to launch in four steps.</h2></div>
<ol class="steps">
<li><h3>See a free sample</h3><p>Tell us about your business and we show you what your site could look like.</p></li>
<li><h3>Tell us your style</h3><p>Answer a short questionnaire about your colors, your photos and what you want your site to do.</p></li>
<li><h3>Review and launch</h3><p>We meet to go through the draft, make changes, and launch when you are happy.</p></li>
<li><h3>We keep it up</h3><p>Maintenance and a check-in every 3 to 6 months keep your site current.</p></li>
</ol>
<p class="arrow-row"><a class="link-arrow" href="how-it-works.html">How it works &rarr;</a><a class="link-arrow" href="pricing.html">See pricing &rarr;</a></p>
</div></section>

<section class="sec sec--soft" aria-labelledby="where-h"><div class="wrap where">
<div><span class="eyebrow">Where we work</span><h2 id="where-h">Based in Cincinnati. Not limited to it.</h2><p>We work with businesses across the Cincinnati area, and with businesses in other cities too. Your site is built online, and we go through the draft with you by phone or video.</p></div>
<ul class="place-list"><li>Cincinnati area<span>In person or online</span></li><li>Other cities<span>Online, by phone or video</span></li></ul>
</div></section>

<section class="sec sec--yellow band" aria-labelledby="cta-h"><div class="wrap">
<h2 id="cta-h">See what your site could look like.</h2>
<p>Tell us about your business and we will show you a sample site for it. It is free.</p>
<a class="btn btn--ink" href="contact.html">{CTA}</a>
</div></section>
"""
    page("index.html",
         "Custom websites for restaurants and contractors in Cincinnati | Preferred Web Solutions",
         "Preferred Web Solutions builds custom websites for restaurants and contractors in the Cincinnati area and other cities. No templates, and you own your site.",
         body, f'<script type="application/ld+json">{jsonld}</script>')


# ---------------------------------------------------------------- samples
def build_samples():
    ents = ""
    for s in (S_DINER, S_ASH, S_ZAF):
        pts = "".join(f"<li>{p}</li>" for p in s["points"])
        ents += f"""<div class="entry"><div class="entry-media">{frame(s['img'], s['alt'], s['name'] + ' | sample site', href=sample_url(s))}</div>
<div><span class="tag">Fictional sample</span><h2>{s['name']}</h2><p><b>{s['kind']}.</b> {s['blurb']}</p><ul>{pts}</ul>
<a class="link-arrow" href="{sample_url(s)}" target="_blank" rel="noopener">Open the full {s['name']} sample site<span class="sr"> (opens in a new tab)</span> &rarr;</a></div></div>
"""
    body = f"""
<div class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Samples</span></nav>
<h1>Sample sites for restaurants and contractors</h1>
<p>Same process, a different site for every business. Open any sample and click around.</p></div></div>
<section class="sec" aria-label="Restaurant samples"><div class="wrap">
{ents}
<div class="coming"><span class="tag">In progress</span><h2>Contractor sample sites</h2><p>We are building sample sites for contractors now: a service page for each trade, a quote request, a service area and photos of finished jobs. If you are a contractor, ask for a sample made for your trade.</p></div>
<p class="disclaimer">The restaurants shown are fictional and the sites are design samples, not live businesses. Photos are for demonstration only. Your site becomes the next example here, with your permission.</p>
<p style="margin-top:2rem"><a class="btn btn--yellow" href="contact.html">{CTA}</a></p>
</div></section>
"""
    page("samples.html", "Sample websites for restaurants and contractors | Preferred Web Solutions",
         "Open full sample websites for a diner, an upscale restaurant and a Mexican cantina from Preferred Web Solutions in Cincinnati. Contractor samples are in progress.", body)


# ---------------------------------------------------------------- how it works
def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)


def build_how():
    faqs = [
        ("What do I need to give you?", "Your answers to our short questionnaire, plus photos, your menu or service details, hours, and contact information. We handle the design and the build."),
        ("Who owns my website?", "You do. You can still ask us to make edits, and we keep it maintained."),
        ("What if something breaks or I want a change?", f'Email us at {EMAIL} or use the <a href="report.html">report form</a>. Maintenance is part of your monthly fee, and we also talk through updates at your regular check-ins.'),
        ("Will my site look like everyone else&rsquo;s?", "No. We design each site around your trade, your style, and your wishes. We do not use templates."),
        ("Do I have to be technical?", "No. You tell us what you want and we build it."),
        ("Which businesses do you work with?", "Restaurants and contractors, starting in the Cincinnati area. We also work with businesses in other cities, since your site is built online. Something else? Send a note and we will tell you if we can help."),
    ]
    body = f"""
<div class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">How it works</span></nav>
<h1>How it works</h1>
<p>A free sample first, so you can see your site before you commit to anything. Then four simple steps to launch.</p></div></div>

<section class="sec" aria-labelledby="steps-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">The process</span><h2 id="steps-h">Four steps from first call to launch.</h2></div>
<ol class="steps">
<li><h3>See a free sample</h3><p>Tell us about your business and we show you what your site could look like, before you commit to anything.</p></li>
<li><h3>Tell us your style</h3><p>You fill out a short questionnaire about your colors, your photos and what you want your site to do.</p></li>
<li><h3>Review and launch</h3><p>We build your site from your answers and meet to go through the draft. We make changes and launch when you are happy.</p></li>
<li><h3>We keep it up</h3><p>Maintenance is covered by your monthly fee, with a check-in every 3 to 6 months to look at how the site is doing and plan updates.</p></li>
</ol>
<p class="arrow-row"><a class="link-arrow" href="pricing.html">See pricing &rarr;</a></p>
</div></section>

<section class="sec sec--soft" aria-labelledby="faq-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Questions</span><h2 id="faq-h">What owners usually ask.</h2></div>
<div class="faq">{faq_html(faqs)}</div>
</div></section>

<section class="sec sec--yellow band" aria-labelledby="cta-h"><div class="wrap"><h2 id="cta-h">Ready to see yours?</h2><p>Tell us about your business and we will show you a sample site for it.</p><a class="btn btn--ink" href="contact.html">{CTA}</a></div></section>
"""
    page("how-it-works.html", "How it works: from free sample to launch | Preferred Web Solutions",
         "How Preferred Web Solutions builds a custom website for your restaurant or contracting business in four steps, starting with a free sample site.", body)


# ---------------------------------------------------------------- pricing
def build_pricing():
    faqs = [
        ("Is the sample site really free?", "Yes. We show you a sample before you commit to anything. You only pay if you decide to go ahead."),
        ("When do I pay each fee?", "The build fee is paid once you sign the service agreement, before we start building. The go-live fee and your first monthly payment are due when you approve the finished site and are ready to launch."),
        ("What does the monthly fee cover?", f'Keeping your site maintained, handling problems when they come up, and a check-in every 3 to 6 months to look at how the site is doing. If something breaks, email {EMAIL} and we reply within one business day.'),
        ("What does a founding client agree to?", "Founding pricing is for our first five clients. In return, you give us a short written testimonial and let us show your site as an example of our work."),
        ("Is there a written agreement?", "Yes. Every client signs a service agreement that sets out what is included, the fees and how payments work, before any work starts."),
    ]
    body = f"""
<div class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Pricing</span></nav>
<h1>Pricing</h1>
<p>A one-time build fee, a go-live fee, and a monthly fee for maintenance and check-ins. The sample site is free.</p></div></div>

<section class="sec" aria-labelledby="pricing-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Plans</span><h2 id="pricing-h">Simple prices. A discount for our first five clients.</h2></div>
<div class="plans">
<article class="plan plan--feature dark" aria-labelledby="pl1"><div><span class="eyebrow" style="color:var(--yellow)">First 5 clients</span><h3 id="pl1">Founding client</h3></div>
<dl class="led"><div><dt>Build</dt><dd>$150</dd></div><div><dt>Go live</dt><dd>$100</dd></div><div><dt>Monthly</dt><dd>$50 <small>/ month</small></dd></div></dl>
<p class="total"><span>Total to launch</span><b>$250</b></p>
<ul><li>A custom 5-page site designed for your business</li><li>Maintenance and issue handling</li><li>A check-in every 3 to 6 months</li><li>In return: a written testimonial and permission to use your site as an example</li></ul>
<a class="btn btn--yellow" href="contact.html">{CTA}</a></article>
<article class="plan" aria-labelledby="pl2"><div><span class="eyebrow">After the first 5</span><h3 id="pl2">Standard</h3></div>
<dl class="led"><div><dt>Build</dt><dd>$250</dd></div><div><dt>Go live</dt><dd>$250</dd></div><div><dt>Monthly</dt><dd>$100 <small>/ month</small></dd></div></dl>
<p class="total"><span>Total to launch</span><b>$500</b></p>
<ul><li>A custom 5-page site designed for your business</li><li>Maintenance and issue handling</li><li>A check-in every 3 to 6 months</li></ul>
<a class="btn btn--ink" href="contact.html">{CTA}</a></article>
</div>
<p class="refer"><b>Refer a business</b><span>Get $25 off one monthly invoice for each referral that signs up, applied in the month their site goes live.</span></p>
<p class="fine">Prices are for the current offer. Full details are set out in a written service agreement. <a href="how-it-works.html">See how it works</a>.</p>
</div></section>

<section class="sec sec--soft" aria-labelledby="faq-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Questions</span><h2 id="faq-h">Questions about pricing.</h2></div>
<div class="faq">{faq_html(faqs)}</div>
</div></section>

<section class="sec sec--yellow band" aria-labelledby="cta-h"><div class="wrap"><h2 id="cta-h">See your site before you pay anything.</h2><p>Tell us about your business and we will show you a sample site for it.</p><a class="btn btn--ink" href="contact.html">{CTA}</a></div></section>
"""
    page("pricing.html", "Website pricing for restaurants and contractors | Preferred Web Solutions",
         "Clear website pricing from Preferred Web Solutions: founding clients pay $150 to build, $100 to go live and $50 a month. Standard is $250, $250 and $100 a month.", body)


# ---------------------------------------------------------------- about
def build_about():
    body = f"""
<div class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">About</span></nav>
<h1>About Preferred Web Solutions</h1>
<p>A Cincinnati company that builds custom websites for restaurants and contractors.</p></div></div>
<section class="sec" aria-labelledby="why-h"><div class="wrap">
<div class="prose">
<h2 id="why-h">Why we started</h2>
<p>Plenty of good local businesses have no website, or have one that looks like everyone else&rsquo;s. Customers who cannot find you online call someone they can.</p>
<p>Preferred Web Solutions exists to fix that. We design each site around the business behind it: its trade, its style and what the owner wants customers to do. You have a say in how it looks, and you own the result.</p>
<p>We also stay after launch. We maintain your site, deal with problems when they come up, and sit down with you every 3 to 6 months to look at how it is doing.</p>
</div>
<div class="owner"><h3>Meet the owner</h3>
<p>I&rsquo;m Steven Embry, the owner of Preferred Web Solutions. I live in the Cincinnati area, and I started this company because so many good local restaurants and contractors either have no website or have one that looks like every other business on the same builder.</p>
<p>I build each site myself, and I&rsquo;m the person you deal with from the first conversation to every check-in after launch. No hand-offs and no call center. If something on your site needs fixing, you email me and I reply within one business day.</p>
<p>My goal is simple: give you a site that is made for your business, that you own, and that helps customers find you and reach you.</p>
</div>
<!-- PHOTO_SLOT: owner photo goes here when provided -->
</div></section>
<section class="sec sec--soft" aria-labelledby="how-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow">How we work</span><h2 id="how-h">Three things we promise.</h2></div>
<ul class="principles">
<li><b>Built for your business</b><span>Every site starts from your trade, your colors, your photos and your words, not from a preset.</span></li>
<li><b>No templates</b><span>We do not reuse another business&rsquo;s layout. A diner, a fine-dining room and a roofer each get a site that fits them.</span></li>
<li><b>Owned by you</b><span>The site is yours. You can still ask us to make edits, and we keep it maintained.</span></li>
</ul>
<p style="margin-top:2rem"><a class="btn btn--yellow" href="contact.html">{CTA}</a></p>
</div></section>
"""
    page("about.html", "About Preferred Web Solutions | Custom websites in Cincinnati",
         "Preferred Web Solutions is a Cincinnati company that builds custom websites for restaurants and contractors. No templates, and you own your site.", body)


# ---------------------------------------------------------------- contact
def build_contact():
    body = f"""
<div class="page-head"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Contact</span></nav>
<h1>{CTA}</h1>
<p>Tell us a little about your business and we will reach out with a sample site made for it.</p></div></div>
<section class="sec" aria-label="Contact"><div class="wrap contact-grid">
<div><h2 style="font-size:1.6rem">Reach us directly</h2>
<ul class="contact-list">
<li><b>Email</b><div class="mail-row"><a href="mailto:{EMAIL}">{EMAIL}</a><button type="button" class="btn btn--sm" data-copy="{EMAIL}">Copy email</button></div></li>
<li><b>Where we work</b><span>Cincinnati, Ohio, and other cities</span></li>
</ul></div>
<div>
<form class="card" data-formspree="https://formspree.io/f/xgavryzg" data-done="sent" novalidate>
<input type="hidden" name="form" value="PWS website inquiry">
<div class="f-row"><div class="f"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
<div class="f"><label for="c-biz">Business name</label><input id="c-biz" name="business" type="text" autocomplete="organization" required></div></div>
<div class="f-row"><div class="f"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
<div class="f"><label for="c-phone">Phone <span class="opt">(optional)</span></label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div></div>
<div class="f-row"><div class="f"><label for="c-type">Type of business</label><select id="c-type" name="type"><option>Restaurant</option><option>Contractor</option><option>Something else</option></select></div>
<div class="f"><label for="c-city">City <span class="opt">(optional)</span></label><input id="c-city" name="city" type="text" autocomplete="address-level2"></div></div>
<div class="f"><label for="c-msg">Anything we should know? <span class="opt">(optional)</span></label><textarea id="c-msg" name="message"></textarea></div>
<button class="btn btn--yellow" type="submit" style="justify-self:start">{CTA}</button>
<p class="status" role="status" aria-live="polite"></p>
<p class="note">We use your details only to reply to you. See our <a href="privacy.html">privacy policy</a>.</p>
</form>
<div class="done-card" id="sent" hidden role="status"><h3>Thanks, we got your message.</h3><p>We will reply to the email or phone number you gave us.</p></div>
</div></div></section>
"""
    page("contact.html", "Get a free sample website for your business | Preferred Web Solutions",
         "Ask Preferred Web Solutions for a free sample website for your restaurant or contracting business in Cincinnati or another city.", body)


# ---------------------------------------------------------------- legal
def legal_page(path, title, desc, inner):
    body = inner
    page(path, title, desc, body)


def build_legal():
    meta = {
        "privacy": ("Privacy policy | Preferred Web Solutions", "How Preferred Web Solutions handles the information you send through this website."),
        "terms": ("Terms and conditions | Preferred Web Solutions", "The terms for using the Preferred Web Solutions website."),
        "cookies": ("Cookie policy | Preferred Web Solutions", "Exactly what the Preferred Web Solutions website stores on your device."),
        "report": ("Report an issue | Preferred Web Solutions", "Report a problem with the Preferred Web Solutions website."),
    }
    fixes = {
        "privacy": [
            ("designs and maintains websites for local restaurants, with contractor websites coming soon.", "designs and maintains websites for restaurants and contractors."),
            ("type of business, and any message you write", "type of business, city if you add one, and any message you write"),
            ("Version 1.0 &middot; Last updated October 6, 2026", "Version 1.1 &middot; Last updated November 5, 2026"),
        ],
        "terms": [
            ("The restaurant sites shown here are samples for fictional businesses.", "The sample sites shown here are for fictional businesses."),
            ("Version 1.0 &middot; Last updated October 6, 2026", "Version 1.1 &middot; Last updated November 5, 2026"),
        ],
    }
    for k, (t, d) in meta.items():
        inner = LEGAL_OLD[k]
        for a, r in fixes.get(k, []):
            assert a in inner, (k, a)
            inner = inner.replace(a, r)
        legal_page(f"{k}.html", t, d, inner)
    acc = f"""<article class="legal"><a class="back" href="index.html">&larr; Back to home</a>
<h1>Accessibility statement</h1>
<p class="meta">Version 1.0 &middot; Last updated November 5, 2026</p>
<p>We want everyone to be able to use this website. We build it with accessibility in mind and aim for WCAG 2.1 level AA. We cannot promise it is perfect, and we do not claim full compliance.</p>
<h2>What we do</h2>
<ul><li>Every page has one main heading, headings in order, and landmarks for the header, navigation, main content and footer.</li><li>You can use the whole site with a keyboard. A skip link jumps past the menu, and the focus outline is always visible.</li><li>Text is real text, not pictures of text, and meets contrast guidelines. The page works when zoomed to 200 percent.</li><li>Images that carry meaning have descriptive text. Decorative images are hidden from screen readers.</li><li>Form fields have labels, and messages after sending are announced to screen readers.</li><li>Nothing plays sound or moves on its own, and animations respect your device&rsquo;s reduce-motion setting.</li><li>Buttons and links are at least 44 pixels tall on phones.</li></ul>
<h2>How we check</h2>
<p>Before each update we run an automated accessibility checker (axe) on every page and test with a keyboard. Automated tools find only part of the problems, so we also fix what people report to us.</p>
<h2>Known limits</h2>
<p>The sample sites linked from this website are separate design samples for fictional businesses. They are being updated to the same standard.</p>
<h2>Tell us about a problem</h2>
<p>If something on this site is hard to use, please <a href="report.html">report an issue</a> or email {EMAIL}. Tell us the page and what went wrong. We aim to reply within one business day.</p>
</article>
"""
    legal_page("accessibility.html", "Accessibility statement | Preferred Web Solutions",
               "How the Preferred Web Solutions website is built with accessibility in mind, how we check it, and how to report a problem.", acc)


def build_seo_files():
    pages = ["", "samples.html", "how-it-works.html", "pricing.html", "about.html", "contact.html", "privacy.html", "terms.html", "cookies.html", "accessibility.html", "report.html"]
    urls = "".join(f"<url><loc>{SITE}/{p}</loc><lastmod>{UPDATED}</lastmod></url>" for p in pages)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    build_home(); build_samples(); build_how(); build_pricing(); build_about(); build_contact(); build_legal(); build_seo_files()
    print("built")
