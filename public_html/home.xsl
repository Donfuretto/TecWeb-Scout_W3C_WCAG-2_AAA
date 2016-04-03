<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:n="http://www.portoconte1.it" exclude-result-prefixes="n">
<xsl:output method="html" version="1.0" encoding="UTF-8" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" indent="yes" /> <!--DA RIVEDERE-->
<xsl:template match="/">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
 <head>
   <title>Home Page-Scout Porte Conte 1</title>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
   <meta name="title" content="Gruppo Scout Porte Conte 1 - Home Page"/> 
   <meta name="description" content="home page sito gruppo scout agesci Porto Conte 1"/>
   <meta name="keywords" content="Agesci, scout, Porto Conte, gruppo, nautico,"/>
   <meta name="author" content="Riccardo Rizzo,Serena Pattaro,Tessaro David"/>
   <meta name="viewport" content="width=device-width"/> 
   <meta name="language" content="italian it"/>
   <link href="css/standard.css" rel="stylesheet" type="text/css" media="screen"/>
   <link rel="stylesheet" type="text/css" media="handheld, screen and (max-width:39em), only screen and(max-device-width:30em)" href="css/mobile.css"/>
   <link rel="stylesheet" type="text/css" media="print" href="css/print.css"/>
    <script type="text/javascript" src="jscript/c_browser.js"></script>
 </head> 
 
 <body>
     
    <div id="header">
       <img src="immagini/agesci.png" class="HeaderIMG" alt="logo Associazione Guide e Scaut Cattolici Italiani"/>
       <h1>Porto Conte 1</h1>
       <h2>Gruppo <span xml:lang="en"> Scout </span> Nautico</h2>
       <a href="https://twitter.com/login" tabindex="2"><img src="immagini/Twitter_icon_logo.png" class="social" alt="link alla pagina di login di twitter"/></a>
       <a href="https://www.facebook.com" tabindex="1"><img src="immagini/Facebook_Logo.png" class="social" alt="link alla pagina di login di facebook"/></a>
       
       
       
    </div>

    <div id="container">
        <div id="subhead">
          <p>Ti trovi in&#58; <span xml:lang="en">Home</span></p>
        </div>

        <a tabindex="3" href="#help" class="help_nav">Salta Menù</a>

        <div id="menu">
          <h1>Menù</h1> 
          <ul>
              <li class="currentlink"><span xml:lang="en">Home</span></li>
              <li><a tabindex="4" href="news.xml"><span xml:lang="en">News</span></a></li>
              <li><a tabindex="5" href="storia.html">Storia</a></li>
              <li><a tabindex="6" href="lupetti.html">Lupetti</a></li>
              <li><a tabindex="7" href="reparto.html">Reparto</a></li>
              <li><a tabindex="8" href="clan.html"><span xml:lang="en">Clan</span></a></li>
              <li><a tabindex="9" href="capi.html">Capi</a></li>
              <li><a tabindex="10" href="iscrizioni.html">Contatti</a></li>
          </ul> 
        </div>
        
        <a id="help" tabindex="11" href="#news" class="help_nav">Vai a News</a>
        <a tabindex="12" href="#contenuti" class="help_nav">Vai a contenuto</a>

        <div id="iscrizioni"><a name="iscrizioni"></a>
          <img class="IscrizioniIMG" src="immagini/iscrizioni.jpg" alt="immagine che riporta la scritta scaut cercasi"/>
          <p>Vuoi entrare a far parte del gruppo <span xml:lang="en">scout </span> di Porte Conte 1? <a tabindex="13" href="iscrizioni.html">Iscriviti ora</a>!!!</p>
        </div>  
        <a tabindex="14" href="#contenuti" class="help_nav">Salta <span xml:lang="en">News</span></a>
        
    
          <div id="news" class="text_line">
      <dl> 
      <dt class="box_title"><xsl:value-of select="n:notizie/descendant::n:notizia[last()]/n:titolo"/><ins class="date"><xsl:value-of select="n:notizie/descendant::n:notizia[last()]/n:data"/></ins></dt>
      <dd class="box_content"><xsl:value-of select="n:notizie/descendant::n:notizia[last()]/n:oggetto"/>
        <a tabindex="15" class="continua">
          <xsl:attribute name="href">
              <xsl:value-of select="concat(n:notizie/descendant::n:notizia[last()]/n:titolo,'.html')"/>
          </xsl:attribute>continua...</a>
      </dd>  
      </dl>

      <dl>
      <dt class="box_title"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-1]/n:titolo"/><ins class="date"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-1]/n:data"/></ins></dt>
      <dd class="box_content"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-1]/n:oggetto"/>
        <a tabindex="16" class="continua" >
          <xsl:attribute name="href">
            <xsl:value-of select="concat(n:notizie/descendant::n:notizia[last()-1]/n:titolo,'.html')"/>
          </xsl:attribute>continua...</a> 
      </dd> 
      </dl>

      <dl>
      <dt class="box_title"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-2]/n:titolo"/><ins class="date"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-2]/n:data"/></ins></dt>
      <dd class="box_content"><xsl:value-of select="n:notizie/descendant::n:notizia[last()-2]/n:oggetto"/>
        <a tabindex="17" class="continua">
          <xsl:attribute name="href">
            <xsl:value-of select="concat(n:notizie/descendant::n:notizia[last()-2]/n:titolo,'.html')"/>
          </xsl:attribute>continua...</a> 
      </dd>  
      </dl>
     
      

    </div>


        <div id="corpo">
          <img id="contenuti" class="TopTesto" src="immagini/fotogruppo.jpg" alt="foto di tutti i ragazzi del gruppo"/>
          <ul class="lista">
            <li><h1>Chi siamo</h1></li>
            <li><p>Il Gruppo <span xml:lang="en">Scout</span> Porte Conte 1 conta più di 80 iscritti ed è l'unico gruppo <span xml:lang="en">scout </span> presente nell'antica città sarda Porte Conte.</p></li>
            <li><p>Il nostro gruppo fa parte dell’associazione <abbr title="agesci">A.G.E.S.C.I.</abbr> l’Associazione Guide e <span xml:lang="en">Scout </span>Cattolici Italiani.</p></li>
            <li><p>Ad oggi il gruppo <span xml:lang="en">scout</span> conta un branco, un reparto e un <span xml:lang="en">clan</span>. Tutti questi gruppi sono gestiti da un unica comunità capi.</p></li>
            <li><p>Il Gruppo <span xml:lang="en">Scout</span> Porte Conte 1 offre ai suoi iscritti la possibilità di vivere esperienze uniche a contatto con la natura, nelle quali ognuno ha la possibilità di scoprire se stesso e di inserirsi in una comunità che cresce insieme.</p></li>       
            <li><p>Vuoi entrare a far parte del gruppo <span xml:lang="en">scout </span> di Porte Conte 1? Che aspetti, <a tabindex="18" href="iscrizioni.html">iscriviti</a>!</p></li>
            <li><a tabindex="19" href="#menu" class="help_nav">Vai a Menù</a></li>
          </ul> 
          
          <h2 class="new_page">Branche</h2>
          <dl>
            <dt class="box_title">Lupetti</dt>
            <dd class="box_content"><img class="LogoDivisione" src="immagini/lc.png" alt="logo lupetti"/>
            <p>Sono chiamati così i bambini e le bambine di età compresa tra gli 8 e i 12 anni, che svolgono l'attività in un'unità chiamata branco. Caratteristiche della proposta educativa offerta a questa fascia d'età sono il gioco e la dimensione comunitaria con lo scopo di educare i bambini alla lealtà, al rispetto delle regole e dei compagni di branco e a essere disponibili ad aiutare il prossimo.</p><a tabindex="20" href="lupetti.html" class="continua">continua...</a></dd>
          </dl>

          <a tabindex="21" href="#menu" class="help_nav">Vai a Menù</a>

          <dl>
            <dt class="box_title">Reparto</dt>
            <dd class="box_content"><img class="LogoDivisione" src="immagini/eg.png" alt="logo reparto"/>
            <p>O più precisamente: Esploratori e Guide; sono i ragazzi e le ragazze che hanno dai 12 ai 16 anni. A loro lo scautismo offre una proposta educativa basata sull'avventura, la vita all'aperto, l'autoeducazione, la manualità, la vita di gruppo e la dimensione di comunità.
            I ragazzi sono divisi in gruppi monosessuati chiamati Squadriglie, all'interno dei quali vivono l'esperienza <span xml:lang="en">scout </span>tramite giochi, attività manuali e vita all'aperto nella natura.</p><a tabindex="19" href="reparto.html" class="continua">continua...</a></dd>
          </dl>

          <a tabindex="22" href="#menu" class="help_nav">Vai a Menù</a>

          <dl>
            <dt class="box_title"><span xml:lang="en">Clan</span></dt>
            <dd class="box_content"><img class="LogoDivisione" src="immagini/rs.png" alt="logo clan"/><p>Il <span xml:lang="en">Clan</span> è la branca che ospita  i <span xml:lang="en">Rover</span> e le <span xml:lang="en">Scolte</span> cioè i ragazzi e le ragazze tra i 17 e i 21 anni, che formano una comunità e continuano la loro formazione all'interno di essa. In questa branca le attività sono svolte dai ragazzi, sono loro che insieme decidono quali temi affrontare e che esperienze vivere, in accordo con i capi. Gli strumenti educativi che utilizza lo scautismo in questa fascia d'età sono principalmente il confronto, la strada (il fare strada: a piedi, in canoa, in bici...) e il servizio.</p><a tabindex="23" href="clan.html" class="continua">continua...</a></dd>
          </dl>

          <a tabindex="24" href="#menu" class="help_nav">Vai a Menù</a>

          <dl>
            <dt class="box_title">Comunità Capi</dt>
            <dd class="box_content"><img class="LogoDivisione" src="immagini/coca.png" alt="logo comunità capi"/>
            <p>Spesso abbreviata in <abbr title="coca"> Co.Ca.</abbr>, il gruppo in questione è composto da soci adulti che si impegnano nella gestione di un gruppo <span xml:lang="en">scout </span> e nell'educazione dei ragazzi; è fedele ai principi del patto associativo e al metodo <span xml:lang="en">scout</span> condiviso tra tutti i gruppi dell'associazione. La Comunità Capi è un ambiente caratterizzato dalla condivisione dalla corresponsabilità educativa e dalla solidarietà reciproca.</p><a tabindex="25" href="capi.html" class="continua">continua...</a></dd>
          </dl>

          <a tabindex="26" href="#menu" class="help_nav">Vai a Menù</a>
      
        </div>

        <div id="foot">
          <p>Gruppo <span xml:lang="en">Scout</span> Porto Conte 1 &#124; Via Pippo Paolo 14 &#45; 34566 Porto Conte &#124; Tel 348 9911754  &#124; <a tabindex="27"  href="link.html">link utili</a> &#124; <a tabindex="28" href="iscrizioni.html">contatti</a></p>
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
