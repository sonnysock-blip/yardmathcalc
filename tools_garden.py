TOOLS = [
 dict(
  slug="raised-bed-soil-calculator",
  kind="raisedbed",
  group="Mulch & soil",
  name="Raised Bed Soil Calculator",
  short="Soil mix, bags and yards to fill raised beds.",
  title="Raised Bed Soil Calculator: Cubic Feet, Yards, Bags",
  desc="Free raised bed soil calculator. Enter bed size, depth and count to get cubic feet, cubic yards, bag counts and how much topsoil, compost or Mel's Mix to buy.",
  h1="Raised bed soil calculator",
  lede="Enter the inside size of your beds and pick a soil recipe to see the total volume, how much of each ingredient to buy, and how many bags that is.",
  area=False,
  waste=None,
  fields=[
    dict(id="len", label="Bed length", unit="ft", value=8, step=0.5, hint="Measure inside the frame"),
    dict(id="wid", label="Bed width", unit="ft", value=4, step=0.5, hint="4 ft lets you reach the middle from both sides"),
    dict(id="ht", label="Soil depth", unit="in", value=12, step=1, hint="Usually the bed height; 10-12 in suits most vegetables"),
    dict(id="beds", label="Number of beds", unit="beds", value=1, step=1),
    dict(id="mix", label="Soil mix", type="select", value=1, options=[
      [1, "60% topsoil, 40% compost"],
      [2, "50% topsoil, 50% compost"],
      [3, "Mel's Mix (1/3 compost, 1/3 peat moss, 1/3 vermiculite)"],
      [4, "Bagged raised bed mix (one product)"]]),
    dict(id="settle", label="Extra for settling", unit="%", value=10, step=1, hint="10-15% covers settling in the first season"),
    dict(id="price", label="Price per cubic yard", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const ft3=v.len*v.wid*(v.ht/12)*v.beds*(1+v.settle/100); const yd=ft3/27;
      const mixes={1:[["Topsoil",0.6],["Compost",0.4]],2:[["Topsoil",0.5],["Compost",0.5]],
        3:[["Compost",1/3],["Peat moss",1/3],["Coarse vermiculite",1/3]],4:[["Raised bed mix",1]]};
      const parts=mixes[v.mix]||mixes[1];
      const rows=[["Total cubic feet",h.f(ft3,1)]];
      parts.forEach(p=>rows.push([p[0],h.f(ft3*p[1],1)+" cu ft ("+h.f(ft3*p[1]/27,2)+" cu yd)"]));
      rows.push(["1 cu ft bags (total)",h.c(ft3)]);
      rows.push(["1.5 cu ft bags (total)",h.c(ft3/1.5)]);
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(yd*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of soil"], rows:rows,
        note:"Bag counts assume every ingredient comes in that bag size. Compressed peat moss bales expand, so check the loose volume on the label."}; }""",
  table_head=["Bed size (inside)", "Depth", "Soil needed"],
  table=[["4 x 4 ft", "12 in", "16 cu ft (0.59 cu yd)"],
         ["4 x 8 ft", "6 in", "16 cu ft (0.59 cu yd)"],
         ["4 x 8 ft", "12 in", "32 cu ft (1.19 cu yd)"],
         ["3 x 6 ft", "18 in", "27 cu ft (1.00 cu yd)"],
         ["4 x 12 ft", "12 in", "48 cu ft (1.78 cu yd)"]],
  table_title="Soil for common raised bed sizes",
  how="""<p>A raised bed is a box, so its soil volume is length times width times depth. The calculator converts the depth to feet, multiplies by the number of beds, and adds your settling allowance.</p>
<p><b>Cubic feet</b> = length (ft) x width (ft) x depth (in) / 12 x number of beds x (1 + extra % / 100)<br><b>Cubic yards</b> = cubic feet / 27<br><b>Each ingredient</b> = cubic feet x its share of the mix</p>
<p>Example: two 4 x 8 ft beds filled 12 inches deep hold 64 cubic feet. With 10% extra that is 70.4 cubic feet, or about 2.61 cubic yards. A 60/40 mix needs about 42.2 cubic feet of topsoil and 28.2 cubic feet of compost. In 1.5 cubic foot bags that is 47 bags in total.</p>
<p>Mel's Mix, from Square Foot Gardening, is equal parts compost, peat moss and coarse vermiculite by volume. The 60/40 and 50/50 blends are common bulk orders from landscape yards. Fresh, fluffy soil settles as it is watered, which is why the extra field starts at 10%. Bulk delivery usually beats bags once you need more than about a cubic yard.</p>""",
  faq=[("How much soil do I need for a 4 x 8 raised bed?","A 4 x 8 ft bed filled 12 inches deep holds 32 cubic feet, about 1.19 cubic yards. Add about 10% for settling, so plan on roughly 35 cubic feet."),
       ("How many bags of soil fill a raised bed?","Divide the bed's cubic feet by the bag size. A 32 cubic foot bed takes 32 bags of 1 cubic foot or about 22 bags of 1.5 cubic feet."),
       ("What is the best soil mix for raised beds?","A blend of about 60% screened topsoil and 40% compost works well for most vegetables. Mel's Mix, equal parts compost, peat moss and vermiculite, is lighter and drains well but costs more."),
       ("Can I fill the bottom of a raised bed with something cheaper?","In beds deeper than about 18 inches, some gardeners fill the bottom with logs, branches or leaves to save soil. That material breaks down and settles, so expect to top up each year.")],
  supplies=["raised garden bed kit", "raised bed soil mix", "bagged compost", "coarse vermiculite", "peat moss"],
  related=["topsoil-calculator", "compost-calculator", "mulch-calculator"],
 ),

 dict(
  slug="compost-calculator",
  kind="compost",
  group="Mulch & soil",
  name="Compost Calculator",
  short="Compost for top-dressing lawns and amending beds.",
  title="Compost Calculator: Cubic Yards and Bags Needed",
  desc="Free compost calculator. Enter your lawn or bed size and depth to get cubic feet, cubic yards, 1 cu ft and 0.75 cu ft bag counts, and a cost estimate.",
  h1="Compost calculator",
  lede="Measure the lawn or garden bed, pick a depth, and see how much compost to order in bulk or how many bags to buy.",
  area=True,
  waste=5,
  fields=[
    dict(id="depth", label="Compost depth", unit="in", value=2, step=0.25, hint="1/4-1/2 in to top-dress a lawn, 1-3 in to dig into beds"),
    dict(id="price", label="Price per cubic yard", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const ft3=v.area*v.depth/12; const yd=ft3/27;
      const rows=[["Cubic feet",h.f(ft3,1)],["1 cu ft bags",h.c(ft3)],["0.75 cu ft bags",h.c(ft3/0.75)],["Area covered",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(yd*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of compost"], rows:rows,
        note:"Many 40 lb bags of compost hold about 0.75 cu ft. Check the volume printed on the bag."}; }""",
  table_head=["Use", "Depth", "1 cu yd covers"],
  table=[["Top-dressing a lawn", "1/4 in", "about 1,300 sq ft"],
         ["Top-dressing a thin lawn", "1/2 in", "about 650 sq ft"],
         ["Amending an existing bed", "1 in", "324 sq ft"],
         ["Preparing a new bed", "2 in", "162 sq ft"],
         ["Heavy amendment of poor soil", "3 in", "108 sq ft"]],
  table_title="How much compost to spread",
  how="""<p>Compost is sold by volume, so the calculator multiplies your area by the depth, converts inches to feet, and divides by 27 to get cubic yards.</p>
<p><b>Cubic feet</b> = area (sq ft) x depth (in) / 12<br><b>Cubic yards</b> = cubic feet / 27<br><b>Bags</b> = cubic feet / bag size (cu ft)</p>
<p>Example: a 5,000 sq ft lawn top-dressed 1/4 inch deep needs about 104 cubic feet, which is about 3.86 cubic yards. A 200 sq ft vegetable bed with 2 inches of compost needs about 33 cubic feet, or 1.23 cubic yards, or 45 bags of 0.75 cubic feet.</p>
<p>Extension guides commonly suggest about 1/4 inch for a yearly lawn top-dressing, raked into the turf after aerating. For beds, 1 to 3 inches is typical, mixed into the top several inches of soil before planting. Thicker layers on a lawn can smother the grass. The extra field adds 5% for uneven spreading.</p>""",
  faq=[("How much compost do I need to top-dress a lawn?","About 1/4 inch, which works out to roughly 0.77 cubic yards per 1,000 sq ft. Going much past 1/2 inch can smother the grass."),
       ("How many bags of compost are in a yard?","A cubic yard is 27 cubic feet, so it equals 27 bags of 1 cubic foot or 36 bags of 0.75 cubic feet."),
       ("How much compost should I add to a garden bed?","Spread 1 to 3 inches and mix it into the top 4 to 8 inches of soil. Use the higher end for new beds or heavy clay."),
       ("When is the best time to spread compost?","For lawns, early fall or spring, ideally right after core aeration. For beds, a few weeks before planting or in fall after cleanup.")],
  supplies=["bagged compost", "compost spreader", "lawn aerator rental", "garden rake"],
  related=["topsoil-calculator", "raised-bed-soil-calculator", "grass-seed-calculator", "mulch-calculator"],
 ),

 dict(
  slug="grass-seed-calculator",
  kind="grassseed", dims=(50, 40),
  group="Lawn & garden",
  name="Grass Seed Calculator",
  short="Pounds and bags of seed for a new lawn or overseeding.",
  title="Grass Seed Calculator: Pounds and Bags of Seed",
  desc="Free grass seed calculator. Pick your grass type and whether you are seeding a new lawn or overseeding, and get pounds of seed, bag counts and a cost estimate.",
  h1="Grass seed calculator",
  lede="Measure the lawn, choose a grass type, and see how many pounds of seed to buy for a new lawn or for overseeding thin turf.",
  area=True,
  waste=None,
  fields=[
    dict(id="seed", label="Grass type", type="select", value=7, options=[
      [7, "Tall fescue (about 7 lb/1,000 sq ft)"],
      [2.5, "Kentucky bluegrass (about 2.5 lb)"],
      [7.5, "Perennial ryegrass (about 7.5 lb)"],
      [4, "Fine fescue (about 4 lb)"],
      [1, "Bermudagrass, hulled (about 1 lb)"],
      [1.5, "Zoysiagrass (about 1.5 lb)"]]),
    dict(id="job", label="Job", type="select", value=1, options=[
      [1, "New lawn or bare soil (full rate)"],
      [0.5, "Overseeding an existing lawn (half rate)"]]),
    dict(id="price", label="Price per lb", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const rate=v.seed*v.job; const lb=v.area/1000*rate;
      const rows=[["Seeding rate",h.f(rate,2)+" lb per 1,000 sq ft"],["3 lb bags",h.c(lb/3)],["7 lb bags",h.c(lb/7)],["20 lb bags",h.c(lb/20)],["Area seeded",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(lb*v.price,2)]);
      return {big:[h.f(lb,1),"pounds of seed"], rows:rows,
        note:"Rates are typical midpoints for pure seed. Mixes and coated seed differ, so follow the rate on your bag if it gives one."}; }""",
  table_head=["Grass type", "New lawn (lb per 1,000 sq ft)", "Overseeding"],
  table=[["Tall fescue", "6-8", "3-4"],
         ["Kentucky bluegrass", "2-3", "1-1.5"],
         ["Perennial ryegrass", "7-8", "3.5-4"],
         ["Fine fescue", "3-6", "1.5-3"],
         ["Bermudagrass (hulled)", "0.5-1", "0.25-0.5"],
         ["Zoysiagrass", "1-2", "0.5-1"]],
  table_title="Grass seeding rates",
  how="""<p>Seed is sold by weight, and every grass has its own seeding rate in pounds per 1,000 square feet. The calculator scales that rate to your lawn and halves it for overseeding, a common extension rule of thumb.</p>
<p><b>Pounds of seed</b> = area (sq ft) / 1,000 x rate (lb per 1,000 sq ft) x job factor<br><b>Job factor</b> = 1 for a new lawn, 0.5 for overseeding</p>
<p>Example: a 5,000 sq ft new tall fescue lawn at 7 lb per 1,000 sq ft needs 35 lb of seed, which is two 20 lb bags. Overseeding the same lawn takes about 17.5 lb.</p>
<p>The default rates sit in the middle of ranges published by university turf programs such as Ohio State, Kansas State and Tennessee. Small-seeded grasses like bluegrass and bermudagrass need far fewer pounds because each pound holds millions of seeds. Coated seed weighs more, so the bag rate can be up to double. Use the bag's own rate when it differs.</p>""",
  faq=[("How much grass seed do I need per 1,000 square feet?","It depends on the grass. Tall fescue needs about 6 to 8 lb for a new lawn, Kentucky bluegrass 2 to 3 lb, and hulled bermudagrass about 1 lb."),
       ("How much seed do I need to overseed?","About half the new-lawn rate. For tall fescue that is roughly 3 to 4 lb per 1,000 square feet."),
       ("Can I put down too much grass seed?","Yes. Seeding far above the recommended rate crowds seedlings, which then compete for water and light and are more prone to disease."),
       ("When is the best time to plant grass seed?","Late summer to early fall for cool-season grasses such as fescue and bluegrass. Late spring to early summer, once soil is warm, for bermudagrass and zoysia.")],
  supplies=["grass seed", "broadcast spreader", "starter fertilizer", "seed starting mulch", "lawn aerator rental"],
  related=["sod-calculator", "fertilizer-calculator", "compost-calculator", "topsoil-calculator"],
 ),

 dict(
  slug="fertilizer-calculator",
  kind="fertilizer", dims=(50, 40),
  group="Lawn & garden",
  name="Fertilizer Calculator",
  short="Pounds and bags of lawn fertilizer from the N-P-K.",
  title="Lawn Fertilizer Calculator: Pounds of Product and Bags",
  desc="Free lawn fertilizer calculator. Enter lawn size, the nitrogen number from the bag and your target rate to get pounds of product, bags needed and cost.",
  h1="Lawn fertilizer calculator",
  lede="Use the first number on the fertilizer bag and your lawn size to find how many pounds of product to spread and how many bags to buy.",
  area=True,
  waste=None,
  fields=[
    dict(id="n", label="Nitrogen in the product", unit="% N", value=20, step=1, hint="The first number of the N-P-K, e.g. 20 in 20-0-5"),
    dict(id="rate", label="Nitrogen to apply", unit="lb N/1,000 sq ft", value=1, step=0.25, hint="0.5-1 lb per feeding; use 0.5 for quick-release products"),
    dict(id="bag", label="Bag weight", unit="lb", value=20, step=0.5),
    dict(id="price", label="Price per bag", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const per=v.n>0?v.rate/(v.n/100):0; const lb=per*v.area/1000; const bags=v.bag>0?lb/v.bag:0;
      const rows=[["Product per 1,000 sq ft",h.f(per,2)+" lb"],["Bags needed",h.c(bags)],["Nitrogen applied (total)",h.f(v.rate*v.area/1000,2)+" lb"],["Area fed",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(Math.ceil(bags)*v.price,2)]);
      return {big:[h.f(lb,1),"pounds of fertilizer"], rows:rows,
        note:"The product label's rate and spreader setting take priority over this estimate."}; }""",
  table_head=["Product (N-P-K)", "Nitrogen", "Product for 1 lb N per 1,000 sq ft"],
  table=[["10-10-10", "10%", "10 lb"],
         ["16-4-8", "16%", "6.25 lb"],
         ["20-0-5", "20%", "5 lb"],
         ["24-0-11", "24%", "4.2 lb"],
         ["29-0-4", "29%", "3.4 lb"],
         ["32-0-4", "32%", "3.1 lb"]],
  table_title="Pounds of product per 1,000 sq ft",
  how="""<p>Lawn fertilizer rates are given as pounds of nitrogen per 1,000 square feet, not pounds of product. The first number in the N-P-K is the percent of the bag's weight that is nitrogen, so the calculator divides your target rate by that percent.</p>
<p><b>Product per 1,000 sq ft</b> = target lb N / (N% / 100)<br><b>Total product</b> = product per 1,000 sq ft x area (sq ft) / 1,000<br><b>Bags</b> = total product / bag weight</p>
<p>Example: a 32-0-4 product at 1 lb N per 1,000 sq ft needs 1 / 0.32 = 3.125 lb of product per 1,000 sq ft. A 5,625 sq ft lawn takes about 17.6 lb, which is one 20 lb bag.</p>
<p>University extension guides usually suggest 0.5 to 1 lb of nitrogen per feeding, with no more than about 0.5 lb from fast-release products. Total yearly nitrogen depends on grass type and region. Always follow the product label and any local fertilizer rules, which take priority over this estimate.</p>""",
  faq=[("How do I read the numbers on a fertilizer bag?","The three numbers are the percent by weight of nitrogen, phosphate and potash. A 50 lb bag of 20-5-10 contains 10 lb of nitrogen."),
       ("How much fertilizer per 1,000 square feet?","Divide your target nitrogen rate by the nitrogen percent. For 1 lb of nitrogen from a 20-0-5 product that is 5 lb of product per 1,000 square feet."),
       ("How much nitrogen should I put on my lawn per year?","Often 2 to 4 lb per 1,000 square feet a year for cool-season lawns, split across several feedings. Warm-season grasses and low-input lawns vary, so check your local extension guide."),
       ("Should I water in fertilizer?","Most granular lawn fertilizers should be watered in with about 1/4 inch of water soon after applying, but follow the label, since some weed-and-feed products need dry leaves.")],
  supplies=["lawn fertilizer", "broadcast spreader", "soil test kit", "drop spreader"],
  related=["grass-seed-calculator", "sod-calculator", "compost-calculator"],
 ),

 dict(
  slug="deck-stain-calculator",
  kind="deckstain",
  group="Lawn & garden",
  name="Deck Stain Calculator",
  short="Gallons of stain for a deck, railing and stairs.",
  title="Deck Stain Calculator: How Many Gallons You Need",
  desc="Free deck stain calculator. Enter deck size, railing length and stairs to get square feet to cover, gallons per coat, total gallons and 1 or 5 gallon cans.",
  h1="Deck stain calculator",
  lede="Measure the deck floor, railing and stairs, pick your stain type, and see how many gallons to buy for the coats you plan.",
  area=False,
  waste=None,
  fields=[
    dict(id="len", label="Deck length", unit="ft", value=16, step=0.5),
    dict(id="wid", label="Deck width", unit="ft", value=12, step=0.5),
    dict(id="rail", label="Railing length", unit="linear ft", value=0, step=1, hint="Total run of railing; 0 if none"),
    dict(id="railh", label="Railing height", unit="ft", value=3, step=0.25, hint="36 in is typical"),
    dict(id="steps", label="Stair steps", unit="steps", value=0, step=1, hint="About 5 sq ft per step for a 3-4 ft wide stair"),
    dict(id="cov", label="Stain type", type="select", value=250, options=[
      [300, "Transparent or toner (about 300 sq ft/gal)"],
      [250, "Semi-transparent (about 250 sq ft/gal)"],
      [200, "Solid color (about 200 sq ft/gal)"]]),
    dict(id="coats", label="Coats", unit="coats", value=2, step=1),
    dict(id="price", label="Price per gallon", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const floor=v.len*v.wid; const rail=v.rail*v.railh*2; const stairs=v.steps*5;
      const sq=floor+rail+stairs; const per=v.cov>0?sq/v.cov:0; const gal=per*v.coats;
      let fives=Math.floor(gal/5); let ones=Math.ceil(gal-fives*5-1e-9);
      if(ones>=4){fives+=1;ones=0;}
      const rows=[["Square feet to cover",h.c(sq)],["Floor",h.c(floor)+" sq ft"],["Railing (both sides)",h.c(rail)+" sq ft"],["Stairs",h.c(stairs)+" sq ft"],
        ["Gallons per coat",h.f(per,2)],["Cans to buy",fives+" x 5 gal + "+ones+" x 1 gal"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(gal*v.price,2)]);
      return {big:[h.f(gal,1),"gallons of stain"], rows:rows,
        note:"Coverage is for rough or weathered wood; smooth new boards take less, and a second coat often goes further than the first. When 4 or more extra gallons are needed, the can mix rounds up to another 5 gallon pail."}; }""",
  table_head=["Stain type", "Rough or weathered wood", "Smooth wood"],
  table=[["Transparent or toner", "about 250-350 sq ft/gal", "about 400-600 sq ft/gal"],
         ["Semi-transparent", "about 200-300 sq ft/gal", "about 400-500 sq ft/gal"],
         ["Solid color", "about 200-300 sq ft/gal", "about 400-500 sq ft/gal"]],
  table_title="Deck stain coverage per gallon",
  how="""<p>The calculator adds up three surfaces, divides by your stain's coverage per gallon, and multiplies by the number of coats.</p>
<p><b>Floor</b> = length (ft) x width (ft)<br><b>Railing</b> = railing length (ft) x railing height (ft) x 2 sides<br><b>Stairs</b> = steps x about 5 sq ft<br><b>Gallons</b> = (floor + railing + stairs) / coverage per gallon x coats</p>
<p>Example: a 16 x 12 ft deck is 192 sq ft. Add 40 ft of 3 ft railing (240 sq ft for both sides) and 4 steps (20 sq ft) for 452 sq ft. Semi-transparent stain at about 250 sq ft per gallon needs 1.81 gallons per coat, or about 3.6 gallons for two coats.</p>
<p>Coverage figures follow manufacturer ranges for rough or weathered surfaces, which soak up more stain than smooth new boards. Railing balusters have four faces, so treating the railing as two solid sides is a rough but practical estimate. The 5 sq ft per step allows for the tread, riser and stringer faces of a typical stair.</p>""",
  faq=[("How much does a gallon of deck stain cover?","Usually about 200 to 300 square feet on rough or weathered wood, and up to 400 to 600 square feet on smooth wood. The can lists the figure for that product."),
       ("How many coats of deck stain do I need?","Many semi-transparent and solid stains call for two coats, often applied wet-on-wet. Some penetrating oils are a single coat, so check the label."),
       ("How much stain for a 12 x 16 deck?","The floor alone is 192 square feet, so about 0.8 gallon per coat of semi-transparent stain. Railings and stairs can more than double that."),
       ("Should I buy a 5 gallon pail or 1 gallon cans?","A 5 gallon pail usually costs less per gallon once you need four or more. Buying all the stain from one batch, or mixing cans together, keeps the color even.")],
  supplies=["deck stain", "deck cleaner", "stain pad applicator", "pump sprayer", "deck brush"],
  related=["concrete-calculator", "fence-post-concrete-calculator", "paver-base-calculator"],
 ),
]
