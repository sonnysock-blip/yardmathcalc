# Yard Math content spec (for contributors)

Site: yardmathcalc.com, "Yard Math". US homeowners, US units (ft, in, sq ft, cu yd, lb). Static site built by build.py.
Write a Python module that defines a list. No imports except `json` if needed. Plain ASCII-safe UTF-8 strings.

## Calculator tool entry (TOOLS list)
```python
dict(
  slug="paver-base-calculator",          # URL, must end in -calculator
  kind="paverbase",                      # short unique id, letters only
  group="Stone & hardscape",             # one of: "Mulch & soil", "Stone & hardscape", "Concrete", "Lawn & garden"
  name="Paver Base Calculator",          # nav/card name
  short="Gravel base and sand for a paver patio.",   # card line, under 60 chars
  title="Paver Base Calculator: Gravel and Sand Needed",  # <title>, under 60 chars
  desc="...",                            # meta description, 140-160 chars
  h1="Paver base calculator",
  lede="...",                            # one or two sentences
  area=True,                             # True = shared shape picker (rectangle/circle/known area) gives v.area in sq ft
  waste=5,                               # default extra % applied to v.area (only when area=True); None to hide
  fields=[                               # extra inputs, in display order
    dict(id="base", label="Gravel base depth", unit="in", value=4, step=0.5, hint="4 in for patios, 6 in for driveways"),
    dict(id="type", label="Seed type", type="select", value=7, options=[[7,"Tall fescue (7 lb/1,000 sq ft)"],[3,"Kentucky bluegrass (3 lb)"]]),
    dict(id="price", label="Price per ton", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const yd=v.area*v.base/12/27;
      return {big:[h.f(yd,2),"cubic yards of base"], rows:[["Base (tons)",h.f(yd*1.4,2)],["Sand bags (0.5 cu ft)",h.c(v.area*1/12/0.5)]],
              note:"Optional short assumption note." }; }""",
  table_head=["Project","Base depth","Sand"],
  table=[["Walkway","4 in","1 in"], ...],      # 3-6 rows of real reference data
  table_title="Recommended depths",           # H2 above the table
  how="""<p>...</p>""",                       # 120-220 words of HTML: formula with <b> labels, a worked example with real numbers, assumptions
  faq=[("Question?","Answer in 1-3 sentences."), ...],   # exactly 4, real questions people search
  supplies=["plate compactor rental","paver edging","polymeric sand"],  # 3-5 generic product search terms (for affiliate links)
  related=["gravel-calculator","concrete-calculator"],  # 2-4 other tool slugs
)
```
JS rules: `v` holds every field id as a number (0 if blank) plus `v.area` (sq ft, waste already added) when area=True. `h.f(n,d)` formats with d decimals, `h.c(n)` rounds up to a whole number with commas. Return `{big:[text,unit], rows:[[label,text],...], note?}`. If price is entered (>0) add an "Estimated cost" row with "$"+h.f(cost,2). Arrow function only, no external calls, must not throw on zeros (guard division).

## Guide entry (GUIDES list)
```python
dict(slug="how-to-mulch-flower-beds", group="Mulch & soil", title="...", desc="...", h1="...", lede="...",
     body="""<h2>...</h2><p>...</p>...""",   # 700-1,000 words, HTML (h2, h3, p, ul, ol, table allowed)
     related=["mulch-calculator"])
```

## Existing and planned tool slugs (link only to these)
mulch-calculator, gravel-calculator, topsoil-calculator, concrete-calculator, sod-calculator,
paver-base-calculator, retaining-wall-block-calculator, river-rock-calculator, decomposed-granite-calculator, fence-post-concrete-calculator,
raised-bed-soil-calculator, compost-calculator, grass-seed-calculator, fertilizer-calculator, deck-stain-calculator

## Quality bar
- Every number must be accurate and checkable; verify bag sizes, densities, coverage rates and seed rates with web search and say "about" where values vary.
- Original, plain, useful writing. Answer the question in the first sentence. No filler, no "in conclusion", no em-dash asides, no claims of personal experience.
- Never copy text from other sites.
