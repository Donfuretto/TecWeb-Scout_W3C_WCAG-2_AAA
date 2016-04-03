<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="news.xml"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:n="http://www.portoconte1.it" exclude-result-prefixes="n">
<xsl:output method="html" version="1.0" encoding="UTF-8" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" indent="yes" /> <!--DA RIVEDERE-->
<xsl:template match="/">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
  <title>News-Scout Porte Conte 1</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <meta name="description" content="News sulle attività del gruppo scout agesci Porto Conte 1"/>
  <meta name="keywords" content="news, scout, agesci, Porto Conte 1"/>
  <meta name="author" content="Riccardo Rizzo,Serena Pattaro,David Tessaro"/>
  <meta name="viewport" content="width=device-width"/> 
  <meta name="language" content="italian it"/>
  <link href="css/standard.css" rel="stylesheet" type="text/css" media="screen"/>
  <link rel="stylesheet" type="text/css" media="handheld, screen and (max-width:39em), only screen and(max-device-width:30em)" href="css/mobile.css"/> 
  <link rel="stylesheet" type="text/css" media="print" href="css/print.css"/>
   <script type="text/javascript" src="jscript/c_browser.js"></script>
 </head>
 
 <body>
     
  <div id="header">
    <a tabindex="1" href="home.xml"><img class="HeaderIMG" src="immagini/agesci.png" alt="logo Associazione Guide e Scaut Cattolici Italiani"/></a>         
    <h1>Porto Conte 1</h1>
    <h2>Gruppo <span xml:lang="en">Scout </span> Nautico</h2>
    <a href="https://twitter.com/login" tabindex="3"><img src="immagini/Twitter_icon_logo.png" class="social" alt="linc alla pagina di loghin di tuitter"/></a>
    <a href="https://www.facebook.com" tabindex="2"><img src="immagini/Facebook_Logo.png" class="social" alt="linc alla pagina di loghin di feisbuc"/></a>
  </div>

  <div id="container">

    <div id="subhead">
      <p>Ti trovi in&#58; <span xml:lang="en"> <a tabindex="4" href="home.xml">Home</a> </span> &gt; <span xml:lang="en">News</span> </p>
    </div>

    <a tabindex="5" href="#help" class="help_nav">Salta Menù</a>
   
    <div id="menu">
      <h1>Menù</h1>
      <ul>    
        <li><a tabindex="6" href="home.xml"><span xml:lang="en">Home</span></a></li>
        <li class="currentlink"><span xml:lang="en">News</span></li>
        <li><a tabindex="7" href="storia.html">Storia</a></li>
        <li><a tabindex="8" href="lupetti.html">Lupetti</a></li>
        <li><a tabindex="9" href="reparto.html">Reparto</a></li>
        <li><a tabindex="10" href="clan.html"><span xml:lang="en">Clan</span></a></li>
        <li><a tabindex="11" href="capi.html">Capi</a></li>
        <li><a tabindex="12" href="iscrizioni.html">Contatti</a></li>
      </ul>
    </div>

    <a id="help" tabindex="13" href="#corpo" class="help_nav">Vai a contenuto</a>      
      
    <div id="iscrizioni">
      <img class="IscrizioniIMG" src="immagini/iscrizioni.jpg" alt="mmagine con scritta scaut cercasi"/>
      <p>Vuoi entrare a far parte del gruppo <span xml:lang="en">scout </span> di Porte Conte 1? <a tabindex="14" href="iscrizioni.html">Iscriviti ora</a>!!!</p>
    </div>
      
    <a tabindex="15" href="#menu" class="help_nav">Vai a Menù</a>

    <div id="corpo">
      
      <xsl:for-each select="n:notizie/n:notizia"> 
        <xsl:sort select="position()" data-type="number" order="descending"/>
        <dl>   
          <dd class="box_news">
             <h2><xsl:value-of select="n:titolo"/></h2><p class="date"><xsl:value-of select="n:data"/></p>
            <img class="IMGnews" src="immagini/{n:img}" alt="{n:alt_img}"/><p><xsl:value-of select="n:corpo" /></p>
             <a tabindex="16" class="continua">
              <xsl:attribute name="href">
                <xsl:value-of select="concat(n:titolo,'.html')"/>
              </xsl:attribute>Leggi...</a>
          </dd>
        </dl>

        <div class="lista">
          <a tabindex="17" href="#menu" class="help_nav">Vai a Menù</a>
        </div>
      </xsl:for-each>
  </div>

  <div id="foot">
    <p>Gruppo <span xml:lang="en">Scout</span> Porto Conte 1 &#124; Via Pippo Paolo 14 &#45; 34566 Porto Conte &#124; Tel 348 9911754 &#124; <a tabindex="18" href="link.html">link utili</a> &#124; <a tabindex="19" href="iscrizioni.html">contatti</a></p>
    <img  class="valid" src="immagini/valid-xhtml10.png" alt="logo html valido"/>
		<img class="valid" src="immagini/vcss.gif" alt="logo css valido"/>  
		<img class="valid" src="immagini/wcag2AAA.gif" alt="logo sito accessibile in tripla a"/>
    <p class="continua"><span xml:lang="en">NewVision</span></p>
  </div>
</div>
</body>
</html>

</xsl:template>
</xsl:stylesheet>
