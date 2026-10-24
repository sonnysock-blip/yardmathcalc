(function(){const R={};
R["mulch"]=((v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,bags=Math.ceil(ft3/2);const rows=[["Cubic feet",h.f(ft3,1)],["2 cu ft bags",h.c(ft3/2)],["3 cu ft bags",h.c(ft3/3)],["Area covered",h.c(v.area)+" sq ft"]];let note="";
if(v.bulk)rows.push(["Bulk cost","$"+h.f(yd*v.bulk,2)]);if(v.bag)rows.push(["Bagged cost","$"+h.f(bags*v.bag,2)]);
if(v.bulk&&v.bag){const d=bags*v.bag-yd*v.bulk;note=d>0?"Bulk saves about $"+h.f(d,0)+" before delivery fees.":"Bags save about $"+h.f(-d,0)+" and need no delivery.";}
return{big:[h.f(yd,2),"cubic yards"],rows,note};});
R["gravel"]=((v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,t=yd*1.4;const rows=[["Weight (approx.)",h.f(t,2)+" tons"],["Cubic feet",h.f(ft3,1)],["0.5 cu ft bags",h.c(ft3/0.5)],["Area covered",h.c(v.area)+" sq ft"]];
if(v.price)rows.push(["Estimated cost","$"+h.f(t*v.price,2)]);return{big:[h.f(yd,2),"cubic yards"],rows,note:"Weight assumes about 1.4 tons per cubic yard."};});
R["topsoil"]=((v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,bags=Math.ceil(ft3/0.75);const rows=[["Weight (approx.)",h.f(yd*1.1,2)+" tons"],["Cubic feet",h.f(ft3,1)],["0.75 cu ft bags",h.c(ft3/0.75)],["1 cu ft bags",h.c(ft3)]];let note="";
if(v.bulk)rows.push(["Bulk cost","$"+h.f(yd*v.bulk,2)]);if(v.bag)rows.push(["Bagged cost","$"+h.f(bags*v.bag,2)]);
if(v.bulk&&v.bag){const d=bags*v.bag-yd*v.bulk;note=d>0?"Bulk saves about $"+h.f(d,0)+" before delivery fees.":"Bags save about $"+h.f(-d,0)+" and need no delivery.";}
return{big:[h.f(yd,2),"cubic yards"],rows,note};});
R["concrete"]=((v,h)=>{const ft3=v.area*v.depth/12,yd=ft3/27,b80=Math.ceil(ft3/0.6);const rows=[["Cubic feet",h.f(ft3,1)],["80 lb bags",h.c(ft3/0.6)],["60 lb bags",h.c(ft3/0.45)],["40 lb bags",h.c(ft3/0.3)]];let note="Bag yields: 80 lb ≈ 0.60 cu ft, 60 lb ≈ 0.45, 40 lb ≈ 0.30.";
if(v.bag)rows.push(["Cost in 80 lb bags","$"+h.f(b80*v.bag,2)]);if(v.ready)rows.push(["Ready-mix cost","$"+h.f(yd*v.ready,2)]);
if(v.bag&&v.ready)note=(b80*v.bag>yd*v.ready?"Ready-mix is cheaper before short-load and delivery fees.":"Bags are cheaper, but mixing "+b80+" bags is a big job.");
return{big:[h.f(yd,2),"cubic yards"],rows,note};});
R["sod"]=((v,h)=>{const rows=[["Sod pieces (16 x 24 in)",h.c(v.area/2.667)],["Pallets (450 sq ft)",h.f(v.area/450,2)],["Large rolls (100 sq ft)",h.c(v.area/100)]];
if(v.price)rows.push(["Estimated cost","$"+h.f(v.area*v.price,2)]);return{big:[h.c(v.area),"square feet"],rows,note:"Pallet sizes vary from about 400 to 500 sq ft by farm."};});
R["paverbase"]=((v,h)=>{ const c=Math.min(v.comp,90)/100;
      const yd=v.area*v.base/12/27/(1-c), ft3=yd*27, tons=yd*1.4;
      const sand=v.area*v.sand/12, pa=v.plen*v.pwid, n=pa>0?v.area*144/pa:0;
      const rows=[["Base stone (tons, approx.)",h.f(tons,2)],["Base stone, 0.5 cu ft bags",h.c(ft3/0.5)],
        ["Bedding sand (cu ft)",h.f(sand,1)],["Bedding sand, 0.5 cu ft bags",h.c(sand/0.5)],
        ["Pavers",h.c(n)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of base"], rows,
        note:"Base volume is loose stone to order, at about 1.4 tons per cubic yard. Paver count uses the extra % entered above." }; });
R["wallblock"]=((v,h)=>{ const per=v.blen>0?Math.ceil(v.len*12/v.blen):0;
      const exp=v.bht>0?Math.ceil(v.ht*12/v.bht):0, courses=exp+(exp>0&&v.bury?1:0), total=per*courses;
      const caps=v.cap>0?Math.ceil(v.len*12/v.cap):0, hft=courses*v.bht/12;
      const back=v.len*1*hft/27, pad=v.len*2*0.5/27;
      const rows=[["Blocks per course",h.c(per)],["Courses",h.c(courses)+(v.bury&&exp>0?" (1 buried)":"")],
        ["Cap blocks",h.c(caps)],["Drainage gravel, 12 in behind wall",h.f(back,2)+" cu yd"],
        ["Leveling base, 6 in x 24 in trench",h.f(pad,2)+" cu yd"]];
      const cost=total*v.price+caps*v.capprice;
      if(cost>0) rows.push(["Estimated cost","$"+h.f(cost,2)]);
      return {big:[h.c(total),"wall blocks"], rows,
        note:(v.ht>3?"Walls over about 3 ft usually need larger blocks, geogrid, or an engineer; check local code. ":"")+"Buy a few spare blocks for cuts and breakage." }; });
R["riverrock"]=((v,h)=>{ const ft3=v.area*v.depth/12, yd=ft3/27, tons=yd*1.35;
      const rows=[["Weight (approx.)",h.f(tons,2)+" tons"],["Cubic feet",h.f(ft3,1)],["0.5 cu ft bags",h.c(ft3/0.5)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards"], rows,
        note:"Weight uses about 1.35 tons per cubic yard; river rock runs about 1.3 to 1.4." }; });
R["dg"]=((v,h)=>{ const c=Math.min(v.comp,90)/100, fin=v.area*v.depth/12, ft3=fin/(1-c), yd=ft3/27, tons=yd*1.35;
      const rows=[["Weight (approx.)",h.f(tons,2)+" tons"],["Loose cubic feet",h.f(ft3,1)],["Compacted volume",h.f(fin/27,2)+" cu yd"],
        ["0.5 cu ft bags",h.c(ft3/0.5)],["Area incl. extra",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards to order"], rows,
        note:"Weight uses about 1.35 tons (2,700 lb) per loose cubic yard. Confirm with your supplier." }; });
R["fencepost"]=((v,h)=>{ const cd=Math.max(v.depth-v.gravel,0), r=v.dia/2;
      const pa=v.post<3?Math.PI*Math.pow(v.post/2,2):v.post*v.post;
      const per=Math.max(Math.PI*r*r-pa,0)*cd/1728, tot=per*v.posts;
      const bp=v.bag>0?per/v.bag:0, bags=v.bag>0?Math.ceil(tot/v.bag-1e-9):0;
      const gr=Math.PI*r*r*Math.min(v.gravel,v.depth)/1728*v.posts;
      const rows=[["Concrete per post",h.f(per,2)+" cu ft"],["Bags per post",h.f(bp,1)],["Total concrete",h.f(tot,2)+" cu ft"],
        ["Gravel for hole bottoms",h.f(gr,2)+" cu ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(bags*v.price,2)]);
      return {big:[h.c(bags),"bags of concrete"], rows,
        note:"Concrete fills the hole above the gravel, minus the post. Add a bag or two for spills and oversized holes." }; });
R["raisedbed"]=((v,h)=>{ const ft3=v.len*v.wid*(v.ht/12)*v.beds*(1+v.settle/100); const yd=ft3/27;
      const mixes={1:[["Topsoil",0.6],["Compost",0.4]],2:[["Topsoil",0.5],["Compost",0.5]],
        3:[["Compost",1/3],["Peat moss",1/3],["Coarse vermiculite",1/3]],4:[["Raised bed mix",1]]};
      const parts=mixes[v.mix]||mixes[1];
      const rows=[["Total cubic feet",h.f(ft3,1)]];
      parts.forEach(p=>rows.push([p[0],h.f(ft3*p[1],1)+" cu ft ("+h.f(ft3*p[1]/27,2)+" cu yd)"]));
      rows.push(["1 cu ft bags (total)",h.c(ft3)]);
      rows.push(["1.5 cu ft bags (total)",h.c(ft3/1.5)]);
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(yd*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of soil"], rows:rows,
        note:"Bag counts assume every ingredient comes in that bag size. Compressed peat moss bales expand, so check the loose volume on the label."}; });
R["compost"]=((v,h)=>{ const ft3=v.area*v.depth/12; const yd=ft3/27;
      const rows=[["Cubic feet",h.f(ft3,1)],["1 cu ft bags",h.c(ft3)],["0.75 cu ft bags",h.c(ft3/0.75)],["Area covered",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(yd*v.price,2)]);
      return {big:[h.f(yd,2),"cubic yards of compost"], rows:rows,
        note:"Many 40 lb bags of compost hold about 0.75 cu ft. Check the volume printed on the bag."}; });
R["grassseed"]=((v,h)=>{ const rate=v.seed*v.job; const lb=v.area/1000*rate;
      const rows=[["Seeding rate",h.f(rate,2)+" lb per 1,000 sq ft"],["3 lb bags",h.c(lb/3)],["7 lb bags",h.c(lb/7)],["20 lb bags",h.c(lb/20)],["Area seeded",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(lb*v.price,2)]);
      return {big:[h.f(lb,1),"pounds of seed"], rows:rows,
        note:"Rates are typical midpoints for pure seed. Mixes and coated seed differ, so follow the rate on your bag if it gives one."}; });
R["fertilizer"]=((v,h)=>{ const per=v.n>0?v.rate/(v.n/100):0; const lb=per*v.area/1000; const bags=v.bag>0?lb/v.bag:0;
      const rows=[["Product per 1,000 sq ft",h.f(per,2)+" lb"],["Bags needed",h.c(bags)],["Nitrogen applied (total)",h.f(v.rate*v.area/1000,2)+" lb"],["Area fed",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(Math.ceil(bags)*v.price,2)]);
      return {big:[h.f(lb,1),"pounds of fertilizer"], rows:rows,
        note:"The product label's rate and spreader setting take priority over this estimate."}; });
R["deckstain"]=((v,h)=>{ const floor=v.len*v.wid; const rail=v.rail*v.railh*2; const stairs=v.steps*5;
      const sq=floor+rail+stairs; const per=v.cov>0?sq/v.cov:0; const gal=per*v.coats;
      let fives=Math.floor(gal/5); let ones=Math.ceil(gal-fives*5-1e-9);
      if(ones>=4){fives+=1;ones=0;}
      const rows=[["Square feet to cover",h.c(sq)],["Floor",h.c(floor)+" sq ft"],["Railing (both sides)",h.c(rail)+" sq ft"],["Stairs",h.c(stairs)+" sq ft"],
        ["Gallons per coat",h.f(per,2)],["Cans to buy",fives+" x 5 gal + "+ones+" x 1 gal"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(gal*v.price,2)]);
      return {big:[h.f(gal,1),"gallons of stain"], rows:rows,
        note:"Coverage is for rough or weathered wood; smooth new boards take less, and a second coat often goes further than the first. When 4 or more extra gallons are needed, the can mix rounds up to another 5 gallon pail."}; });
R["bagstoyards"]=((v,h)=>{ const ft3=v.bags*v.size, yd=ft3/27;
      const rows=[["Cubic feet",h.f(ft3,1)],["Bags in one cubic yard",v.size>0?h.f(27/v.size,1):"0"]];
      if(v.bag>0) rows.push(["Bagged cost","$"+h.f(v.bags*v.bag,2)]);
      if(v.bulk>0) rows.push(["Bulk cost, same volume","$"+h.f(yd*v.bulk,2)]);
      let note="A cubic yard is 27 cubic feet. Check the volume printed on the bag, since sizes vary by brand.";
      if(v.bag>0&&v.bulk>0){ const d=v.bags*v.bag-yd*v.bulk;
        note=d>0?"Bulk is about $"+h.f(d,0)+" cheaper before delivery fees.":"Bags are about $"+h.f(-d,0)+" cheaper and need no delivery."; }
      return {big:[h.f(yd,2),"cubic yards"], rows:rows, note:note}; });
R["yardstotons"]=((v,h)=>{ const d=[0,2800,2800,2200,1000,500][v.m]||0; const lbyd=v.custom>0?v.custom:d;
      const lb=v.yd*lbyd, tons=lb/2000;
      const rows=[["Pounds",h.c(lb)],["Metric tons",h.f(tons*0.907185,2)],["Density used",h.c(lbyd)+" lb per cu yd"],["Tons per cubic yard",h.f(lbyd/2000,2)]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(tons*v.price,2)]);
      return {big:[h.f(tons,2),"US tons"], rows:rows, note:"Weights are approximate and rise when material is wet or compacted. Tons here are US short tons of 2,000 lb."}; });
R["lime"]=((v,h)=>{ const prod=v.cce>0?v.req/(v.cce/100):0; const total=prod*v.area/1000;
      const apps=prod>0?Math.ceil(prod/50):0; const bags=v.bag>0?Math.ceil(total/v.bag):0;
      const rows=[["Lime per 1,000 sq ft",h.f(prod,1)+" lb"],["Applications (max 50 lb per 1,000 sq ft each)",String(apps)],
        ["Per application",apps>0?h.f(prod/apps,1)+" lb per 1,000 sq ft":"0"],["Bags needed",String(bags)],["Area limed",h.c(v.area)+" sq ft"]];
      if(v.price>0) rows.push(["Estimated cost","$"+h.f(bags*v.price,2)]);
      return {big:[h.f(total,0),"pounds of lime"], rows:rows, note:"Follow your soil test and the product label first. Brand rates on bags can differ from this general calculation."}; });

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
})();
