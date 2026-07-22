
const file=document.getElementById('pdfFile');
const status=document.getElementById('status');
const start=document.getElementById('startParser');
const bar=document.getElementById('progressBar');

file.addEventListener('change',()=>{
 if(!file.files.length)return;
 const f=file.files[0];
 status.innerHTML=`<strong>${f.name}</strong><br>PDF ausgewählt.`;
 bar.style.width='25%';
 start.disabled=false;
});

start.addEventListener('click',()=>{
 bar.style.width='50%';
 status.innerHTML+=`<br><br>🔧 Parser würde jetzt gestartet werden...`;
 console.log('TODO: Python Parser anbinden');
});
