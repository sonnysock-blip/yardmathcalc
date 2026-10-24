#!/usr/bin/env python3
"""Builds the Yard Math static site into ./site, plus preview.html.
Edit the settings below, then run:  python3 build.py
Calculators live in tools_*.py and guides in guides.py (format: SPEC.md).
"""
import json, os, shutil, html, importlib, sys

# ---------------- SETTINGS (edit these) ----------------
SITE_NAME = "Yard Math"
SITE_URL = "https://yardmathcalc.com"
CONTACT_EMAIL = "hello@yardmathcalc.com"
ADSENSE_ID = ""      # e.g. "ca-pub-1234567890123456" once AdSense approves the site
AMAZON_TAG = ""      # e.g. "yardmath-20" once Amazon Associates approves you; turns supply lists into links
PRODUCT_URL = ""     # link to the printable planner on Etsy or Gumroad; shows a promo box when set
YEAR = 2026
# -------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")
sys.path.insert(0, HERE)

GROUPS = [("Mulch & soil", "mulch-and-soil", "Mulch, topsoil, compost and raised bed soil, in yards and bags."),
          ("Stone & hardscape", "stone-and-hardscape", "Gravel, river rock, paver base, decomposed granite and wall blocks."),
          ("Concrete", "concrete", "Slabs, pads and fence posts, in bags or ready-mix."),
          ("Lawn & garden", "lawn-and-garden", "Sod, grass seed, fertilizer and deck stain.")]

def load(modname, attr):
    try:
        return list(getattr(importlib.import_module(modname), attr))
    except ModuleNotFoundError:
        return []

TOOLS = load("tools_core", "TOOLS") + load("tools_hardscape", "TOOLS") + load("tools_garden", "TOOLS") + load("tools_extra", "TOOLS")
GUIDES = load("guides", "GUIDES")
SLUGS = {t["slug"] for t in TOOLS}
BY_SLUG = {t["slug"]: t for t in TOOLS}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap">')

CSS = r"""
/* Layout: measuring-tape utility. Inputs left, a ruled result card right; stacks on phones. */
:root{
  --bg:#EDEFEA; --surface:#F8F9F6; --ink:#1F261F; --muted:#566157; --line:#CDD3CB;
  --moss:#2E5A37; --moss-ink:#F3F7F1; --ochre:#94681F;
  --f-display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;
  --f-body:"Source Sans 3","Segoe UI",system-ui,sans-serif;
  --f-data:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#131813; --surface:#1B221C; --ink:#E5EAE2; --muted:#9CA79D; --line:#2F3A30;
  --moss:#80BC8D; --moss-ink:#102014; --ochre:#D9AB5B; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#131813; --surface:#1B221C; --ink:#E5EAE2; --muted:#9CA79D; --line:#2F3A30;
  --moss:#80BC8D; --moss-ink:#102014; --ochre:#D9AB5B; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:400 17px/1.6 var(--f-body);margin:0}
a{color:var(--moss)}
:focus-visible{outline:2px solid var(--ochre);outline-offset:2px}
.wrap{max-width:1040px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header.top{border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 24px;padding-block:14px}
.brand{font:700 26px/1 var(--f-display);letter-spacing:.02em;text-transform:uppercase;color:var(--ink);text-decoration:none;display:flex;align-items:center;gap:10px}
.brand i{display:inline-block;width:22px;height:22px;border-radius:4px;background:var(--moss);
  -webkit-mask:linear-gradient(90deg,#000 2px,transparent 2px) 0 0/5px 100%;mask:linear-gradient(90deg,#000 2px,transparent 2px) 0 0/5px 100%}
nav.tools{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:15px}
nav.tools a{color:var(--muted);text-decoration:none}
nav.tools a:hover,nav.tools a[aria-current]{color:var(--ink);text-decoration:underline;text-underline-offset:4px}
h1,h2,h3{font-family:var(--f-display);font-weight:700;line-height:1.08;text-wrap:balance;margin:0}
h1{font-size:clamp(36px,6vw,56px);text-transform:uppercase;letter-spacing:.01em}
h2{font-size:30px;margin-top:8px}
h3{font-size:21px}
.lede{color:var(--muted);max-width:62ch;margin:10px 0 0}
main .wrap{padding-block:32px 56px;display:grid;gap:40px}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:8px}
.crumbs a{color:var(--muted)}
.eyebrow{font:500 12px/1 var(--f-data);letter-spacing:.12em;text-transform:uppercase;color:var(--ochre)}
.prose{max-width:68ch;display:grid;gap:14px}
.prose p,.prose ul,.prose ol{margin:0}
.prose li{margin-bottom:6px}
.prose h2{margin-top:14px}
.prose h3{margin-top:6px}
/* calculator */
.calc{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;align-items:start}
@media (max-width:760px){.calc{grid-template-columns:1fr}}
.inputs{display:grid;gap:18px}
.seg{display:flex;flex-wrap:wrap;border:1px solid var(--line);border-radius:8px;overflow:hidden;width:fit-content;max-width:100%}
.seg input{position:absolute;opacity:0;pointer-events:none}
.seg label{padding:9px 14px;font-size:15px;cursor:pointer;color:var(--muted)}
.seg label+input+label{border-left:1px solid var(--line)}
.seg input:checked+label{background:var(--moss);color:var(--moss-ink)}
.seg input:focus-visible+label{outline:2px solid var(--ochre);outline-offset:-2px}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}
.field{display:grid;gap:6px;align-content:start}
.field label{font-size:14px;font-weight:600}
.unit{display:flex;align-items:center;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
.unit:focus-within{border-color:var(--moss);box-shadow:0 0 0 3px color-mix(in srgb,var(--moss) 25%,transparent)}
.unit input,.unit select{flex:1;min-width:0;border:0;background:transparent;color:var(--ink);font:500 18px var(--f-data);padding:10px 12px;outline:none}
.unit select{font:400 16px var(--f-body);padding-right:8px}
.unit span{padding-right:12px;color:var(--muted);font-size:14px}
.unit span.pre{padding:0 0 0 12px}
.hint{font-size:13px;color:var(--muted);font-weight:400}
.result{background:var(--surface);border:1px solid var(--line);border-radius:10px;overflow:hidden;position:sticky;top:16px}
.tape{height:22px;background:
  repeating-linear-gradient(90deg,var(--ochre) 0 1px,transparent 1px 100%) 0 0/48px 100% no-repeat,
  repeating-linear-gradient(90deg,var(--ink) 0 1px,transparent 1px 48px) 0 0/100% 14px no-repeat,
  repeating-linear-gradient(90deg,var(--muted) 0 1px,transparent 1px 12px) 0 0/100% 7px no-repeat;
  border-bottom:1px solid var(--line);opacity:.8}
.result .body{padding:20px 22px 22px;display:grid;gap:16px}
.big{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.big b{font:700 64px/1 var(--f-display);color:var(--moss);font-variant-numeric:tabular-nums}
.big span{font:600 20px var(--f-display);text-transform:uppercase;letter-spacing:.04em}
.lines{display:grid;margin:0}
.lines div{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-top:1px dashed var(--line)}
.lines dt{color:var(--muted);font-size:15px}
.lines dd{margin:0;font:500 16px var(--f-data);font-variant-numeric:tabular-nums;text-align:right}
.callout{margin:0;font-size:15px;padding:10px 12px;border-radius:8px;background:color-mix(in srgb,var(--moss) 12%,transparent)}
.note{font-size:13px;color:var(--muted);margin:0}
table{border-collapse:collapse;width:100%;font-size:15px}
.tbl{overflow-x:auto}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font:500 12px var(--f-data);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
td.num{font-family:var(--f-data);font-variant-numeric:tabular-nums}
details{border-top:1px solid var(--line);padding:12px 0}
details:last-child{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:600}
details p{margin:8px 0 0;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px}
.card{display:grid;gap:6px;align-content:start;padding:18px;border:1px solid var(--line);border-radius:10px;background:var(--surface);text-decoration:none;color:var(--ink)}
.card:hover{border-color:var(--moss)}
.card .eyebrow{color:var(--moss)}
.card p{margin:0;color:var(--muted);font-size:15px}
.group{display:grid;gap:14px}
.group-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:6px 16px}
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px}
@media (max-width:760px){.split{grid-template-columns:1fr}}
.supplies ul{margin:0;padding-left:20px}
.disclose{font-size:13px;color:var(--muted);margin:0}
.promo{display:grid;gap:8px;padding:18px;border:1px dashed var(--ochre);border-radius:10px}
.promo p{margin:0}
.linklist{margin:0;padding-left:20px}
article.prose table{font-size:15px}
footer{border-top:1px solid var(--line);font-size:14px;color:var(--muted)}
footer .wrap{display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between;padding-block:20px}
footer a{color:var(--muted)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

ENGINE = r"""
const h={f:(n,d)=>isFinite(n)?n.toLocaleString("en-US",{minimumFractionDigits:d,maximumFractionDigits:d}):"0",
         c:n=>isFinite(n)&&n>0?Math.ceil(n-1e-9).toLocaleString("en-US"):"0"};
document.querySelectorAll(".calc[data-kind]").forEach(root=>{
 const k=root.dataset.kind,fn=R[k],o=s=>root.querySelector('[data-o="'+s+'"]');
 const shape=()=>{const r=root.querySelector('input[name="'+k+'-shape"]:checked');return r?r.value:"rect"};
 function run(){
  const v={};
  root.querySelectorAll("input[data-f],select[data-f]").forEach(el=>{const n=parseFloat(el.value);v[el.dataset.f]=isFinite(n)&&n>0?n:0});
  if(root.dataset.area){
   const s=shape();root.querySelectorAll("[data-shape]").forEach(el=>{el.hidden=el.dataset.shape!==s});
   let a=s==="rect"?v.len*v.wid:s==="circle"?Math.PI*Math.pow(v.dia/2,2):v.sqft;
   v.area=a*(1+(v.waste||0)/100);
  }
  let r;try{r=fn(v,h)}catch(e){r={big:["0",""],rows:[]}}
  o("big").textContent=r.big[0];o("unit").textContent=r.big[1]||"";
  o("lines").innerHTML=(r.rows||[]).map(x=>"<div><dt>"+x[0]+"</dt><dd>"+x[1]+"</dd></div>").join("");
  const n=o("note");n.textContent=r.note||"";n.hidden=!r.note;
 }
 root.addEventListener("input",run);root.addEventListener("change",run);run();
});
"""

def esc(s): return html.escape(str(s), quote=True)

def app_js(tools):
    reg = "".join(f'R[{json.dumps(t["kind"])}]=({t["js"].strip()});\n' for t in tools)
    return "(function(){const R={};\n" + reg + ENGINE + "})();\n"

def field_html(k, fd):
    fid = f'{k}-{fd["id"]}'
    opt = fd.get("optional")
    label = esc(fd["label"]) + (' <span class="hint">(optional)</span>' if opt else "")
    hint = f'<span class="hint">{esc(fd["hint"])}</span>' if fd.get("hint") else ""
    if fd.get("type") == "select":
        ops = "".join(f'<option value="{esc(v)}"{" selected" if str(v)==str(fd.get("value")) else ""}>{esc(l)}</option>' for v, l in fd["options"])
        ctl = f'<div class="unit"><select id="{fid}" data-f="{esc(fd["id"])}">{ops}</select></div>'
    else:
        unit = fd.get("unit", "")
        step = fd.get("step", "0.01" if unit == "$" else "any")
        val = f' placeholder="0.00"' if opt else f' value="{esc(fd.get("value", ""))}"'
        inp = f'<input id="{fid}" data-f="{esc(fd["id"])}" type="number" inputmode="decimal" min="0" step="{step}"{val}>'
        ctl = f'<div class="unit"><span class="pre">$</span>{inp}</div>' if unit == "$" else f'<div class="unit">{inp}<span>{esc(unit)}</span></div>'
    return f'<div class="field"><label for="{fid}">{label}</label>{ctl}{hint}</div>'

def calc_html(t):
    k = t["kind"]; parts = []
    if t.get("area"):
        L, W = t.get("dims", (20, 10))
        parts.append(f'''<div class="seg" role="radiogroup" aria-label="Area shape">
        <input type="radio" id="{k}-s1" name="{k}-shape" value="rect" checked><label for="{k}-s1">Rectangle</label>
        <input type="radio" id="{k}-s2" name="{k}-shape" value="circle"><label for="{k}-s2">Circle</label>
        <input type="radio" id="{k}-s3" name="{k}-shape" value="area"><label for="{k}-s3">I know the area</label></div>
      <div class="row" data-shape="rect">{field_html(k, dict(id="len",label="Length",unit="ft",value=L))}{field_html(k, dict(id="wid",label="Width",unit="ft",value=W))}</div>
      <div class="row" data-shape="circle" hidden>{field_html(k, dict(id="dia",label="Diameter",unit="ft",value=10))}</div>
      <div class="row" data-shape="area" hidden>{field_html(k, dict(id="sqft",label="Total area",unit="sq ft",value=200,hint="Add up several areas and enter the total"))}</div>''')
    plain = [f for f in t.get("fields", []) if not f.get("optional")]
    money = [f for f in t.get("fields", []) if f.get("optional")]
    row = "".join(field_html(k, f) for f in plain)
    if t.get("area") and t.get("waste") is not None:
        row += field_html(k, dict(id="waste", label="Extra for waste", unit="%", value=t["waste"]))
    if row: parts.append(f'<div class="row">{row}</div>')
    if money: parts.append(f'<div class="row">{"".join(field_html(k, f) for f in money)}</div>')
    return f'''
  <section class="calc" data-kind="{k}"{' data-area="1"' if t.get("area") else ""} aria-label="{esc(t["name"])}">
    <div class="inputs">{"".join(parts)}</div>
    <div class="result" aria-live="polite">
      <div class="tape" aria-hidden="true"></div>
      <div class="body">
        <span class="eyebrow">You need</span>
        <div class="big"><b data-o="big">0</b><span data-o="unit"></span></div>
        <dl class="lines" data-o="lines"></dl>
        <p class="callout" data-o="note" hidden></p>
        <p class="note">Estimates round up. Check product labels and supplier figures before ordering.</p>
      </div>
    </div>
  </section>'''

def group_slug(name): return dict((g, s) for g, s, _ in GROUPS).get(name, "")

def supplies_html(t):
    items = t.get("supplies") or []
    if not items: return ""
    if AMAZON_TAG:
        from urllib.parse import quote_plus
        lis = "".join(f'<li><a href="https://www.amazon.com/s?k={quote_plus(s)}&amp;tag={esc(AMAZON_TAG)}" rel="sponsored nofollow noopener" target="_blank">{esc(s.capitalize())}</a></li>' for s in items)
        disc = '<p class="disclose">As an Amazon Associate, Yard Math earns from qualifying purchases.</p>'
    else:
        lis = "".join(f"<li>{esc(s.capitalize())}</li>" for s in items); disc = ""
    return f'<section class="prose supplies"><h2>What you\'ll need</h2><ul>{lis}</ul>{disc}</section>'

def promo_html():
    if not PRODUCT_URL: return ""
    return f'''<section class="promo"><span class="eyebrow">Printable</span><h3>Yard Project Planner</h3>
<p>Measuring worksheets, material estimate sheets, coverage charts and a supplier quote table, ready to print.</p>
<p><a href="{esc(PRODUCT_URL)}" target="_blank" rel="noopener">Get the planner</a></p></section>'''

def tool_body(t):
    rows = "".join("<tr>" + "".join(f'<td{" class=num" if i else ""}>{esc(c)}</td>' for i, c in enumerate(r)) + "</tr>" for r in t["table"])
    head = "".join(f"<th>{esc(x)}</th>" for x in t["table_head"])
    faqs = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
    rel = [BY_SLUG[s] for s in t.get("related", []) if s in BY_SLUG and s != t["slug"]]
    rel_cards = "".join(f'<a class="card" href="/{o["slug"]}"><span class="eyebrow">{esc(o["name"])}</span><p>{esc(o["short"])}</p></a>' for o in rel)
    guides = [g for g in GUIDES if t["slug"] in g.get("related", [])]
    guide_list = ("<section class='prose'><h2>Guides</h2><ul class='linklist'>" + "".join(f'<li><a href="/{g["slug"]}">{esc(g["h1"])}</a></li>' for g in guides) + "</ul></section>") if guides else ""
    gs = group_slug(t["group"])
    return f'''
  <div><p class="crumbs"><a href="/">Yard Math</a> / <a href="/{gs}">{esc(t["group"])}</a></p>
  <h1>{esc(t["h1"])}</h1><p class="lede">{esc(t["lede"])}</p></div>
  {calc_html(t)}
  <section class="prose"><h2>{esc(t.get("table_title","Reference"))}</h2>
    <div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></section>
  <section class="prose"><h2>How it's calculated</h2>{t["how"]}</section>
  {supplies_html(t)}
  <section class="prose"><h2>Common questions</h2><div>{faqs}</div></section>
  {guide_list}
  {promo_html()}
  <section class="group"><h2>Related calculators</h2><div class="cards">{rel_cards}</div></section>'''

def guide_body(g):
    rel = [BY_SLUG[s] for s in g.get("related", []) if s in BY_SLUG]
    cards = "".join(f'<a class="card" href="/{o["slug"]}"><span class="eyebrow">{esc(o["name"])}</span><p>{esc(o["short"])}</p></a>' for o in rel)
    return f'''
  <div><p class="crumbs"><a href="/">Yard Math</a> / <a href="/guides">Guides</a></p>
  <h1>{esc(g["h1"])}</h1><p class="lede">{esc(g["lede"])}</p></div>
  <article class="prose">{g["body"]}</article>
  {promo_html()}
  {"<section class='group'><h2>Calculators for this project</h2><div class='cards'>"+cards+"</div></section>" if cards else ""}'''

def group_section(name, slug, blurb, link=True):
    ts = [t for t in TOOLS if t["group"] == name]
    if not ts: return ""
    cards = "".join(f'<a class="card" href="/{t["slug"]}"><span class="eyebrow">{esc(t["name"])}</span><p>{esc(t["short"])}</p></a>' for t in ts)
    head = f'<h2><a href="/{slug}" style="color:inherit;text-decoration:none">{esc(name)}</a></h2>' if link else ""
    return f'<section class="group"><div class="group-head">{head}<span class="hint">{esc(blurb)}</span></div><div class="cards">{cards}</div></section>'

def home_body():
    groups = "".join(group_section(*g) for g in GROUPS)
    gl = "".join(f'<li><a href="/{g["slug"]}">{esc(g["h1"])}</a></li>' for g in GUIDES[:6])
    guides = f'<section class="prose"><h2>Project guides</h2><ul class="linklist">{gl}</ul><p><a href="/guides">All guides</a></p></section>' if GUIDES else ""
    return f'''
  <div><span class="eyebrow">Measure once, buy once</span><h1>Yard material calculators</h1>
  <p class="lede">Free estimates for {len(TOOLS)} yard and garden projects. Enter your measurements and get cubic yards, tons, bags, pallets and costs.</p></div>
  {groups}
  {guides}
  <section class="prose"><h2>Why estimate first</h2>
  <p>Ordering too little means a second trip or a second delivery fee. Ordering too much leaves a pile on the driveway. A two-minute measurement saves both.</p>
  <p>Every calculator shows its formula and the sizes and weights it assumes. The <a href="/methodology">methodology page</a> lists them all in one place.</p></section>'''

def hub_body(name, slug, blurb):
    gs = [g for g in GUIDES if g.get("group") == name]
    gl = f'<section class="prose"><h2>Guides</h2><ul class="linklist">' + "".join(f'<li><a href="/{g["slug"]}">{esc(g["h1"])}</a></li>' for g in gs) + "</ul></section>" if gs else ""
    return f'''<div><p class="crumbs"><a href="/">Yard Math</a></p><h1>{esc(name)} calculators</h1><p class="lede">{esc(blurb)}</p></div>
  {group_section(name, slug, "", link=False)}{gl}'''

def guides_index_body():
    secs = ""
    for name, slug, _ in GROUPS:
        gs = [g for g in GUIDES if g.get("group") == name]
        if gs:
            secs += f'<section class="prose"><h2>{esc(name)}</h2><ul class="linklist">' + "".join(f'<li><a href="/{g["slug"]}">{esc(g["h1"])}</a> <span class="hint">{esc(g["lede"])}</span></li>' for g in gs) + "</ul></section>"
    return f'<div><p class="crumbs"><a href="/">Yard Math</a></p><h1>Project guides</h1><p class="lede">Plain how-to guides with real numbers, each paired with a calculator.</p></div>{secs}'

METHOD = [
 ("Mulch (shredded hardwood)", "Sold by volume", "2 and 3 cu ft bags"),
 ("Topsoil", "about 1.0–1.3 tons per cu yd (we use 1.1)", "0.75 and 1 cu ft bags"),
 ("Gravel and crushed stone", "about 1.3–1.5 tons per cu yd (we use 1.4)", "0.5 cu ft bags"),
 ("Concrete mix", "80 lb bag ≈ 0.60 cu ft; 60 lb ≈ 0.45; 40 lb ≈ 0.30", "Ready-mix sold by the cu yd"),
 ("Sod", "Piece 16 × 24 in ≈ 2.67 sq ft", "Pallet about 400–500 sq ft (we use 450)"),
]

def method_body():
    rows = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>" for a, b, c in METHOD)
    return f'''<div class="prose"><h1>Methodology</h1>
<p>Every calculator turns your measurements into an area in square feet, multiplies by depth for a volume, and converts to the units suppliers sell: cubic yards, tons, bags or pallets.</p>
<p><b>Cubic feet</b> = area (sq ft) × depth (in) ÷ 12. <b>Cubic yards</b> = cubic feet ÷ 27. A circle's area is π × (diameter ÷ 2)².</p>
<p>Bag counts always round up. The "extra for waste" percentage is added to the area before anything else, to cover uneven ground, settling and cuts.</p>
<h2>Standard figures</h2>
<div class="tbl"><table><thead><tr><th>Material</th><th>Figure used</th><th>Sold as</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Each calculator page lists any further assumptions it makes. Weights vary with moisture and particle size, so check your supplier's figure when ordering by the ton.</p>
<h2>Corrections</h2><p>Spotted an error? Email {CONTACT_EMAIL} and we'll fix it.</p></div>'''

STATIC = {
 "about": ("About", "About Yard Math, free calculators for landscaping and home projects.", lambda: f'''<div class="prose"><h1>About</h1>
<p>{SITE_NAME} is a set of free calculators and guides for common yard and home projects. Each tool shows its formula and the standard sizes it assumes, so you can check the result.</p>
<p>The figures are estimates. Product yields, stone density and pallet sizes vary, so confirm quantities with your supplier before you order. See the <a href="/methodology">methodology</a> for the figures we use.</p>
<p>The site is supported by ads and, where noted, affiliate links. That keeps the tools free.</p></div>'''),
 "contact": ("Contact", "Contact Yard Math.", lambda: f'''<div class="prose"><h1>Contact</h1>
<p>Found a mistake or want a new calculator? Email <b>{CONTACT_EMAIL}</b>.</p></div>'''),
 "privacy": ("Privacy Policy", "Privacy policy for Yard Math.", lambda: f'''<div class="prose"><h1>Privacy policy</h1>
<p>Last updated: October {YEAR}.</p>
<p>{SITE_NAME} does not ask for or store personal information. Numbers you type into a calculator stay in your browser and are not sent to us.</p>
<h2>Advertising and cookies</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on those visits.</p>
<p>You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads">Google Ads Settings</a>, or opt out of some third-party vendors' cookies at <a href="https://www.aboutads.info/choices/">aboutads.info</a>. See <a href="https://policies.google.com/technologies/partner-sites">how Google uses data from partner sites</a>.</p>
<p>Visitors in the EEA, UK and Switzerland are shown a consent message, managed through Google's certified consent tools, before personalised ads load.</p>
<h2>Affiliate links</h2><p>Some pages link to products on Amazon. As an Amazon Associate, Yard Math earns from qualifying purchases, at no extra cost to you.</p>
<h2>Analytics</h2><p>We may use privacy-friendly, aggregate traffic statistics to see which calculators are used.</p>
<h2>Contact</h2><p>Questions about this policy: {CONTACT_EMAIL}.</p></div>'''),
 "methodology": ("Methodology", "How Yard Math calculators work: formulas, bag sizes and material weights used in every estimate.", method_body),
}

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#2E5A37"/><path d="M6 8v16M11 8v9M16 8v16M21 8v9M26 8v16" stroke="#F3F7F1" stroke-width="2.5" stroke-linecap="round"/></svg>'

def page(title, desc, path, body, current=None, extra_head=""):
    canon = SITE_URL + path
    ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>' if ADSENSE_ID else "")
    nav = "".join(f'<a href="/{s}"{" aria-current=page" if s==current else ""}>{esc(g)}</a>' for g, s, _ in GROUPS)
    nav += f'<a href="/guides"{" aria-current=page" if current=="guides" else ""}>Guides</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="/style.css">{ads}{extra_head}
</head><body>
<header class="top"><div class="wrap"><a class="brand" href="/"><i></i>{SITE_NAME}</a><nav class="tools" aria-label="Sections">{nav}</nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap"><span>© {YEAR} {SITE_NAME}. Estimates only; confirm with your supplier.</span>
<span><a href="/about">About</a> · <a href="/methodology">Methodology</a> · <a href="/privacy">Privacy</a> · <a href="/contact">Contact</a></span></div></footer>
<script src="/app.js" defer></script></body></html>'''

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj) + "</script>"

def tool_ld(t):
    return ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t["faq"]]}) + \
           ld({"@context":"https://schema.org","@type":"WebApplication","name":t["name"],"url":SITE_URL+"/"+t["slug"],"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}})

def guide_ld(g):
    return ld({"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["desc"],"url":SITE_URL+"/"+g["slug"],
               "author":{"@type":"Organization","name":SITE_NAME},"publisher":{"@type":"Organization","name":SITE_NAME},"dateModified":f"{YEAR}-10-18"})

def check():
    seen = set()
    for t in TOOLS:
        assert t["slug"] not in seen and t["kind"] not in seen, f"duplicate {t['slug']}"
        seen |= {t["slug"], t["kind"]}
        assert t["group"] in [g for g, _, _ in GROUPS], f"bad group in {t['slug']}"
    for g in GUIDES:
        assert g["slug"] not in seen, f"guide slug clash {g['slug']}"; seen.add(g["slug"])
        g["related"] = [s for s in g.get("related", []) if s in SLUGS]

def build_site():
    check()
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    def w(name, s): open(os.path.join(OUT, name), "w").write(s)
    w("style.css", CSS); w("app.js", app_js(TOOLS)); w("favicon.svg", FAVICON)
    w("index.html", page(f"{SITE_NAME}: Yard and Garden Material Calculators",
        "Free calculators for mulch, gravel, topsoil, concrete, sod, pavers, grass seed and more. Get cubic yards, tons, bags and costs instantly.", "/", home_body()))
    urls = ["/"]
    for name, slug, blurb in GROUPS:
        if any(t["group"] == name for t in TOOLS):
            w(slug + ".html", page(f"{name} Calculators · {SITE_NAME}", f"Free {name.lower()} calculators. {blurb}", "/" + slug, hub_body(name, slug, blurb), slug)); urls.append("/" + slug)
    for t in TOOLS:
        w(t["slug"] + ".html", page(t["title"], t["desc"], "/" + t["slug"], tool_body(t), group_slug(t["group"]), tool_ld(t))); urls.append("/" + t["slug"])
    if GUIDES:
        w("guides.html", page(f"Project Guides · {SITE_NAME}", "Plain how-to guides for yard projects: mulching, gravel driveways, paver bases, sod, fence posts, lawn care and more.", "/guides", guides_index_body(), "guides")); urls.append("/guides")
        for g in GUIDES:
            w(g["slug"] + ".html", page(g["title"], g["desc"], "/" + g["slug"], guide_body(g), "guides", guide_ld(g))); urls.append("/" + g["slug"])
    for slug, (title, desc, body) in STATIC.items():
        w(slug + ".html", page(f"{title} · {SITE_NAME}", desc, "/" + slug, body())); urls.append("/" + slug)
    w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"  <url><loc>{SITE_URL}{u}</loc><lastmod>{YEAR}-10-18</lastmod></url>\n" for u in urls) + "</urlset>\n")
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    if ADSENSE_ID:
        w("ads.txt", f"google.com, {ADSENSE_ID.replace('ca-','')}, DIRECT, f08c47fec0942fa0\n")
    w("404.html", page(f"Page not found · {SITE_NAME}", "Page not found.", "/404",
        '<div class="prose"><h1>Page not found</h1><p><a href="/">Back to all calculators</a></p></div>'))
    return urls

def build_preview():
    tabs = "".join(f'<input type="radio" name="tab" id="t-{t["kind"]}"{" checked" if i==0 else ""}><label for="t-{t["kind"]}">{esc(t["name"].replace(" Calculator",""))}</label>' for i, t in enumerate(TOOLS))
    panels = "".join(f'<div class="panel" data-p="{t["kind"]}"><h2>{esc(t["h1"])}</h2><p class="lede" style="margin-bottom:18px">{esc(t["lede"])}</p>{calc_html(t)}</div>' for t in TOOLS)
    sel = "".join(f'#t-{t["kind"]}:checked~.panels [data-p="{t["kind"]}"]{{display:block}}' for t in TOOLS)
    css = CSS + f'''
.tabs{{display:flex;flex-wrap:wrap;gap:6px}} .tabs>input{{position:absolute;opacity:0}}
.tabs>label{{padding:7px 12px;border:1px solid var(--line);border-radius:999px;cursor:pointer;font-size:14px;background:var(--surface)}}
.tabs>input:checked+label{{background:var(--moss);color:var(--moss-ink);border-color:var(--moss)}}
.tabs>input:focus-visible+label{{outline:2px solid var(--ochre)}}
.panels{{flex-basis:100%;margin-top:22px}} .panel{{display:none}} {sel}
.banner{{background:var(--surface);border:1px dashed var(--line);border-radius:8px;padding:10px 14px;font-size:14px;color:var(--muted)}}'''
    return f'''<title>Yard Math</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}<style>{css}</style>
<header class="top"><div class="wrap"><span class="brand"><i></i>{SITE_NAME}</span><span class="hint">Preview of all {len(TOOLS)} calculators</span></div></header>
<main><div class="wrap">
<p class="banner">This preview puts every calculator on one page. The real site gives each one its own page with a reference table, formula, FAQ and guides, plus {len(GUIDES)} project guides.</p>
<div class="tabs">{tabs}<div class="panels">{panels}</div></div>
</div></main>
<script>{app_js(TOOLS)}</script>'''

if __name__ == "__main__":
    urls = build_site()
    open(os.path.join(HERE, "preview.html"), "w").write(build_preview())
    print(f"built {len(urls)} pages: {len(TOOLS)} calculators, {len(GUIDES)} guides")
