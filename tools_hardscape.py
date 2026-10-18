TOOLS = [
 dict(
  slug="paver-base-calculator",
  kind="paverbase",
  group="Stone & hardscape",
  name="Paver Base Calculator",
  short="Gravel base, bedding sand and pavers for a patio.",
  title="Paver Base Calculator: Gravel, Sand and Pavers",
  desc="Free paver base calculator. Enter your patio size and base depth to get crushed stone in cubic yards and tons, bedding sand bags, and the number of pavers.",
  h1="Paver base calculator",
  lede="A paver patio needs a compacted gravel base, about 1 inch of bedding sand, and the pavers themselves. Enter your area and depths to get all three.",
  area=True,
  waste=5,
  fields=[
    dict(id="base", label="Gravel base depth (compacted)", unit="in", value=4, step=0.5, hint="4-6 in for patios and walks, 8-12 in for driveways"),
    dict(id="comp", label="Compaction allowance", unit="%", value=15, step=1, hint="Crushed stone loses about 15-20% of its loose volume when compacted"),
    dict(id="sand", label="Bedding sand depth", unit="in", value=1, step=0.25, hint="About 1 in; do not go over 1.5 in"),
    dict(id="plen", label="Paver length", unit="in", value=8, step=0.25, hint="Standard brick paver is 4 x 8 in"),
    dict(id="pwid", label="Paver width", unit="in", value=4, step=0.25),
    dict(id="price", label="Price per ton (base stone)", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const c=Math.min(v.comp,90)/100;
      const yd=v.area*v.base/12/27/(1-c), ft3=yd*27, tons=yd*1.4;
      const sand=v.area*v.sand/12, pa=v.plen*v.pwid, n=pa>0?v.area*144/pa:0;
      const rows=[["Base stone (tons, approx.)",h.f(tons,2)],["Base stone, 0.5 cu ft bags",h.c(ft3/0.5)],
        ["Bedding sand (cu ft)",h.f(sand,1)],["Bedding sand, 0.5 cu ft bags",h.c(sand/0.5)],
        ["Pavers",h.c(n)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of base"], rows,
        note:"Base volume is loose stone to order, at about 1.4 tons per cubic yard. Paver count uses the extra % entered above." }; }""",
  table_head=["Project","Gravel base","Bedding sand"],
  table=[["Garden walkway","4 in","1 in"],["Patio, mild climate","4-6 in","1 in"],["Patio, freezing winters or clay soil","6-8 in","1 in"],["Residential driveway","8-12 in","1 in"]],
  table_title="Recommended base depths",
  how="""<p>The calculator works out three quantities from your area, which already includes the extra percentage.</p>
<p><b>Base (cu yd)</b> = area (sq ft) x base depth (in) / 12 / 27 / (1 - compaction %)<br>
<b>Base (tons)</b> = cubic yards x 1.4<br>
<b>Bedding sand (cu ft)</b> = area x sand depth (in) / 12<br>
<b>Pavers</b> = area x 144 / (paver length x width in inches)</p>
<p>Example: a 10 x 20 ft patio is 200 sq ft, or 210 sq ft with 5% extra. A 4 in compacted base needs 210 x 4 / 12 / 27 = 2.59 cubic yards in place. Crushed stone shrinks about 15% when compacted, so order 2.59 / 0.85 = 3.05 cubic yards, about 4.3 tons. One inch of sand is 17.5 cu ft, or 35 half-cubic-foot bags. With 4 x 8 in pavers (4.5 per sq ft) you need 945 pavers.</p>
<p>Crushed stone base weighs about 1.35 to 1.45 tons per cubic yard depending on gradation and moisture. Use a dense-graded 3/4 in minus base (with fines) so it locks together, and compact it in 2 to 3 inch lifts.</p>""",
  faq=[("How deep should a paver base be?","About 4 inches of compacted gravel for walkways and 4 to 6 inches for patios. Use 6 to 8 inches in freezing climates or clay soil, and 8 to 12 inches under driveways."),
       ("How much sand goes under pavers?","About 1 inch of coarse concrete sand, screeded flat over the compacted base. Sand thicker than about 1.5 inches tends to shift and cause uneven pavers."),
       ("How many 4 x 8 pavers are in a square foot?","4.5. Each 4 x 8 in paver covers 32 square inches, and a square foot is 144 square inches."),
       ("Do I need to compact the gravel base?","Yes. Compact it in lifts of 2 to 3 inches with a plate compactor. An uncompacted base settles and lets pavers sink and rock.")],
  supplies=["plate compactor rental","paver base gravel","paver sand","paver edge restraint","polymeric sand"],
  related=["gravel-calculator","concrete-calculator","retaining-wall-block-calculator"],
 ),

 dict(
  slug="retaining-wall-block-calculator",
  kind="wallblock",
  group="Stone & hardscape",
  name="Retaining Wall Block Calculator",
  short="Blocks, caps and drainage gravel for a garden wall.",
  title="Retaining Wall Block Calculator: Blocks and Caps",
  desc="Free retaining wall block calculator. Enter wall length, height and block size to get blocks per course, total blocks, caps, and gravel for base and backfill.",
  h1="Retaining wall block calculator",
  lede="Enter the length and exposed height of your wall and the face size of the block you plan to use. You get the block count, cap count, and gravel for the base and drainage zone.",
  area=False,
  waste=None,
  fields=[
    dict(id="len", label="Wall length", unit="ft", value=20, step=0.5),
    dict(id="ht", label="Exposed wall height", unit="ft", value=2, step=0.25, hint="Height above ground, not counting caps"),
    dict(id="blen", label="Block face length", unit="in", value=11.75, step=0.25, hint="Small garden blocks are about 4 x 11.75 in; large ones about 6 x 18 in"),
    dict(id="bht", label="Block face height", unit="in", value=4, step=0.25),
    dict(id="bury", label="Buried first course", type="select", value=1, options=[[1,"Yes, one course below grade"],[0,"No"]]),
    dict(id="cap", label="Cap blocks", type="select", value=12, options=[[0,"No caps"],[12,"Caps about 12 in long"],[16,"Caps about 16 in long"]]),
    dict(id="price", label="Price per wall block", unit="$", optional=True),
    dict(id="capprice", label="Price per cap", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const per=v.blen>0?Math.ceil(v.len*12/v.blen):0;
      const exp=v.bht>0?Math.ceil(v.ht*12/v.bht):0, courses=exp+(exp>0&&v.bury?1:0), total=per*courses;
      const caps=v.cap>0?Math.ceil(v.len*12/v.cap):0, hft=courses*v.bht/12;
      const back=v.len*1*hft/27, pad=v.len*2*0.5/27;
      const rows=[["Blocks per course",h.c(per)],["Courses",h.c(courses)+(v.bury&&exp>0?" (1 buried)":"")],
        ["Cap blocks",h.c(caps)],["Drainage gravel, 12 in behind wall",h.f(back,2)+" cu yd"],
        ["Leveling base, 6 in x 24 in trench",h.f(pad,2)+" cu yd"]];
      const cost=total*v.price+caps*v.capprice;
      if(cost>0) rows.push(["Estimated cost","$"+h.f(cost,2)]);
      return {big:[h.c(total),"wall blocks"], rows,
        note:(v.ht>3?"Walls over about 3 ft usually need larger blocks, geogrid, or an engineer; check local code. ":"")+"Buy a few spare blocks for cuts and breakage." }; }""",
  table_head=["Block type","Face (H x L)","Typical max height"],
  table=[["Small garden block","4 x 11.75 in","about 2-3 ft"],["Medium wall block","6 x 16-18 in","about 3-4 ft"],["Large wall block","8 x 18 in","about 4 ft, more with geogrid"],["Cap block","3-4 in tall, 12-16 in long","Top course only"]],
  table_title="Common block sizes",
  how="""<p>The calculator counts blocks course by course, rounding up so each row is complete.</p>
<p><b>Blocks per course</b> = wall length (in) / block face length (in), rounded up<br>
<b>Courses</b> = exposed height (in) / block face height (in), rounded up, plus 1 buried course<br>
<b>Total blocks</b> = blocks per course x courses<br>
<b>Caps</b> = wall length (in) / cap length (in), rounded up</p>
<p>Example: a wall 20 ft long and 2 ft high built from 4 x 11.75 in blocks needs 240 / 11.75 = 20.4, so 21 blocks per course. Two feet is 24 inches, or 6 courses, plus 1 buried course makes 7. That is 147 blocks and 20 caps of about 12 inches.</p>
<p>Gravel is estimated for a drainage zone 12 inches deep behind the full block height and a leveling pad 6 inches deep and 24 inches wide. Use clean 3/4 in angular stone behind the wall and a compactable base under it. Block sizes differ by brand, so measure the face of the block you will buy.</p>""",
  faq=[("How many retaining wall blocks do I need?","Divide the wall length by the block length for blocks per course, then multiply by the number of courses. A 20 ft wall of 4 x 11.75 in blocks, 2 ft high plus a buried course, needs about 147 blocks."),
       ("How deep should the first course be buried?","A common guideline is to bury at least one full course, or about 1 inch for every 8 inches of wall height, whichever is more. Follow your block maker's instructions."),
       ("Do I need gravel behind a retaining wall?","Yes. About 12 inches of clean angular stone behind the blocks lets water drain instead of building pressure that pushes the wall over."),
       ("How tall can a block retaining wall be without reinforcement?","Small garden blocks are usually limited to about 2 to 3 feet. Many codes require engineering or a permit for walls over 4 feet.")],
  supplies=["retaining wall blocks","retaining wall caps","masonry adhesive","drainage gravel","landscape fabric"],
  related=["gravel-calculator","paver-base-calculator","topsoil-calculator"],
 ),

 dict(
  slug="river-rock-calculator",
  kind="riverrock",
  group="Stone & hardscape",
  name="River Rock Calculator",
  short="Cubic yards, tons and bags of river rock.",
  title="River Rock Calculator: Cubic Yards, Tons and Bags",
  desc="Free river rock calculator. Enter your bed size and depth to see cubic yards, tons and 0.5 cu ft bags of river rock, with depth guidance for each rock size.",
  h1="River rock calculator",
  lede="Measure your bed or dry creek, choose a depth that suits the rock size, and get cubic yards, approximate tons, and bag counts.",
  area=True,
  waste=5,
  fields=[
    dict(id="depth", label="Depth", unit="in", value=3, step=0.5, hint="2 in for 3/4-1.5 in rock, 3 in for 1-3 in, 4-6 in for larger"),
    dict(id="price", label="Price per ton", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const ft3=v.area*v.depth/12, yd=ft3/27, tons=yd*1.35;
      const rows=[["Weight (approx.)",h.f(tons,2)+" tons"],["Cubic feet",h.f(ft3,1)],["0.5 cu ft bags",h.c(ft3/0.5)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards"], rows,
        note:"Weight uses about 1.35 tons per cubic yard; river rock runs about 1.3 to 1.4." }; }""",
  table_head=["Rock size","Depth","1 ton covers"],
  table=[["3/4-1.5 in","2 in","about 120 sq ft"],["1-3 in","3 in","about 80 sq ft"],["2-5 in","4-5 in","about 50-60 sq ft"],["6 in and up","One layer","about 25 sq ft"]],
  table_title="How deep should river rock be?",
  how="""<p>River rock is sold by the cubic yard, by the ton, or in bags of about 0.5 cubic feet. The calculator finds the volume and converts it to all three.</p>
<p><b>Cubic yards</b> = area (sq ft) x depth (in) / 12 / 27<br>
<b>Tons</b> = cubic yards x 1.35<br>
<b>Bags</b> = cubic feet / 0.5</p>
<p>Example: a 200 sq ft bed with 5% extra is 210 sq ft. At 3 inches deep that is 52.5 cubic feet, or 1.94 cubic yards, which weighs about 2.6 tons. In bags it is 105 half-cubic-foot bags.</p>
<p>The right depth depends on rock size. A layer should be about twice as deep as the stones are wide so no soil or fabric shows through, and large cobbles are laid one stone deep. Round rock rolls underfoot, so it suits beds and drainage more than paths. Weight varies with stone type and moisture, so ask your supplier for their figure.</p>""",
  faq=[("How much does a yard of river rock weigh?","About 1.3 to 1.4 tons, or roughly 2,600 to 2,800 pounds. This calculator uses 1.35 tons."),
       ("How much area does a ton of river rock cover?","At 2 inches deep, about 120 square feet. At 3 inches, about 80 square feet."),
       ("How many bags of river rock make a yard?","Most bagged river rock is 0.5 cubic feet, so a cubic yard is 54 bags."),
       ("Should I put landscape fabric under river rock?","Usually yes. Fabric keeps rock from sinking into the soil and slows weeds, though some weeds will still root in debris that collects on top.")],
  supplies=["river rock","landscape fabric","landscape edging","fabric landscape staples"],
  related=["gravel-calculator","decomposed-granite-calculator","mulch-calculator"],
 ),

 dict(
  slug="decomposed-granite-calculator",
  kind="dg",
  group="Stone & hardscape",
  name="Decomposed Granite Calculator",
  short="Loose DG to order for a compacted path or patio.",
  title="Decomposed Granite Calculator: Yards, Tons, Bags",
  desc="Free decomposed granite calculator. Enter area, finished depth and compaction to get the loose cubic yards, tons and bags of DG to order for a path or patio.",
  h1="Decomposed granite calculator",
  lede="Decomposed granite shrinks when you compact it, so you need to order more loose material than the finished depth suggests. This calculator does that conversion for you.",
  area=True,
  waste=5,
  fields=[
    dict(id="depth", label="Finished depth (compacted)", unit="in", value=3, step=0.5, hint="2-3 in for paths, 3-4 in for patios"),
    dict(id="comp", label="Compaction", unit="%", value=20, step=1, hint="DG loses about 20-25% of its loose volume when compacted"),
    dict(id="price", label="Price per ton", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const c=Math.min(v.comp,90)/100, fin=v.area*v.depth/12, ft3=fin/(1-c), yd=ft3/27, tons=yd*1.35;
      const rows=[["Weight (approx.)",h.f(tons,2)+" tons"],["Loose cubic feet",h.f(ft3,1)],["Compacted volume",h.f(fin/27,2)+" cu yd"],
        ["0.5 cu ft bags",h.c(ft3/0.5)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards to order"], rows,
        note:"Weight uses about 1.35 tons (2,700 lb) per loose cubic yard. Confirm with your supplier." }; }""",
  table_head=["Project","Finished depth","Base underneath"],
  table=[["Garden path","2-3 in","Optional, 2-4 in on soft soil"],["Patio or seating area","3-4 in","2-4 in crushed base"],["Busy walkway","3-4 in","4 in crushed base"],["Driveway","4-6 in","4-6 in crushed base"]],
  table_title="How deep should decomposed granite be?",
  how="""<p>Decomposed granite (DG) is sold loose, but you measure the job by its compacted depth. The calculator works back from the finished depth to the loose volume to order.</p>
<p><b>Compacted cu ft</b> = area (sq ft) x finished depth (in) / 12<br>
<b>Loose cu ft</b> = compacted cu ft / (1 - compaction %)<br>
<b>Tons</b> = loose cubic yards x 1.35</p>
<p>Example: a 200 sq ft path with 5% extra is 210 sq ft. At 3 inches finished depth that is 52.5 cubic feet compacted. With 20% compaction you need 52.5 / 0.8 = 65.6 cubic feet loose, or 2.43 cubic yards, about 3.3 tons. In bags that is 132 half-cubic-foot bags.</p>
<p>DG compacts more or less depending on how fine it is, how damp it is, and how hard you tamp it. Plan on 20 to 25% with a plate compactor. Lay it in 1 to 2 inch lifts, mist each lift, and compact before adding the next. Stabilized DG compacts in a similar way but is harder once cured.</p>""",
  faq=[("How much does a yard of decomposed granite weigh?","About 1.35 tons, or 2,700 pounds, loose. Damp DG weighs more."),
       ("How much does decomposed granite compact?","Roughly 20 to 25% by volume with a plate compactor, so 3 inches of loose DG ends up around 2.25 to 2.4 inches."),
       ("How deep should a decomposed granite path be?","About 2 to 3 inches compacted for a garden path and 3 to 4 inches for patios or busy walkways, ideally over a compacted crushed base."),
       ("Do I need edging for decomposed granite?","Yes. Steel, aluminum or paver edging keeps DG from migrating into lawns and beds and helps it hold its compacted shape.")],
  supplies=["decomposed granite","plate compactor rental","steel landscape edging","DG stabilizer","landscape fabric"],
  related=["gravel-calculator","river-rock-calculator","paver-base-calculator"],
 ),

 dict(
  slug="fence-post-concrete-calculator",
  kind="fencepost",
  group="Concrete",
  name="Fence Post Concrete Calculator",
  short="Bags of concrete to set fence posts.",
  title="Fence Post Concrete Calculator: Bags Per Post",
  desc="Free fence post concrete calculator. Enter post count, hole size and post size to get the concrete per hole and the number of 50, 60 or 80 lb bags to buy.",
  h1="Fence post concrete calculator",
  lede="Enter how many posts you are setting and the size of each hole. The calculator subtracts the post and the gravel at the bottom to give the concrete and bags you need.",
  area=False,
  waste=None,
  fields=[
    dict(id="posts", label="Number of posts", unit="posts", value=10, step=1),
    dict(id="dia", label="Hole diameter", unit="in", value=10, step=0.5, hint="About 3 x post width: 10-12 in for a 4x4"),
    dict(id="depth", label="Hole depth", unit="in", value=30, step=1, hint="1/3 to 1/2 of the post's height above ground, below frost line"),
    dict(id="gravel", label="Gravel at bottom", unit="in", value=6, step=1, hint="About 6 in of gravel for drainage"),
    dict(id="post", label="Post size", type="select", value=3.5, options=[[3.5,"4x4 wood (3.5 x 3.5 in)"],[5.5,"6x6 wood (5.5 x 5.5 in)"],[2.375,"Chain link terminal, 2-3/8 in round"],[1.625,"Chain link line, 1-5/8 in round"]]),
    dict(id="bag", label="Bag size", type="select", value=0.375, options=[[0.375,"50 lb fast-setting (0.375 cu ft)"],[0.45,"60 lb concrete mix (0.45 cu ft)"],[0.6,"80 lb concrete mix (0.60 cu ft)"]]),
    dict(id="price", label="Price per bag", unit="$", optional=True),
  ],
  js="""(v,h)=>{ const cd=Math.max(v.depth-v.gravel,0), r=v.dia/2;
      const pa=v.post<3?Math.PI*Math.pow(v.post/2,2):v.post*v.post;
      const per=Math.max(Math.PI*r*r-pa,0)*cd/1728, tot=per*v.posts;
      const bp=v.bag>0?per/v.bag:0, bags=v.bag>0?Math.ceil(tot/v.bag-1e-9):0;
      const gr=Math.PI*r*r*Math.min(v.gravel,v.depth)/1728*v.posts;
      const rows=[["Concrete per post",h.f(per,2)+" cu ft"],["Bags per post",h.f(bp,1)],["Total concrete",h.f(tot,2)+" cu ft"],
        ["Gravel for hole bottoms",h.f(gr,2)+" cu ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(bags*v.price,2)]);
      return {big:[h.c(bags),"bags of concrete"], rows,
        note:"Concrete fills the hole above the gravel, minus the post. Add a bag or two for spills and oversized holes." }; }""",
  table_head=["Post","Hole diameter","Typical depth (6 ft fence)"],
  table=[["4x4 wood","10-12 in","24-36 in"],["6x6 wood","16-18 in","30-36 in"],["Chain link terminal, 2-3/8 in","8-10 in","30-36 in"],["Chain link line, 1-5/8 in","6-8 in","24-30 in"]],
  table_title="Fence post hole sizes",
  how="""<p>Each hole is a cylinder. The calculator takes the part above the gravel layer, subtracts the space the post takes up, and divides by the yield of one bag.</p>
<p><b>Concrete per hole (cu in)</b> = (3.1416 x (diameter / 2)<sup>2</sup> - post area) x (hole depth - gravel depth)<br>
<b>Cubic feet</b> = cubic inches / 1,728<br>
<b>Bags</b> = total cubic feet / bag yield</p>
<p>Example: a 10 in hole 30 in deep with 6 in of gravel leaves 24 in of concrete. The hole holds 3.1416 x 25 x 24 = 1,885 cu in, and a 4x4 post (3.5 x 3.5 in) takes 294 cu in, leaving 1,591 cu in, or 0.92 cu ft. That is about 2.5 bags of 50 lb fast-setting mix per post, or 25 bags for 10 posts.</p>
<p>Bag yields assumed: 50 lb fast-setting mix about 0.375 cu ft, 60 lb concrete mix about 0.45 cu ft, and 80 lb about 0.60 cu ft. A common rule is a hole about three times the post width, buried one third to one half of the post's height above ground, and below your frost line.</p>""",
  faq=[("How many bags of concrete per fence post?","For a 4x4 post in a 10 in hole with 24 in of concrete, about 2.5 bags of 50 lb fast-setting mix or about 1.5 bags of 80 lb mix."),
       ("How big should a fence post hole be?","About three times the post width across, so 10 to 12 inches for a 4x4. Depth should be one third to one half of the post's height above ground, and below the frost line."),
       ("Do I need gravel under a fence post?","It helps. About 6 inches of gravel at the bottom lets water drain away from the end of a wood post, which slows rot."),
       ("Can I pour fast-setting concrete in dry?","Fast-setting mix is made to be poured dry into the hole and then soaked with about a gallon of water per 50 lb bag. It sets in roughly 20 to 40 minutes.")],
  supplies=["fast-setting concrete mix","post hole digger","fence post level","gravel"],
  related=["concrete-calculator","gravel-calculator","retaining-wall-block-calculator"],
 ),
]
