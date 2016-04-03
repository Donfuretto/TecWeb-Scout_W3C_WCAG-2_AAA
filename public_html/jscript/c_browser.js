var nVer = navigator.appVersion;
var nAgt = navigator.userAgent;
var browserName  = navigator.appName;
var fullVersion  = ''+parseFloat(navigator.appVersion);
var majorVersion = parseInt(navigator.appVersion,10);
var nameOffset,verOffset,ix;
  
//In Internet Explorer la versione reale si trova dopo "MSIE" nell'userAgent
if ((verOffset=nAgt.indexOf("MSIE"))!=-1) {
 browserName = "Microsoft Internet Explorer";
 fullVersion = nAgt.substring(verOffset+5);
}
// In Opera, la versione reale si trova dopo "Opera"
else if ((verOffset=nAgt.indexOf("Opera"))!=-1) {
 browserName = "Opera";
 fullVersion = nAgt.substring(verOffset+6);
}
// In Chrome, la versione reale si trova dopo "Chrome"
else if ((verOffset=nAgt.indexOf("Chrome"))!=-1) {
 browserName = "Chrome";
 fullVersion = nAgt.substring(verOffset+7);
}
// In Safari, la versione reale si trova "Safari"
else if ((verOffset=nAgt.indexOf("Safari"))!=-1) {
 browserName = "Safari";
 fullVersion = nAgt.substring(verOffset+7);
}
// In Firefox, la versione reale si trova dopo "Firefox"
else if ((verOffset=nAgt.indexOf("Firefox"))!=-1) {
 browserName = "Firefox";
 fullVersion = nAgt.substring(verOffset+8);
}
// Nella maggior parte dei browser, "name/version" è alla fine dell'userAgent
else if ( (nameOffset=nAgt.lastIndexOf(' ')+1) < (verOffset=nAgt.lastIndexOf('/')) )
{
 browserName = nAgt.substring(nameOffset,verOffset);
 fullVersion = nAgt.substring(verOffset+1);
 if (browserName.toLowerCase()==browserName.toUpperCase()) {
  browserName = navigator.appName;
 }
}
// "taglia" la string fullVersion se è presente uno spazio
if ((ix=fullVersion.indexOf(";"))!=-1) fullVersion=fullVersion.substring(0,ix);
if ((ix=fullVersion.indexOf(" "))!=-1) fullVersion=fullVersion.substring(0,ix);
  
majorVersion = parseInt(''+fullVersion,10);
if (isNaN(majorVersion)) {
 fullVersion  = ''+parseFloat(navigator.appVersion);
 majorVersion = parseInt(navigator.appVersion,10);
}



	
var numver=Number(fullVersion);
//window.alert('stai usando:'+ browserName+' versione:'+numver);

if((browserName=="Microsoft Internet Explorer")&&(numver < 9)){
window.alert('Per migliorare la visualizzazione del sito su questo pc aggiorna : \n \n '+browserName +' alla versione più recente,\n \n ma puoi comunque continuare la navigazione! ');
}
/*
if((browserName=="Netscape")&&(numver <6)){
window.alert('Per migliorare la visualizzazione del sito su questo pc aggiorna : \n \n '+browserName +' alla versione più recente,\n \n ma puoi comunque continuare la navigazione! ');
}*/


 
