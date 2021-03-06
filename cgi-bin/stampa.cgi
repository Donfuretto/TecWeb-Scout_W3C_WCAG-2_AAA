open (OUT,">../public_html/$titolo.html") or die "Errore Creazione pagina";
        print OUT "<?xml version='1.0' encoding='UTF-8'?>
        <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
        <html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
         <head>
           <title>$title-Scout Porto conte 1</title>
           <meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>
           <meta name='description' content='ultime news nel dettaglio'/>
           <meta name='keywords' content='News,Scout,Porto Conte1'/>
           <meta name='author' content='Tessaro David'/>
           <meta name='language' content='italian it'/>
           <meta name='X-UA-compatible' content='IE=edge, crome=1'/> <!--IE per crome 1  -->
           <link href='css/standard.css' rel='stylesheet' type='text/css' media='screen'/>
           <link rel='stylesheet' type='text/css' media='handheld, screen and (max-width:39em), only screen and (max-device-width:30em)' href='css/mobile.css'/>
             <link rel='stylesheet' type='text/css' media='print' href='css/print.css'/>
         </head> 
         
         <body>
          <div id='header'>
              <a tabindex='1' href='home.xml'><img class='HeaderIMG' src='immagini/agesci.png' alt='logo Associazione Guide e Scout Cattolici Italiani'/></a>         
              <h1>Porto Conte 1</h1>
              <h2>Gruppo <span xml:lang='en'>Scout </span>Nautico</h2>
              <a href='https://twitter.com/login' tabindex='3'><img src='immagini/Twitter_icon_logo.png' class='social' alt='linc alla pagina di loghin di tuitter'/></a>
              <a href='https://www.facebook.com' tabindex='2'><img src='immagini/Facebook_Logo.png' class='social' alt='linc alla pagina di loghin di feisbuc'/></a>
          </div>

          <div id='container'>
            
            <div id='subhead'>
              <p>Ti trovi in&#58;<span xml:lang='en'> <a tabindex='4' href='home.xml'>Home</a> </span> &gt; <span xml:lang='en'><a tabindex='5' href='news.xml'>News</a></span> &gt; $titolo </p>
            </div>

            <div class='help_nav'>
              <a tabindex='6' href='#contenuto' class='help_nav'>Salta Menù</a>
            </div>

            <div id='menu'>
                <h1>Menù</h1>
                <ul>    
                    <li><a tabindex='7' href='home.xml'><span xml:lang='en'>Home</span></a></li>
                    <li><a tabindex='8' href='news.xml'><span xml:lang='en'>News</span></a></li>
                    <li><a tabindex='9' href='storia.html'><span xml:lang='en'>News</span></a></li>
                    <li><a tabindex='10' href='lupetti.html'>Lupetti</a></li>
                    <li><a tabindex='11' href='reparto.html'>Reparto</a></li>
                    <li><a tabindex='12' href='clan.html'><span xml:lang='en'>Clan</span></a></li>
                    <li><a tabindex='13' href='capi.html'>Capi</a></li>
                    <li><a tabindex='14' href='iscrizioni.html'>Contatti</a></li>
                </ul>
            </div>

            <div id='iscrizioni'>
                        <img class='IscrizioniIMG' src='immagini/iscrizioni.jpg' alt=''/>
                        <p>Vuoi entrare a far parte del gruppo scout di Porte Conte 1? <a tabindex='15' href='iscrizioni.html'>Iscriviti ora!!!</a></p>
                    </div>

            <div id='corpo'>
              <ul class='lista'>
                <li><h1>$titolo</h1></li>
                <li><p class='date'>$date</p></li>
                <li><img class='IMGnews' src='immagini/$img' alt='$alt'/></li>
                <li><div id='test'><p>$testo</p></div></li></ul>
                <a tabindex='16' href='#menù' class='help_nav'>Vai a Menù</a>
            </div>
            <a tabindex='17' href='#menù' class='help_nav'>Vai a Menù</a>
               <div id='foot'>
            
              <p>Gruppo <span xml:lang='en'>Scout</span> Porto Conte 1 &#124; Via Pippo Paolo 14 &#45; 34566 Porto Conte &#124; Tel 348 9911754 &#45; <a tabindex='18' href='link.html'>link utili</a> &#124; <a tabindex='19' href='iscrizioni.html'>contatti</a></p>
              <img class='valid' src='immagini/valid-xhtml10.png' alt='logo html valido'/>
              <img class='valid' src='immagini/vcss.gif' alt='logo css valido'/>  
                </div>
            </div>
          </body>
          </html>";
close (OUT);