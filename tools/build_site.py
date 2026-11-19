"""Builds the static GitHub Pages site for salmazahrapsy.github.io.
Run: python3 build_site.py <output_dir>
Plain HTML + one CSS file. No framework, so a student can maintain it by editing this file or the HTML directly."""
import os, sys, html, datetime

OUT = sys.argv[1]
BASE = "https://salmazahrapsy.github.io"
GH = "https://github.com/salmazahrapsy"
TODAY = datetime.date(2026, 11, 19).isoformat()

NAV = [("/", "Home"), ("/about/", "About"), ("/research/", "Research"),
       ("/projects/", "Projects"), ("/business-behaviour/", "Business & Behaviour"),
       ("/gmp-2027/", "GMP 2027")]

OG = (f'<meta property="og:image" content="{BASE}/assets/og.png">\n<meta name="twitter:card" content="summary_large_image">\n'
      if os.path.exists(os.path.join(OUT, "assets", "og.png")) else "")

def page(path, title, desc, body, extra_head=""):
    canon = BASE + path
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
{OG}<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="/">Salma Zahra</a>
  <nav aria-label="Main">{nav}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <p>Salma Zahra · Psychology, research &amp; human-centred innovation · Indonesia</p>
  <p><a href="{GH}">GitHub</a> · <a href="/about/#contact">Contact</a> · Last updated {TODAY}</p>
  <p class="small">Independent personal portfolio. Not affiliated with or endorsed by any company named on this site.</p>
</footer>
</body>
</html>
"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html") if not path.endswith(".html") else os.path.join(OUT, path.strip("/")), "w") as f:
        f.write(doc)

PERSON_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","name":"Salma Zahra",
 "description":"Psychology undergraduate from Indonesia whose work explores psychology, psychological statistics, research and emerging technology.",
 "url":"https://salmazahrapsy.github.io/","sameAs":["https://github.com/salmazahrapsy"],
 "knowsAbout":["Psychology","Psychological statistics","Human behaviour","Behavioural science","Research methods","Emerging technology"]}
</script>"""

# ---------- Home
page("/", "Salma Zahra | Psychology, Research & Global Business",
     "Salma Zahra is a Psychology undergraduate from Indonesia whose work explores psychology, psychological statistics, research and emerging technology.",
f"""
<section class="hero">
  <p class="eyebrow">Psychology · Research · Data · Independent projects</p>
  <h1>I explore where psychology, evidence and technology meet.</h1>
  <p class="lede">I'm Salma Zahra, a Psychology undergraduate from Indonesia. My work combines psychological thinking, research, statistics and independent projects to understand people and develop better ideas.</p>
  <p class="cta"><a class="button" href="/projects/">See my work</a> <a class="button ghost" href="/business-behaviour/">Read the latest case study</a></p>
</section>

<section aria-labelledby="explore">
  <h2 id="explore">Explore</h2>
  <div class="cards">
    <a class="card" href="/research/"><h3>Research</h3><p>How I work with evidence: questions, sources, methods and limits.</p></a>
    <a class="card" href="/psychstats/"><h3>PsychStats</h3><p>An open project organising psychology and statistics knowledge, with tested data pipelines.</p></a>
    <a class="card" href="/psyweb3/"><h3>PsyWeb3</h3><p>The research and education studio I founded, on human behaviour in online communities. Live site with a free reading list.</p></a>
    <a class="card" href="/business-behaviour/"><h3>Business &amp; Behaviour</h3><p>What 5,400 Indonesian product reviews say about customer disappointment in clothing.</p></a>
  </div>
</section>

<section aria-labelledby="principles">
  <h2 id="principles">How I work</h2>
  <ul class="ticks">
    <li><strong>Evidence first.</strong> I separate what the data shows from my interpretation and from untested ideas.</li>
    <li><strong>Small, honest steps.</strong> I build in short cycles and write down what did not work.</li>
    <li><strong>People, not only numbers.</strong> Psychology is the reason I care about the data in the first place.</li>
  </ul>
</section>
""", PERSON_LD)

# ---------- About
page("/about/", "About Salma Zahra | Psychology undergraduate, Indonesia",
     "About Salma Zahra: Psychology undergraduate from Indonesia, founder of PsyWeb3, builder of PsychStats.",
f"""
<article class="prose">
<h1>About</h1>
<p class="lede">Salma Zahra is a Psychology undergraduate from Indonesia whose work explores psychology, psychological statistics, research and emerging technology.</p>

<h2>In short</h2>
<dl class="facts">
  <dt>Study</dt><dd>Psychology (S.Psi.), Universitas YARSI, Jakarta — first year</dd>
  <dt>Founder</dt><dd><a href="/psyweb3/">PsyWeb3</a>, a research and education studio on behaviour in online communities</dd>
  <dt>Builds</dt><dd><a href="/psychstats/">PsychStats</a>, an open psychology and statistics knowledge project</dd>
  <dt>Interests</dt><dd>Human behaviour, decision-making, statistics, AI and emerging technology, entrepreneurship, global business</dd>
  <dt>Languages</dt><dd>Indonesian; English (advanced)</dd>
</dl>

<h2>Why psychology led me to business</h2>
<p>Psychology taught me to ask why people decide what they decide. The longer I studied it, the more I saw that behaviour depends on the systems around people: the information they get, the groups they belong to, the organisations they work in. Business is where those systems are designed. I want to learn how evidence about people can shape better decisions in organisations that work across many cultures.</p>

<h2>Global perspective</h2>
<p>I am from Indonesia, one of the most diverse countries in the world, and I work in English and Indonesian. I am interested in which insights about people travel across cultures and which do not, and I look for chances to test that with teams from other countries.</p>

<h2 id="contact">Contact</h2>
<p>The best way to reach me is through <a href="{GH}">GitHub</a>. <!-- TODO(Salma): add a professional email or LinkedIn link here if you want them public --></p>
</article>
""", PERSON_LD)

# ---------- Research
page("/research/", "Research | Salma Zahra",
     "Salma Zahra's research interests and methods: psychology, psychological statistics, behaviour in online communities, and evidence-based analysis.",
"""
<article class="prose">
<h1>Research</h1>
<p class="lede">My research questions sit between psychology and the systems people use every day: online communities, digital shopping, and organisations.</p>

<h2>Current questions</h2>
<ul>
  <li><strong>Trust in online communities.</strong> How do people decide whom to trust when members are pseudonymous? Through PsyWeb3 I am building a verified source register on this topic, starting from the ability-benevolence-integrity model of trust (Mayer, Davis &amp; Schoorman, 1995).</li>
  <li><strong>Emotion in customer feedback.</strong> What do negative emotions in online reviews reveal about the gap between what customers expect and what they receive? See the <a href="/business-behaviour/">case study</a>.</li>
  <li><strong>Teaching statistics.</strong> How can psychology students learn statistics through well-structured, open materials? This drives <a href="/psychstats/">PsychStats</a>.</li>
</ul>

<h2>How I label claims</h2>
<table>
  <thead><tr><th scope="col">Label</th><th scope="col">Meaning</th></tr></thead>
  <tbody>
    <tr><td>Evidence</td><td>Directly supported by a cited source or by data I analysed, with the method shown.</td></tr>
    <tr><td>Interpretation</td><td>My reading of the evidence. Others could read it differently.</td></tr>
    <tr><td>Hypothesis</td><td>An idea worth testing. Not yet supported.</td></tr>
  </tbody>
</table>

<h2>Ethics</h2>
<p>My work is educational and non-clinical. I do not give individual psychological advice. Anything involving people uses informed consent and data minimisation, in line with Indonesia's Personal Data Protection Law (Law No. 27 of 2022).</p>

<!-- TODO(Salma): add academic research (course projects, thesis topic) and any publications with DOI once confirmed. -->
</article>
""")

# ---------- Projects
page("/projects/", "Projects | Salma Zahra",
     "Projects by Salma Zahra: PsychStats, PsyWeb3 and an Indonesian e-commerce review case study.",
f"""
<article class="prose">
<h1>Projects</h1>
<table>
 <thead><tr><th scope="col">Project</th><th scope="col">What it is</th><th scope="col">Status</th><th scope="col">Source</th></tr></thead>
 <tbody>
  <tr><td><a href="/psychstats/">PsychStats</a></td><td>Open psychology and statistics knowledge project with tested data pipelines and an assessment generator</td><td>Active</td><td><a href="{GH}/psychstats">GitHub</a></td></tr>
  <tr><td><a href="/psyweb3/">PsyWeb3</a></td><td>Research and education studio on behaviour in online communities</td><td>Early stage · site live</td><td><a href="/psyweb3/">Website</a> · <a href="{GH}/psyweb3">GitHub</a></td></tr>
  <tr><td><a href="/business-behaviour/">Emotion in Indonesian product reviews</a></td><td>Independent analysis of 5,400 labelled reviews</td><td>Published Nov 2026</td><td><a href="{GH}/psychstats">Script in PsychStats</a></td></tr>
 </tbody>
</table>
</article>
""")

# ---------- PsychStats
page("/psychstats/", "PsychStats | Salma Zahra",
     "PsychStats: an open project by Salma Zahra organising psychology and psychological statistics knowledge, with tested data pipelines.",
f"""
<article class="prose">
<h1>PsychStats</h1>
<p class="lede">An open, evidence-informed project that organises knowledge in psychology and psychological statistics, and the code that keeps it reproducible.</p>
<h2>What is in it</h2>
<ul>
  <li><strong>Knowledge pages</strong> on psychology, psychological statistics, psychotherapy and mental health, written to a common template with references.</li>
  <li><strong>Data pipelines</strong> that validate a metadata schema, normalise datasets and record what was changed.</li>
  <li><strong>An assessment generator</strong> that turns content into Moodle XML and Aiken question banks, tagged by Bloom's taxonomy level.</li>
  <li><strong>Automated checks</strong>: a test suite and a GitHub Actions workflow that runs on every change.</li>
</ul>
<h2>Why I built it</h2>
<p>Psychology students learn statistics best with clear, structured material. I also wanted to practise building things the way researchers should: tested, documented and reproducible.</p>
<p><a class="button" href="{GH}/psychstats">View on GitHub</a></p>
<p class="small">Educational content only. It is not a substitute for professional assessment or care.</p>
<!-- TODO(Salma): link the PsychStats Miraheze wiki here once you confirm its URL. -->
</article>
""")

# ---------- Business & Behaviour (case study)
CHART = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chart.svg")).read()
page("/business-behaviour/", "Emotion in Indonesian Product Reviews: What Disappoints Clothing Buyers | Salma Zahra",
     "Independent student analysis of 5,400 Indonesian e-commerce reviews: in clothing, negative emotion centres on fabric, fit, colour and 'not as pictured', not delivery.",
f"""
<article class="prose">
<p class="eyebrow">Independent student analysis · November 2026</p>
<h1>In online clothing, disappointment is about the product, not the delivery</h1>
<p class="lede">I analysed 5,400 Indonesian e-commerce reviews labelled by emotion. In the clothing categories, negative reviews talked about the item not matching its photo, fabric, colour and fit far more than reviews of other products did, and talked about delivery less.</p>

<h2>Question</h2>
<p>What do negative emotions in online reviews say about customer experience, and is clothing different from other categories?</p>

<h2>Data</h2>
<p>PRDECT-ID: 5,400 product reviews from Tokopedia across 29 categories, each labelled with one emotion (happy, love, sadness, fear, anger) and a sentiment, following criteria set by a clinical psychologist. Citation: Sutoyo, R., Achmad, S., Chowanda, A., Andangsari, E. W., &amp; Isa, S. M. (2022). PRDECT-ID: Indonesian product reviews dataset for emotions classification tasks. <em>Data in Brief, 44</em>, 108554. <a href="https://doi.org/10.1016/j.dib.2022.108554">doi:10.1016/j.dib.2022.108554</a>. Dataset: <a href="https://doi.org/10.17632/574v66hf2v.1">Mendeley Data, doi:10.17632/574v66hf2v.1</a>.</p>

<h2>Evidence</h2>
<figure>
{CHART}
<figcaption>Share of negative reviews mentioning each theme: four clothing categories (400 negative reviews) vs the other 25 categories (2,421). Keyword matching on Indonesian text; every difference shown has p &lt; .001 (Fisher's exact test).</figcaption>
</figure>
<table>
 <thead><tr><th scope="col">Finding</th><th scope="col">Result</th></tr></thead>
 <tbody>
  <tr><td>Star ratings follow emotion closely: anger averages 1.26 stars, love 4.96</td><td>Kruskal–Wallis H = 4,502, p &lt; .001</td></tr>
  <tr><td>Cheaper items attract more negative reviews: 57.5% in the cheapest quarter vs 45.5% in the most expensive</td><td>χ²(3) = 43.7, p &lt; .001; Cramér's V = 0.09 (small)</td></tr>
  <tr><td>Clothing negatives mention "not as described / unlike the photo" in 27.8% of cases vs 14.0% elsewhere</td><td>p &lt; .001</td></tr>
  <tr><td>Clothing negatives mention delivery less often: 22.8% vs 31.5%</td><td>p &lt; .001</td></tr>
 </tbody>
</table>

<h2>Interpretation</h2>
<p>For clothing bought online, the main emotional cost is an expectation gap: the customer imagined one fabric, colour or fit and received another. Logistics matter, but less than for electronics or household goods. This fits a basic idea from consumer psychology: satisfaction depends on how experience compares with expectation, so information that sets accurate expectations is part of the product.</p>

<h2>Hypotheses worth testing</h2>
<ul>
  <li>Clear fabric descriptions (weight, feel, breathability) reduce negative-emotion reviews in clothing more than faster delivery does.</li>
  <li>True-colour photos taken in natural light reduce "not as pictured" complaints.</li>
  <li>Fit guidance based on body measurements reduces size complaints and returns.</li>
</ul>

<h2>Limitations</h2>
<ul>
  <li>The dataset was balanced by label when it was built, so percentages describe this sample, not Tokopedia or any retailer.</li>
  <li>Themes come from keyword matching. A manual check of 16 matches found about 12 relevant; some words (such as "besar", big) also appear in other senses.</li>
  <li>The data covers one marketplace and contains no information about any specific brand. Nothing here describes the customers of any named company.</li>
</ul>

<h2>Reproduce it</h2>
<p>The analysis script is in the <a href="{GH}/psychstats">PsychStats repository</a> (<code>analysis/prdect_case_study.py</code>). It runs in under a second on the public dataset with pandas and SciPy.</p>
</article>
""")

# ---------- GMP 2027
page("/gmp-2027/", "Global Management Program 2027 — Salma Zahra",
     "How Salma Zahra is preparing for the Fast Retailing Global Management Program 2027: psychology, research, initiative and a learning roadmap.",
"""
<article class="prose">
<h1>Global Management Program 2027 — Salma Zahra</h1>
<p class="lede">I am applying to the Fast Retailing Global Management Program 2027. This page shows how I am preparing. It is a personal page: the official application is submitted only through Fast Retailing's own portal.</p>

<h2>Why global business</h2>
<p>Psychology studies people in general. Business is where insight about people meets real limits: price, time, supply and culture. A global business adds the hardest question: which insights hold across countries and which must change. That is the question I want to work on.</p>

<h2>Leadership</h2>
<p>I started a voluntary peer tutoring circle for classmates held back by anxiety about English tests, built around small goals and treating mistakes as data. I also founded <a href="/psyweb3/">PsyWeb3</a> and run it in weekly sprints with a written review each week. Leading alone has taught me discipline and honest reviews; it has also shown me what I cannot do without a team, which is why programmes built on multicultural teamwork matter to me.</p>

<h2>Research</h2>
<p>My work separates evidence from interpretation and hypothesis. See <a href="/research/">Research</a> and <a href="/psychstats/">PsychStats</a>.</p>

<h2>Human behaviour × business</h2>
<table>
 <thead><tr><th scope="col">Area</th><th scope="col">Psychology that applies</th></tr></thead>
 <tbody>
  <tr><td>Customer experience</td><td>Satisfaction depends on expectation versus experience; emotion in feedback signals where the gap is.</td></tr>
  <tr><td>Employee motivation</td><td>Self-determination theory: autonomy, competence and relatedness support lasting motivation.</td></tr>
  <tr><td>Organisational behaviour</td><td>Group identity and trust shape cooperation in teams and communities.</td></tr>
  <tr><td>Decision-making</td><td>Known biases (anchoring, confirmation, hindsight) affect managers as much as customers.</td></tr>
  <tr><td>Innovation</td><td>Testing small changes and measuring behaviour beats guessing what people want.</td></tr>
 </tbody>
</table>

<h2>Business case work</h2>
<p><a href="/business-behaviour/">In online clothing, disappointment is about the product, not the delivery</a> — an independent analysis of 5,400 Indonesian product reviews.</p>

<h2>Learning roadmap</h2>
<table>
 <thead><tr><th scope="col">Area</th><th scope="col">What I am doing</th></tr></thead>
 <tbody>
  <tr><td>Retail strategy</td><td>Reading Fast Retailing's integrated reports and results briefings; comparing store and online models.</td></tr>
  <tr><td>Customer behaviour</td><td>Extending the review analysis; observing stores and noting what shoppers do.</td></tr>
  <tr><td>Data analysis</td><td>Reproducible analysis in Python with pandas and SciPy.</td></tr>
  <tr><td>Leadership</td><td>Weekly sprint reviews in PsyWeb3; practising giving and receiving feedback.</td></tr>
  <tr><td>Cross-cultural management</td><td>Studying how global companies adapt one philosophy to local markets, starting with Southeast Asia.</td></tr>
 </tbody>
</table>
<p><a href="/gmp-2027/timeline/">See my preparation timeline</a></p>
</article>
""")

page("/gmp-2027/timeline/", "GMP 2027 Preparation Timeline — Salma Zahra",
     "Salma Zahra's preparation timeline for the Fast Retailing Global Management Program 2027, with a countdown to the 28 February 2027 deadline.",
"""
<article class="prose">
<h1>Preparation timeline</h1>
<p class="countdown" id="countdown" aria-live="polite">Application deadline: 28 February 2027, 08:59 Japan time (06:59 Western Indonesia Time).</p>
<p class="small">The official Fast Retailing application portal is the only way to apply. This page tracks my own preparation.</p>
<table>
 <thead><tr><th scope="col">When</th><th scope="col">Milestone</th></tr></thead>
 <tbody>
  <tr><td>Nov–Dec 2026</td><td>Research the programme and company; publish this portfolio</td></tr>
  <tr><td>Dec 2026</td><td>CV final; first research note from PsyWeb3</td></tr>
  <tr><td>Dec 2026 – Jan 2027</td><td>Motivation statement drafts and feedback</td></tr>
  <tr><td>Dec 2026 – Feb 2027</td><td>Online assessment practice</td></tr>
  <tr><td>Jan – Feb 2027</td><td>Five mock interview rounds</td></tr>
  <tr><td>26 Feb 2027</td><td>Submit the application (two days early)</td></tr>
  <tr><td>Mar – May 2027</td><td>Assessment and interviews, if invited</td></tr>
 </tbody>
</table>
</article>
<script>
(function(){
  var el=document.getElementById('countdown'); if(!el) return;
  var deadline=Date.UTC(2027,1,27,23,59,0); // 08:59 JST = 23:59 UTC on 27 Feb
  var days=Math.ceil((deadline-Date.now())/86400000);
  if(days>0){ el.textContent=days+' days to the application deadline: 28 February 2027, 08:59 Japan time (06:59 Western Indonesia Time).'; }
  else { el.textContent='The GMP 2027 application deadline (28 February 2027, 08:59 Japan time) has passed.'; }
})();
</script>
""")

# ---------- 404
with open(os.path.join(OUT, "404.html"), "w") as f:
    f.write(f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Salma Zahra</title><meta name="robots" content="noindex"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"></head>
<body><main id="main" class="prose"><h1>Page not found</h1><p>That page does not exist. Try the <a href="/">home page</a> or <a href="/projects/">projects</a>.</p></main></body></html>""")

# ---------- sitemap + robots
paths = ["/", "/about/", "/research/", "/projects/", "/psychstats/", "/business-behaviour/", "/gmp-2027/", "/gmp-2027/timeline/"]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in paths:
        f.write(f"  <url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("built", len(paths), "pages")
