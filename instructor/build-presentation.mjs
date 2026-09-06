/**
 * Rebuild the teaching companion using the supplied O'Reilly PowerPoint template.
 * Usage: node build-presentation.mjs <template.pptx> <workspace> <revision>
 * Requires the bundled @oai/artifact-tool runtime and PRESENTATION_SKILL_DIR,
 * ARTIFACT_RUNTIME_PYTHON, RUNTIME_NODE_MODULES. The publisher template stays outside source control.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { FileBlob, Presentation, PresentationFile } from '@oai/artifact-tool';

const repo=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const [templateArg,workspaceArg,revision='v2']=process.argv.slice(2);
if(!templateArg||!workspaceArg||!process.env.PRESENTATION_SKILL_DIR||!process.env.ARTIFACT_RUNTIME_PYTHON||!process.env.RUNTIME_NODE_MODULES) throw new Error('Supply template, workspace, skill directory, bundled Python, and RUNTIME_NODE_MODULES.');
const template=path.resolve(templateArg),workspace=path.resolve(workspaceArg);
if(!/^[a-z0-9-]+$/i.test(revision)) throw new Error('Revision must contain only letters, digits, and hyphens.');
const skill=process.env.PRESENTATION_SKILL_DIR;
const buildDir=path.join(workspace,'work',`oreilly-${revision}`);
const output=path.join(workspace,'outputs',`copilot-studio-oreilly-${revision}.pptx`);
const ink='#161616',blue='#0345FF',pale='#F0F5FF';

function text(slide,value,x,y,w,h,size=22,bold=false,color=ink){
  const shape=slide.shapes.add({geometry:'textbox',name:value.slice(0,55),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  shape.text=value;shape.text.style={typeface:'Arial',fontSize:size,bold,color,autoFit:'none'};return shape;
}
function node(slide,label,x,y,w,h=82,options={}){
  // Diagram boundaries carry meaning; native nodes keep that evidence editable.
  const shape=slide.shapes.add({geometry:options.geometry??'rect',name:label,position:{left:x,top:y,width:w,height:h},fill:options.fill??'#FFFFFF',line:{fill:options.line??blue,width:2,style:options.dashed?'dashed':'solid'}});
  shape.text=label;shape.text.style={typeface:'Arial',fontSize:options.size??21,bold:!!options.bold,color:ink,alignment:'center',verticalAlignment:'middle',autoFit:'none'};return shape;
}
function arrow(slide,a,b,fromSide='right',toSide='left'){
  return slide.shapes.connect(a,b,{kind:'elbow',fromSide,toSide,line:{fill:ink,width:2},tail:{type:'arrow',width:'med',length:'med'}});
}
function rowFlow(slide,labels,{y=230,h=88,size=21}={}){
  const gap=25,w=(854-gap*(labels.length-1))/labels.length;
  const nodes=labels.map((label,i)=>node(slide,label,53+i*(w+gap),y,w,h,{size,fill:i===0?pale:'#FFFFFF'}));
  for(let i=0;i<nodes.length-1;i++)arrow(slide,nodes[i],nodes[i+1]);return nodes;
}
function diagram(slide,kind){
  if(kind==='anatomy'){
    text(slide,'Instructions guide behavior; identity and policy control access.',53,139,850,48,21);
    const u=node(slide,'User message\nthrough a channel',53,275,166,88);
    const o=node(slide,'Generative\norchestration',275,275,215,88,{fill:pale,bold:true});arrow(slide,u,o);
    for(const [label,y] of [['Knowledge\nreference material',184],['Topic\nauthored conversation',289],['Tool\na defined operation',394]])arrow(slide,o,node(slide,label,585,y,315,80));
  }else if(kind==='grounding'){
    rowFlow(slide,['Question','Retrieve\nrelevant passage','Generate\nan answer','Inspect answer\nand source'],{y:224});
    text(slide,'“Who patches the guest OS of Contoso’s Azure virtual machine?”',53,156,854,50,24);
    text(slide,'A citation supports inspection. It does not guarantee correctness.',53,368,854,75,24,true);
  }else if(kind==='wait'){
    const a=node(slide,'Message\nTeach the concept',53,252,180,88);
    const b=node(slide,'Question\nWAIT for a choice',290,252,230,88,{fill:pale,bold:true});arrow(slide,a,b);
    const c=node(slide,'Correct choice\nExplain why',630,161,270,80);
    const d=node(slide,'Incorrect choice\nExplain misconception',630,278,270,80);
    const e=node(slide,'Unmatched twice\nOffer recovery',630,395,270,80);for(const n of[c,d,e])arrow(slide,b,n);
    text(slide,'“Ask every time” collects new learner thinking.',53,400,485,65,21);
  }else if(kind==='contract'){
    rowFlow(slide,['Input: focus\ncloud | security | governance','GetStudySession\nnative agent flow','Outputs: status + plan\nBoth are Text'],{y:214,h:122,size:20});
    text(slide,'Valid focus → ok + reviewed 30-minute session',53,381,854,40,24,true);
    text(slide,'Unsupported focus → unsupported + choice reminder',53,429,854,40,22);
  }else if(kind==='flow'){
    rowFlow(slide,['Agent\ncalls flow','Initialize\nstatus / plan','If\ncloud','If\nsecurity','If\ngovernance','Respond\nonce'],{y:240,h:94,size:18});
    text(slide,'Three sequential conditions. Each supported match sets the result.',53,155,854,55,24);
    text(slide,'Default: unsupported. Assign variables inside a matching branch.',53,389,854,75,22);
  }else if(kind==='agents'){
    const parent=node(slide,'Parent agent',53,171,374,274,{fill:pale});
    // The parent caption is replaced so the child has its own readable region.
    parent.text='';text(slide,'Parent agent',75,186,325,45,26,true);
    const child=node(slide,'Child agent\nspecialized work',102,298,273,96);
    const connected=node(slide,'Connected agent\nseparately managed',566,251,338,118);
    arrow(slide,parent,connected);text(slide,'A2A: a protocol for agent communication',459,401,448,65,21);
    text(slide,'Concept only: possible extension. Our assistant stays one agent.',53,113,854,40,22,true);
    text(slide,'Connection awareness: Microsoft Foundry, Fabric, Microsoft 365 Agents SDK',53,471,854,30,18);
  }else if(kind==='evaluation'){
    rowFlow(slide,['Same test set','Run before','One change','Run after'],{y:202,h:80,size:23});
    const a=node(slide,'Compare individual cases',244,360,288,82,{fill:pale});
    const b=node(slide,'Inspect source / tool trace',589,360,310,82);arrow(slide,a,b);
    text(slide,'Check improvements AND regressions; verify the grader’s explanation.',53,132,854,48,21);
    text(slide,'A model change is a change to test.',53,473,854,30,19);
  }else if(kind==='publish'){
    rowFlow(slide,['Tested draft','Publish\nconfigured version','Scoped channel\nand access','Fresh session\nactual user'],{y:212,h:114,size:21});
    text(slide,'Publishing, installing, and granting access are separate checks.',53,377,854,70,25,true);
    text(slide,'Instructor: entitled environment. Trial learners: observe this demo.',53,461,854,38,20);
  }else throw new Error(`Unknown diagram: ${kind}`);
}
function table(slide,item){
  const values=[item.columns,...item.rows],rows=values.length;
  // The five-concern table needs extra native PowerPoint footer clearance.
  const top=item.title==='Five Well-Architected concerns'?146:160;
  const t=slide.tables.add({rows,columns:2,left:53.215,top,width:853.575,height:Math.min(336,rows*62),columnWidths:[292,561.575],values});
  t.styleOptions={headerRow:true,bandedRows:false};
  t.borders.assign({fill:'#FFFFFF',width:1,style:'solid'});
  t.cells.block({row:0,column:0,rowCount:rows,columnCount:2}).assign({margins:{top:9,bottom:9,left:12,right:12},anchor:'center'});
  for(let r=0;r<rows;r++)for(let c=0;c<2;c++){
    const cell=t.getCell(r,c);cell.fill=r===0?'#D30020':r%2===0?'#F3F3F3':'#FFFFFF';
    cell.text.style={typeface:'Arial',fontSize:r===0?20:19,bold:r===0,color:r===0?'#FFFFFF':ink,autoFit:'none'};
  }
  if(item.subtitle)text(slide,item.subtitle,53,112,854,35,20,true);
}
try{
  await fs.mkdir(buildDir,{recursive:true});await fs.mkdir(path.dirname(output),{recursive:true});
  const manuscript=JSON.parse(await fs.readFile(path.join(repo,'instructor','teaching-slides.json'),'utf8'));
  const imported=await PresentationFile.importPptx(await FileBlob.load(template));
  const originals=[...imported.slides.items],chosen=[];
  for(const [i,item] of manuscript.slides.entries()){
    // Duplicate source slides so the original master, layout, and brand assets survive.
    const ref=item.kind==='cover'?0:item.kind==='break'?16:2;
    const slide=originals[ref].duplicate();chosen.push(slide.id);
    const shapes=slide.shapes.items;
    for(const sh of shapes)sh.text='';
    if(item.kind==='cover'){
      shapes[0].text=item.title;shapes[0].position={left:53.215,top:126,width:320,height:258};
      shapes[0].text.style={typeface:'Poppins SemiBold',fontSize:40,color:'#FFFFFF',autoFit:'none'};
      shapes[1].text='Tim Warner\nSeptember 8, 2026';shapes[1].position={left:53.215,top:438,width:310,height:68};
      shapes[1].text.style={typeface:'Poppins',fontSize:24,color:'#FFFFFF',autoFit:'none'};
    }else if(item.kind==='break'){
      shapes[0].text=item.title;shapes[0].text.style={typeface:'Poppins SemiBold',fontSize:42.67,color:'#FFFFFF',autoFit:'none'};
      text(slide,item.lines.join('\n'),53,292,835,102,25,false,'#FFFFFF');
    }else{
      shapes[0].text=item.title;shapes[0].text.style={typeface:'Poppins SemiBold',fontSize:32,color:ink,autoFit:'none'};
      shapes[3].text=String(i+1);shapes[3].text.style={typeface:'Arial',fontSize:10,color:ink,autoFit:'none'};
      if(item.kind==='table')table(slide,item);
      else if(item.kind==='diagram')diagram(slide,item.diagram);
      else if(item.kind==='illustration'){
        item.lines.forEach((line,j)=>text(slide,line,53,186+j*89,326,77,24,j===0));
        slide.images.add({blob:new Uint8Array(await fs.readFile(path.join(repo,item.asset))),contentType:'image/png',alt:'Conceptual illustration of a maker designing a conversation for an internal Azure learner',fit:'contain',position:{left:402,top:166,width:508,height:336}});
      }else if(item.kind==='outcomes'){
        item.lines.forEach((line,j)=>{text(slide,`${j+1}`,53,151+j*84,36,45,28,true,blue);text(slide,line,105,147+j*84,797,75,22);});
      }else if(item.kind==='sequence'){
        item.lines.forEach((line,j)=>{text(slide,`${j+1}`,53,167+j*79,36,45,28,true,blue);text(slide,line,105,167+j*79,797,65,24);});
      }else{
        const y=item.lines.length===4?166:190,gap=item.lines.length===4?78:93;
        item.lines.forEach((line,j)=>text(slide,line,53,y+j*gap,850,70,item.kind==='comparison'?25:24,j===0));
      }
    }
    const sources=item.sources.map(url=>`Source: ${url}`).join('\n');
    slide.speakerNotes.textFrame.setText(`${item.notes}\n\n${sources}`.trim());
  }
  const proto=imported.toProto(),byId=new Map(proto.slides.map(s=>[s.id,s]));
  proto.slides=chosen.map((id,i)=>({...byId.get(id),index:i}));
  const deck=Presentation.load(proto);
  for(let i=0;i<deck.slides.items.length;i++){
    const slide=deck.slides.items[i];const name=String(i+1).padStart(2,'0');
    await fs.writeFile(path.join(buildDir,`${name}.png`),new Uint8Array(await(await deck.export({slide,format:'png',scale:1.25})).arrayBuffer()));
    await fs.writeFile(path.join(buildDir,`${name}.json`),await(await slide.export({format:'layout'})).text());
  }
  const candidate=path.join(buildDir,'candidate.pptx');await(await PresentationFile.exportPptx(deck)).save(candidate);
  const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools','artifact_tool_utils.mjs')).href);
  const tableOwners=manuscript.slides.flatMap((s,i)=>s.kind==='table'?[i+1]:[]);
  const result=await finalizePresentation({workspaceDir:workspace,candidatePath:candidate,finalPath:output,pythonExecutable:process.env.ARTIFACT_RUNTIME_PYTHON,integrityValidatorPath:path.join(skill,'container_tools','inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools','inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','9144000,5143500','--validate-heading-fit',...tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],requiredNativeTableOwnerSlides:tableOwners,fontPolicy:{basis:'reference',families:['Arial','Poppins','Poppins SemiBold'],referencePath:template,referenceSha256:crypto.createHash('sha256').update(await fs.readFile(template)).digest('hex')},sourceTemplatePath:template,verifyArtifactToolImport:true,receiptPath:path.join(buildDir,'validation.json')});
  console.log(JSON.stringify({output,slides:deck.slides.items.length,result}));
}catch(e){console.error(e.stack);process.exitCode=1;}
