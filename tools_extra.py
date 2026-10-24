"""Calculators added after launch. Format: SPEC.md."""

TOOLS = [
 dict(
  slug="bags-to-yards-calculator",
  kind="bagstoyards",
  group="Mulch & soil",
  name="Bags to Yards Calculator",
  short="Convert bags of mulch, soil or stone to cubic yards.",
  title="Bags to Cubic Yards Calculator: Mulch, Soil, Stone",
  desc="Free bags to cubic yards calculator. Enter how many bags and the bag size in cubic feet to see cubic yards, and compare bagged cost with a bulk delivery.",
  h1="Bags to cubic yards calculator",
  lede="Enter the number of bags and the size printed on the bag to see how many cubic yards you have, or how much bulk material the same job would take.",
  area=False,
  fields=[
    dict(id="bags", label="Number of bags", value=40, step=1),
    dict(id="size", label="Bag size", type="select", value=2, options=[
      [0.5, "0.5 cu ft (gravel, river rock)"],
      [0.75, "0.75 cu ft (topsoil)"],
      [1, "1 cu ft (garden soil)"],
      [1.5, "1.5 cu ft (garden soil, potting mix)"],
      [2, "2 cu ft (mulch)"],
      [3, "3 cu ft (mulch)"]]),
    dict(id="bag", label="Price per bag", unit="$", optional=True),
    dict(id="bulk", label="Bulk price per cubic yard", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const ft3=v.bags*v.size, yd=ft3/27;
      const rows=[["Cubic feet",h.f(ft3,1)],["Bags in one cubic yard",v.size>0?h.f(27/v.size,1):"0"]];
      if(v.bag>0) rows.push(["Bagged cost","$"+h.f(v.bags*v.bag,2)]);
      if(v.bulk>0) rows.push(["Bulk cost, same volume","$"+h.f(yd*v.bulk,2)]);
      let note="A cubic yard is 27 cubic feet. Check the volume printed on the bag, since sizes vary by brand.";
      if(v.bag>0&&v.bulk>0){ const d=v.bags*v.bag-yd*v.bulk;
        note=d>0?"Bulk is about $"+h.f(d,0)+" cheaper before delivery fees.":"Bags are about $"+h.f(-d,0)+" cheaper and need no delivery."; }
      return {big:[h.f(yd,2),"cubic yards"], rows:rows, note:note}; }""",
  table_head=["Bag size","Bags in 1 cubic yard","Bags in 2 cubic yards"],
  table=[["0.5 cu ft","54","108"],["0.75 cu ft","36","72"],["1 cu ft","27","54"],["1.5 cu ft","18","36"],["2 cu ft","13.5 (14)","27"],["3 cu ft","9","18"]],
  table_title="Bags per cubic yard",
  how="""<p>Bags are labeled in cubic feet and bulk material is sold in cubic yards, so the conversion is a single division. One cubic yard is 3 ft x 3 ft x 3 ft, which is 27 cubic feet.</p>
<p><b>Cubic feet</b> = number of bags x bag size (cu ft)<br><b>Cubic yards</b> = cubic feet / 27<br><b>Bags per cubic yard</b> = 27 / bag size</p>
<p>Example: 40 bags of mulch at 2 cubic feet each is 80 cubic feet, which is 80 / 27 = 2.96 cubic yards. If a cubic yard of bulk mulch costs $40 and a bag costs $4.50, the bags cost $180 and 2.96 yards of bulk cost about $119.</p>
<p>Bag sizes shown in the menu are common retail sizes, such as 0.75 cubic foot topsoil, 1.5 cubic foot garden soil and 2 or 3 cubic foot mulch. Some bags are sold by weight only, in which case the volume depends on the material. Always use the cubic feet printed on the bag.</p>""",
  faq=[("How many bags of mulch are in a cubic yard?","A cubic yard is 27 cubic feet, so it holds 13.5 bags of 2 cubic feet or 9 bags of 3 cubic feet."),
       ("How many 1 cubic foot bags make a yard?","27. Divide 27 by the bag size in cubic feet for any bag."),
       ("Is it cheaper to buy mulch or soil in bags or in bulk?","Bulk is usually cheaper per cubic yard once you need about two to three yards or more, but delivery fees can erase the savings on small jobs. Enter both prices above to compare."),
       ("How many 0.75 cubic foot bags of topsoil are in a yard?","36. Divide 27 by 0.75.")],
  supplies=["wheelbarrow","garden rake","landscape tarp","work gloves"],
  related=["mulch-calculator","topsoil-calculator","raised-bed-soil-calculator","gravel-calculator"],
 ),

 dict(
  slug="cubic-yards-to-tons-calculator",
  kind="yardstotons",
  group="Stone & hardscape",
  name="Cubic Yards to Tons Calculator",
  short="Convert yards of gravel, sand, soil or mulch to tons.",
  title="Cubic Yards to Tons Calculator by Material",
  desc="Free cubic yards to tons calculator for gravel, sand, topsoil, compost and mulch. Pick the material or enter your own density to get tons, pounds and cost.",
  h1="Cubic yards to tons calculator",
  lede="Pick a material, enter cubic yards, and get the approximate weight in tons and pounds. Weight varies with moisture, so enter your supplier's density if you have it.",
  area=False,
  fields=[
    dict(id="yd", label="Cubic yards", value=5, step=0.25),
    dict(id="m", label="Material", type="select", value=1, options=[
      [1, "Gravel or crushed stone (about 1.4 tons/yd)"],
      [2, "Sand (about 1.4 tons/yd)"],
      [3, "Topsoil (about 1.1 tons/yd)"],
      [4, "Compost (about 0.5 tons/yd)"],
      [5, "Wood mulch (about 0.25 tons/yd)"]]),
    dict(id="custom", label="Your own density (optional)", unit="lb/cu yd", optional=True, hint="Overrides the material above, e.g. from your supplier"),
    dict(id="price", label="Price per ton", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const d=[0,2800,2800,2200,1000,500][v.m]||0; const lbyd=v.custom>0?v.custom:d;
      const lb=v.yd*lbyd, tons=lb/2000;
      const rows=[["Pounds",h.c(lb)],["Metric tons",h.f(tons*0.907185,2)],["Density used",h.c(lbyd)+" lb per cu yd"],["Tons per cubic yard",h.f(lbyd/2000,2)]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(tons,2),"US tons"], rows:rows, note:"Weights are approximate and rise when material is wet or compacted. Tons here are US short tons of 2,000 lb."}; }""",
  table_head=["Material","Tons per cubic yard (about)","Pounds per cubic yard"],
  table=[["Gravel or crushed stone","1.3-1.5","2,600-3,000"],["Sand, dry","1.3-1.5","2,600-3,000"],["Topsoil, dry","1.0-1.3","2,000-2,600"],["Compost","about 0.5","about 1,000"],["Wood mulch","0.1-0.4","200-800"]],
  table_title="Typical weight by material",
  how="""<p>Suppliers sell stone and sand by the ton and by the cubic yard, and the link between them is the material's density. A US ton is 2,000 pounds.</p>
<p><b>Pounds</b> = cubic yards x density (lb per cu yd)<br><b>Tons</b> = pounds / 2,000</p>
<p>Example: 5 cubic yards of gravel at about 2,800 lb per cubic yard weighs 14,000 lb, or about 7 tons. Five yards of topsoil at 2,200 lb per cubic yard is about 5.5 tons, and five yards of compost at about 1,000 lb is 2.5 tons.</p>
<p>The default densities come from the middle of commonly published ranges, including 1.4 tons per cubic yard for sand from the Minnesota Pollution Control Agency, about 1,000 lb per cubic yard for compost from University of New Hampshire Extension, and roughly 0.1 to 0.4 tons for wood mulch. Wet material is heavier, and fine soils swing the most. Ask your supplier for the figure they use, enter it in the density box, and treat the result as an estimate.</p>""",
  faq=[("How many tons are in a cubic yard of gravel?","About 1.3 to 1.5 tons, depending on stone size, fines and moisture. This calculator uses about 1.4."),
       ("How many cubic yards are in a ton of gravel?","About 0.7. Divide 1 by the tons per cubic yard, so 1 / 1.4 is about 0.71 cubic yards."),
       ("Does wet material weigh more?","Yes. Wet sand and soil can weigh noticeably more per cubic yard than dry, so a delivery after rain may be heavier than quoted."),
       ("Is a ton the same as a metric ton?","No. A US ton is 2,000 lb. A metric ton is about 2,205 lb. The results table shows both.")],
  supplies=["wheelbarrow","landscape rake","heavy duty tarp","work gloves"],
  related=["gravel-calculator","topsoil-calculator","paver-base-calculator","river-rock-calculator"],
 ),

 dict(
  slug="lime-calculator",
  kind="lime",
  group="Lawn & garden",
  name="Lawn Lime Calculator",
  short="Pounds and bags of lime from your soil test.",
  title="Lawn Lime Calculator: Pounds and Bags of Lime",
  desc="Free lawn lime calculator. Enter lawn size, the lime requirement from your soil test and the bag's calcium carbonate equivalent to get pounds, bags and applications.",
  h1="Lawn lime calculator",
  lede="Lime rates come from a soil test, not a guess. Enter the requirement on your test report and the strength printed on the bag to see how much lime to buy.",
  area=True,
  waste=None,
  dims=(50, 40),
  fields=[
    dict(id="req", label="Lime requirement from soil test", unit="lb/1,000 sq ft", value=50, step=5, hint="Pounds of pure calcium carbonate per 1,000 sq ft, from your report"),
    dict(id="cce", label="Calcium carbonate equivalent", unit="%", value=90, step=1, hint="On the bag; ground limestone is about 70-95"),
    dict(id="bag", label="Bag weight", unit="lb", value=40, step=1, hint="Bags are commonly 30, 40 or 50 lb"),
    dict(id="price", label="Price per bag", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const prod=v.cce>0?v.req/(v.cce/100):0; const total=prod*v.area/1000;
      const apps=prod>0?Math.ceil(prod/50):0; const bags=v.bag>0?Math.ceil(total/v.bag):0;
      const rows=[["Lime per 1,000 sq ft",h.f(prod,1)+" lb"],["Applications (max 50 lb per 1,000 sq ft each)",String(apps)],
        ["Per application",apps>0?h.f(prod/apps,1)+" lb per 1,000 sq ft":"0"],["Bags needed",String(bags)],["Area limed",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(bags*v.price,2)]);
      return {big:[h.f(total,0),"pounds of lime"], rows:rows, note:"Follow your soil test and the product label first. Brand rates on bags can differ from this general calculation."}; }""",
  table_head=["Material","Calcium carbonate equivalent","Speed","Max per application (lb/1,000 sq ft)"],
  table=[["Ground limestone","70-95","Slow","50"],["Dolomitic limestone","70-95","Slow","50"],["Pelletized limestone","70-95","Fast","50"],["Hydrated lime","about 140","Fast","20"],["Burned lime","about 180","Fast","10"]],
  table_title="Liming materials and maximum rates",
  how="""<p>A soil test reports how much pure calcium carbonate your lawn needs to reach a healthy pH. Lime on the shelf is weaker than pure calcium carbonate, so the calculator divides the requirement by the bag's calcium carbonate equivalent (CCE).</p>
<p><b>Lime per 1,000 sq ft</b> = requirement / (CCE / 100)<br><b>Total lime</b> = lime per 1,000 sq ft x area / 1,000<br><b>Applications</b> = lime per 1,000 sq ft / 50, rounded up</p>
<p>Example: a 5,000 sq ft lawn with a requirement of 50 lb per 1,000 sq ft and a 90% CCE lime needs 50 / 0.9 = 55.6 lb per 1,000 sq ft. That is 278 lb in total, or seven 40 lb bags. Because it is above 50 lb per 1,000 sq ft, split it into two passes of about 28 lb, months apart.</p>
<p>The 50 lb maximum and the product table follow Ohio State University Extension guidance. Do not apply lime without a soil test, since too much can push soil pH too high.</p>""",
  faq=[("How much lime do I need per 1,000 square feet?","It depends on the soil test. A common rate for ground limestone is about 50 lb per 1,000 square feet, and the soil test report gives the exact requirement."),
       ("When is the best time to lime a lawn?","Spring or fall, when rain is common, is recommended because rain moves lime into the root zone. Avoid wilted or frost-covered turf."),
       ("What does calcium carbonate equivalent mean?","It is the percent of the product's liming strength compared with pure calcium carbonate. A bag rated 90 is 90% as strong, so you need more product than the soil test number."),
       ("Can gypsum replace lime?","No. Gypsum barely changes soil pH, so it is not a liming material.")],
  supplies=["pelletized lime","soil test kit","broadcast spreader","lawn core aerator rental"],
  related=["fertilizer-calculator","grass-seed-calculator","sod-calculator"],
 ),
]
