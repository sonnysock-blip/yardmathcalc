# The original five calculators, in the shared tool format (see SPEC.md).
TOOLS = [{'slug': 'mulch-calculator',
  'kind': 'mulch',
  'name': 'Mulch Calculator',
  'short': 'How many yards or bags of mulch for your beds.',
  'title': 'Mulch Calculator: Cubic Yards and Bags Needed',
  'desc': 'Free mulch calculator. Enter your bed size and depth to get cubic yards, 2 cu ft and 3 cu ft bag counts, '
          'and a cost estimate.',
  'h1': 'Mulch calculator',
  'lede': 'Measure your beds, pick a depth, and get the cubic yards to order or the number of bags to load in the car.',
  'table': [['Flower and shrub beds', '2–3 in', '108–162 sq ft'],
            ['Weed suppression', '3–4 in', '81–108 sq ft'],
            ['Around trees (keep off the trunk)', '2–4 in', '81–162 sq ft'],
            ['Paths and play areas', '3–4 in', '81–108 sq ft']],
  'table_head': ['Use', 'Depth', '1 cu yd covers'],
  'how': "<p>Mulch is sold by volume, so the calculator turns your bed's area into cubic feet and then into cubic "
         'yards, the unit bulk suppliers use.</p>\n'
         '<p><b>Cubic feet</b> = length (ft) × width (ft) × depth (in) ÷ 12<br><b>Cubic yards</b> = cubic feet ÷ '
         '27</p>\n'
         '<p>A bed 20 ft long and 10 ft wide at 3 inches deep holds 50 cubic feet, which is about 1.85 cubic yards or '
         '25 two-cubic-foot bags.</p>\n'
         '<p>Bulk mulch is usually cheaper once you need more than two or three yards. Bags make sense for small beds '
         'and for top-ups.</p>',
  'faq': [('How many bags of mulch are in a yard?',
           'A cubic yard is 27 cubic feet, so it equals 13.5 bags of 2 cubic feet or 9 bags of 3 cubic feet.'),
          ('How much area does a yard of mulch cover?',
           'At 3 inches deep, one cubic yard covers about 108 square feet. At 2 inches it covers about 162 square '
           'feet.'),
          ('Should I remove old mulch first?',
           'Not usually. If the old layer is still 1–2 inches deep, add only enough to bring the total back to 3 '
           'inches, and rake it loose first.'),
          ('How much extra should I order?',
           'Add 5–10% for uneven ground and settling. Use the extra percentage field above.')],
  'table_title': 'How deep should mulch be?',
  'group': 'Mulch & soil',
  'area': True,
  'waste': 5,
  'dims': (20, 10),
  'fields': [{'id': 'depth',
              'label': 'Depth',
              'unit': 'in',
              'value': 3,
              'step': 0.25,
              'hint': '2–3 in for beds, 3–4 in to smother weeds'},
             {'id': 'bulk', 'label': 'Bulk price per cubic yard', 'unit': '$', 'optional': True},
             {'id': 'bag', 'label': 'Price per 2 cu ft bag', 'unit': '$', 'optional': True}],
  'js': '(v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,bags=Math.ceil(ft3/2);const rows=[["Cubic feet",h.f(ft3,1)],["2 '
        'cu ft bags",h.c(ft3/2)],["3 cu ft bags",h.c(ft3/3)],["Area covered",h.c(v.area)+" sq ft"]];let note="";\n'
        'if(v.bulk)rows.push(["Bulk cost","$"+h.f(yd*v.bulk,2)]);if(v.bag)rows.push(["Bagged '
        'cost","$"+h.f(bags*v.bag,2)]);\n'
        'if(v.bulk&&v.bag){const d=bags*v.bag-yd*v.bulk;note=d>0?"Bulk saves about $"+h.f(d,0)+" before delivery '
        'fees.":"Bags save about $"+h.f(-d,0)+" and need no delivery.";}\n'
        'return{big:[h.f(yd,2),"cubic yards"],rows,note};}',
  'supplies': ['landscape fabric', 'bed edging', 'garden rake', 'wheelbarrow'],
  'related': ['topsoil-calculator', 'compost-calculator', 'raised-bed-soil-calculator']},
 {'slug': 'gravel-calculator',
  'kind': 'gravel',
  'name': 'Gravel Calculator',
  'short': 'Cubic yards and tons of gravel for paths and driveways.',
  'title': 'Gravel Calculator: Cubic Yards and Tons Needed',
  'desc': 'Free gravel calculator. Get cubic yards, tons and bag counts for driveways, paths and patios from your '
          'length, width and depth.',
  'h1': 'Gravel calculator',
  'lede': 'Work out how much gravel or crushed stone to order, in cubic yards and in tons, since many quarries sell by '
          'weight.',
  'table': [['Garden paths', '2–3 in'],
            ['Patio or paver base', '4 in'],
            ['Driveway (new)', '4–6 in, in layers'],
            ['Driveway (refresh)', '1–2 in']],
  'table_head': ['Project', 'Depth'],
  'how': '<p>The calculator finds the volume of your area, converts it to cubic yards, and estimates weight at about '
         '1.4 tons per cubic yard, a common figure for pea gravel and crushed stone.</p>\n'
         '<p><b>Cubic yards</b> = length (ft) × width (ft) × depth (in) ÷ 12 ÷ 27<br><b>Tons</b> ≈ cubic yards × '
         '1.4</p>\n'
         '<p>Density varies with stone size and moisture, roughly 1.3 to 1.5 tons per cubic yard. Ask your supplier '
         'for their figure if you are ordering by the ton.</p>',
  'faq': [('How many tons of gravel are in a cubic yard?',
           'Roughly 1.3 to 1.5 tons. This calculator uses 1.4 tons per cubic yard.'),
          ('How much gravel do I need for a driveway?',
           'A new gravel driveway usually needs 4–6 inches, laid as a coarse base and a finer top layer. A 12 × 50 ft '
           'driveway at 4 inches needs about 7.4 cubic yards.'),
          ('Should I use landscape fabric under gravel?',
           'For paths and patios it helps keep weeds down and stops stone sinking into soil. Many driveway builders '
           'skip it in favour of a thick compacted base.'),
          ('How many bags of gravel make a yard?',
           'Most bagged gravel is 0.5 cubic feet, so a cubic yard is about 54 bags.')],
  'table_title': 'How deep should gravel be?',
  'group': 'Stone & hardscape',
  'area': True,
  'waste': 5,
  'dims': (12, 40),
  'fields': [{'id': 'depth',
              'label': 'Depth',
              'unit': 'in',
              'value': 4,
              'step': 0.5,
              'hint': '2–3 in for paths, 4–6 in for driveways'},
             {'id': 'price', 'label': 'Price per ton', 'unit': '$', 'optional': True}],
  'js': '(v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,t=yd*1.4;const rows=[["Weight (approx.)",h.f(t,2)+" '
        'tons"],["Cubic feet",h.f(ft3,1)],["0.5 cu ft bags",h.c(ft3/0.5)],["Area covered",h.c(v.area)+" sq ft"]];\n'
        'if(v.price)rows.push(["Estimated cost","$"+h.f(t*v.price,2)]);return{big:[h.f(yd,2),"cubic '
        'yards"],rows,note:"Weight assumes about 1.4 tons per cubic yard."};}',
  'supplies': ['landscape fabric', 'steel landscape edging', 'hand tamper', 'gravel rake'],
  'related': ['paver-base-calculator', 'river-rock-calculator', 'decomposed-granite-calculator']},
 {'slug': 'topsoil-calculator',
  'kind': 'topsoil',
  'name': 'Topsoil Calculator',
  'short': 'Soil for new lawns, raised beds and leveling.',
  'title': 'Topsoil Calculator: Cubic Yards, Tons and Bags',
  'desc': 'Free topsoil calculator for lawns, garden beds and raised beds. Get cubic yards, approximate tons and bag '
          'counts.',
  'h1': 'Topsoil calculator',
  'lede': 'Find out how much topsoil or garden soil you need for a new lawn, a raised bed, or filling low spots.',
  'table': [['Top-dressing a lawn', '¼–½ in'],
            ['New lawn from seed or sod', '4–6 in'],
            ['New vegetable bed', '6–8 in'],
            ['Raised bed', 'Full bed depth']],
  'table_head': ['Project', 'Depth'],
  'how': '<p>Topsoil is sold by the cubic yard in bulk or in bags of 0.75 or 1 cubic foot. The calculator gives all '
         'three, plus a weight estimate of about 1.1 tons per cubic yard for dry soil.</p>\n'
         '<p><b>Cubic yards</b> = length (ft) × width (ft) × depth (in) ÷ 12 ÷ 27</p>\n'
         "<p>For a raised bed, use the bed's inside length and width and its full height as the depth. Fresh soil "
         'settles, so order 10–15% extra for beds.</p>',
  'faq': [('How many bags of topsoil are in a yard?', 'About 36 bags of 0.75 cubic feet, or 27 bags of 1 cubic foot.'),
          ('How much does a yard of topsoil weigh?',
           'Roughly 1 to 1.3 tons, depending on moisture. Wet soil is heavier.'),
          ('Is it cheaper to buy topsoil in bulk?',
           'Usually, once you need more than about one cubic yard. Delivery fees can tip the balance for small '
           'orders.'),
          ('How much soil for a 4 × 8 raised bed?',
           'A 4 × 8 ft bed that is 12 inches deep holds 32 cubic feet, about 1.2 cubic yards.')],
  'table_title': 'How much topsoil do you need?',
  'group': 'Mulch & soil',
  'area': True,
  'waste': 5,
  'dims': (30, 20),
  'fields': [{'id': 'depth',
              'label': 'Depth',
              'unit': 'in',
              'value': 4,
              'step': 0.25,
              'hint': '4–6 in for a new lawn; full depth for raised beds'},
             {'id': 'bulk', 'label': 'Bulk price per cubic yard', 'unit': '$', 'optional': True},
             {'id': 'bag', 'label': 'Price per 0.75 cu ft bag', 'unit': '$', 'optional': True}],
  'js': '(v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,bags=Math.ceil(ft3/0.75);const rows=[["Weight '
        '(approx.)",h.f(yd*1.1,2)+" tons"],["Cubic feet",h.f(ft3,1)],["0.75 cu ft bags",h.c(ft3/0.75)],["1 cu ft '
        'bags",h.c(ft3)]];let note="";\n'
        'if(v.bulk)rows.push(["Bulk cost","$"+h.f(yd*v.bulk,2)]);if(v.bag)rows.push(["Bagged '
        'cost","$"+h.f(bags*v.bag,2)]);\n'
        'if(v.bulk&&v.bag){const d=bags*v.bag-yd*v.bulk;note=d>0?"Bulk saves about $"+h.f(d,0)+" before delivery '
        'fees.":"Bags save about $"+h.f(-d,0)+" and need no delivery.";}\n'
        'return{big:[h.f(yd,2),"cubic yards"],rows,note};}',
  'supplies': ['garden soil', 'lawn leveling rake', 'wheelbarrow', 'soil test kit'],
  'related': ['raised-bed-soil-calculator', 'compost-calculator', 'sod-calculator']},
 {'slug': 'concrete-calculator',
  'kind': 'concrete',
  'name': 'Concrete Calculator',
  'short': 'Bags or yards of concrete for a slab or pad.',
  'title': 'Concrete Slab Calculator: Bags and Cubic Yards',
  'desc': 'Free concrete calculator for slabs, patios and pads. Get cubic yards and the number of 80 lb or 60 lb bags '
          'to buy.',
  'h1': 'Concrete calculator',
  'lede': 'Size a patio, shed pad or walkway and see whether to buy bags or order ready-mix by the yard.',
  'table': [['Walkway or patio', '4 in'],
            ['Shed or hot tub pad', '4–6 in'],
            ['Driveway', '5–6 in'],
            ['Garage floor', '4–6 in']],
  'table_head': ['Project', 'Thickness'],
  'how': '<p>The calculator multiplies area by thickness for the volume, then divides by the yield of each bag size: '
         'an 80 lb bag makes about 0.60 cubic feet and a 60 lb bag about 0.45 cubic feet.</p>\n'
         '<p><b>Cubic yards</b> = length (ft) × width (ft) × thickness (in) ÷ 12 ÷ 27</p>\n'
         '<p>Forms flex and ground is never perfectly flat, so the extra field defaults to 10%. Above about one cubic '
         'yard, ready-mix delivery is usually less work and often cheaper than bags.</p>',
  'faq': [('How many 80 lb bags of concrete make a yard?', 'About 45 bags of 80 lb, or 60 bags of 60 lb.'),
          ('How many bags for a 10 × 10 slab?',
           'At 4 inches thick, a 10 × 10 slab is about 1.23 cubic yards: roughly 56 bags of 80 lb before adding '
           'extra.'),
          ('Should I buy bags or ready-mix?',
           'Bags suit small jobs under about one cubic yard. Larger pours are easier with a truck, which also gives a '
           'more even mix.'),
          ('Does this include gravel base?',
           'No. Use the gravel calculator for the 4 inch compacted base most slabs sit on.')],
  'table_title': 'How thick should a slab be?',
  'group': 'Concrete',
  'area': True,
  'waste': 10,
  'dims': (10, 10),
  'fields': [{'id': 'depth',
              'label': 'Thickness',
              'unit': 'in',
              'value': 4,
              'step': 0.5,
              'hint': '4 in for patios and walks, 5–6 in for driveways'},
             {'id': 'bag', 'label': 'Price per 80 lb bag', 'unit': '$', 'optional': True},
             {'id': 'ready', 'label': 'Ready-mix price per cubic yard', 'unit': '$', 'optional': True}],
  'js': '(v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,b80=Math.ceil(ft3/0.6);const rows=[["Cubic '
        'feet",h.f(ft3,1)],["80 lb bags",h.c(ft3/0.6)],["60 lb bags",h.c(ft3/0.45)],["40 lb bags",h.c(ft3/0.3)]];let '
        'note="Bag yields: 80 lb ≈ 0.60 cu ft, 60 lb ≈ 0.45, 40 lb ≈ 0.30.";\n'
        'if(v.bag)rows.push(["Cost in 80 lb bags","$"+h.f(b80*v.bag,2)]);if(v.ready)rows.push(["Ready-mix '
        'cost","$"+h.f(yd*v.ready,2)]);\n'
        'if(v.bag&&v.ready)note=(b80*v.bag>yd*v.ready?"Ready-mix is cheaper before short-load and delivery '
        'fees.":"Bags are cheaper, but mixing "+b80+" bags is a big job.");\n'
        'return{big:[h.f(yd,2),"cubic yards"],rows,note};}',
  'supplies': ['concrete mixer rental', 'wood stakes and form boards', 'bull float', 'rebar or wire mesh'],
  'related': ['gravel-calculator', 'fence-post-concrete-calculator', 'paver-base-calculator']},
 {'slug': 'sod-calculator',
  'kind': 'sod',
  'name': 'Sod Calculator',
  'short': 'Pieces and pallets of sod for a new lawn.',
  'title': 'Sod Calculator: Square Feet, Pieces and Pallets',
  'desc': 'Free sod calculator. Enter your lawn size to see how many square feet, sod pieces and pallets to order, '
          'with extra for cuts.',
  'h1': 'Sod calculator',
  'lede': 'Measure the lawn, add a little extra for trimming around edges, and see how many pieces and pallets to '
          'order.',
  'table': [['Standard piece', '16 × 24 in', '2.67 sq ft'],
            ['Pallet (typical)', 'about 170 pieces', '400–500 sq ft'],
            ['Large roll', '2 × 50 ft', '100 sq ft']],
  'table_head': ['Unit', 'Size', 'Covers'],
  'how': '<p>Sod is sold by the square foot, by the piece or by the pallet. The calculator adds your extra percentage, '
         'then divides by a standard 16 × 24 inch piece (about 2.67 sq ft) and a 450 sq ft pallet.</p>\n'
         '<p>Pallet sizes vary by farm, usually from 400 to 500 square feet, so check with your supplier before '
         'ordering.</p>\n'
         '<p>Curved beds and lots of edges waste more sod. Use 5% for simple rectangles and 10% or more for curvy '
         'yards.</p>',
  'faq': [('How much sod is on a pallet?', 'Usually 400 to 500 square feet, often around 450. It depends on the farm.'),
          ('How much extra sod should I order?', '5% for simple shapes, 10–15% for curved beds and many obstacles.'),
          ('How fast do I need to lay sod?',
           'Within a day of delivery in warm weather. Sod left rolled in the heat starts to yellow quickly.'),
          ('Do I need topsoil under sod?',
           'Sod roots best in 4–6 inches of loose topsoil. Use the topsoil calculator to size that layer.')],
  'table_title': 'Sod sizes at a glance',
  'group': 'Lawn & garden',
  'area': True,
  'waste': 5,
  'dims': (40, 25),
  'fields': [{'id': 'price', 'label': 'Price per sq ft', 'unit': '$', 'optional': True, 'step': 0.01}],
  'js': '(v,h)=>{const rows=[["Sod pieces (16 x 24 in)",h.c(v.area/2.667)],["Pallets (450 sq '
        'ft)",h.f(v.area/450,2)],["Large rolls (100 sq ft)",h.c(v.area/100)]];\n'
        'if(v.price)rows.push(["Estimated cost","$"+h.f(v.area*v.price,2)]);return{big:[h.c(v.area),"square '
        'feet"],rows,note:"Pallet sizes vary from about 400 to 500 sq ft by farm."};}',
  'supplies': ['lawn roller rental', 'sod knife', 'oscillating sprinkler', 'starter fertilizer'],
  'related': ['topsoil-calculator', 'grass-seed-calculator', 'fertilizer-calculator']}]
