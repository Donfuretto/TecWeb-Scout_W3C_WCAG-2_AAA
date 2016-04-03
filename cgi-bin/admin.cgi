#!/usr/bin/perl -w
use CGI;
use CGI qw(:standard);
use XML::LibXML;
use CGI::Cookie qw();
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

use Time::localtime;#data e ora
use Time::Piece;


$page = CGI->new;

if( !($page->cookie('utente'))) {
  print redirect(-uri=>'login.cgi');
}

if($ENV{'HTTP_REFERER'}!~/admin.cgi$|cnews.cgi$|login.cgi$/){
  print redirect(-uri=>'login.cgi');
}

print "Content-type: text/html\n\n";

if(($page->param("Ins") eq 'Inserisci')){
  my $parser = XML::LibXML->new();
    #apro file xml
    my $filenews='../public_html/news.xml';
    my $filehome='../public_html/home.xml';
    
    #raccolgo dati dal limbo
    $titolo= $page -> param('nome');
    $testo= $page -> param('descrizione');
    $alt=$page -> param('descr');
    $img=$page -> param('files[]');

    #Controllo dati
    if($titolo=~/[<>=]/){
      $ERRORE_TITOLO=1;
      $ERRORE=1;
    }
    if($testo=~/[<>=]/){
      $ERRORE_TESTO=1;
      $ERRORE=1;
    }
    if($alt=~/[<>=]/){
      $ERRORE_ALT=1;
      $ERRORE=1;
    }
    open IMG, "<", "/$img";
      $size = (stat(IMG))[7];
    close IMG;

    if($img!~/jpg$|png$/)
    {
      $ERRORE_IMG=1;
      $ERRORE=1;
    }
    if($size>2*1048576){
      $ERRORE_DIM=1;
      $ERRORE=1;
    }

    #apro filenews per prendere ultimo id
    my $doc = $parser->parse_file($filenews);
      if(!$doc){$ERRORE=1;}
    my $root = $doc->getDocumentElement;
    @news = $root->getElementsByTagName('notizia');
    
    $id=0;
    foreach $nod (@news){$id++;}#calcolo ultimo id
    $id++;

    #creo data di oggi
    $date = localtime->strftime('%Y-%m-%d');   
    #Sistemo nome img
      $img=~ s/.*[\/\\](.*)/$1/;
    if(!$ERRORE){
      #creo segmento corretto per xml
      $n_news ="\n\t<notizia>
      \t<id>$id</id>
      \t<titolo>$titolo</titolo>
      \t<data>$date</data>
      \t<img>$img</img>
      \t<alt_img>$alt</alt_img>
      \t<corpo>$testo</corpo>
      \n\t</notizia>\n";

      #Carico Immagine

      #Scelgo la cartella
      $upload_dir="../public_html/immagini";

      $upload_filehandle = $page->upload('files[]');#vado a prenderla dal limbo
      open UPLOADFILE, ">$upload_dir/$img"
              or die "Caricamento Immagine fallita";  
        while (<$upload_filehandle>){#Se c'è cartico
          print UPLOADFILE;
        }
      close UPLOADFILE;

      #Inserisco in News 
      $frammento=$parser->parse_balanced_chunk($n_news);
      $root->appendChild($frammento);

      open (OUT,">$filenews")
              or die "Errore $filenews"; 
        print OUT $doc->toString;
      close (OUT);
      
      #Creo HTML news
      $title=substr($titolo, 0, 7);
      #richiamo parte di codice per stampa html
      require "stampa.cgi";

      #creo stringa per homexml
      $Ogg=substr($testo, 0, 100);
      $n_news ="\n\t<notizia>
      \t<id>$id</id>
      \t<titolo>$titolo</titolo>
      \t<data>$date</data>  
      \t<oggetto>$Ogg</oggetto>
      \n\t</notizia>\n";
      
      #Inserisco in Homexml
      my $doc = $parser->parse_file("../public_html/home.xml");
      my $root = $doc->getDocumentElement;
      $frammento=$parser->parse_balanced_chunk($n_news);
      $root->appendChild($frammento);
      
      open (OUT,">$filehome")
              or die "Errore $filehome";
        print OUT $doc->toString;
      close (OUT);

      #Se sono qui è andato tutto bene
      $Articolo="Articolo inserito";
  }
}#------------------------------------------------------------------------------------------------

print <<EOF;

<?xml version='1.0' encoding='UTF-8'?>
      <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
      <html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
      <head>
      <title>Nuova N..-Scout Porto conte 1</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
      <meta name="description" content="inserimento nuova news"/>
      <meta name="keywords" content="Porto conte, nuova news, scout, Agesci"/> 
      <meta name="language" content="italian it"/> 
      <meta name="author" content="Serena Pattaro,David Tessaro, Riccardo Rizzo"/>
      <meta name="viewport" content="width=device-width"/> 
      <meta name="X-UA-compatible" content="IE=edge, crome=1"/> 
      <link rel="stylesheet" type="text/css" href="../css/standard.css" media="screen" /> 
      <link rel="stylesheet" type="text/css" media="handheld, screen and (max-width:39em), only screen and(max-device-width:30em)" href="../css/mobile.css"/> 
      <link rel="stylesheet" type="text/css" media="print" href="../css/print.css"/>
      <script type="text/javascript" src="../jscript/c_browser.js"></script>
</head>
<body>   
    <div id="header">
    <a tabindex="1" href="../home.xml"><img src="../immagini/agesci.png" class="HeaderIMG" alt="logo Associazione Guide e Scout Cattolici Italiani"/></a>
       <h1>Porto Conte 1</h1>
       <h2>Gruppo <span xml:lang="en">Scout </span>Nautico</h2>          
    </div>

    <div id="container">
        <div id="subhead">
          <h3>Pannello di amministrazione</h3> 
        </div>

      <div id="menu">
        <h1>Menù</h1> 
        <ul>
            <li class="currentlink">Nuovo Articolo</li>
            <li><a tabindex="2" href="cnews.cgi">Cancella Articolo</a></li>
        </ul>
      </div>

      <div id="corpo">

EOF
;
      #Stampo eventuali errori
      if($Articolo)
        {print "<p>$Articolo</p>"}
      if($ERRORE)
        {print "<p>Errore Inserimento pagina.</p>";}
      if($ERRORE_TITOLO)
        {print "<p>ERRORE TITOLO: errore nel titolo dell'articolo!</p>";}
      if($ERRORE_IMG)
        {print "<p>ERRORE FORMATO IMMAGINE: il file immagine deve essere formato jpg o png.</p>";}
      if($ERRORE_DIM)
        {print "<p>ERRORE DIMENSIONE IMMAGINE: attenzione, l'immagine non deve superare i 2 mb!</p>";}
      if($ERRORE_ALT)
        {print "<p>ERRORE DESCRIZIONE IMMAGINE: errore nella descrizione dell'immagine!</p>";} 
      if($ERRORE_TESTO)
        {print "<p>ERRORE CORPO: errore nel testo dell'articolo!</p>";}

print <<EOF;

        <form method="post" enctype="multipart/form-data" action="admin.cgi">
          <fieldset>
            <legend>Inserisci nuovo articolo</legend>
            <label title="nome">Titolo: 
            <span><input name="nome" title="nome" type="text" tabindex="3"/></span>
            </label>
            
              <fieldset>
              <legend>Inserisci immagine</legend>
                <label title="file">Immagine: <input type="file" id="files" name="files[]"/></label>
                <output id="list"></output>

            <p><label title="descr">Descrizione immagine: <input name="descr" title="descr" type="text" tabindex="5"/></label></p>
            </fieldset>


            <script type="text/javascript">
              function handleFileSelect(evt) {
                  var files = evt.target.files; 
                  var output = [];
                  for (var i = 0, f; f = files[i]; i++) {
                    if (!f.type.match('image.*')){
                      output.push('<li><strong>','ERRORE FILE NON IMMAGINE','</strong></li>');
                      break;
                    }
                    else{
                      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                        f.size, ' bytes, last modified: ',
                        f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
                        '</li>');}
                    }
                    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
                  }
                 document.getElementById('files').addEventListener('change', handleFileSelect, false);
            </script>
            <fieldset>
              <legend>Notizia:</legend>
              <textarea class="textarea" title="descrizione" name="descrizione" rows="4" cols="50" tabindex="6"></textarea>
            </fieldset>

          </fieldset>
          <p><input id="submit" name="Ins" value="Inserisci" type="submit" tabindex="7"/></p>
        </form>

        <p>ATTENZIONE: non sono accettati i seguenti caratteri: &gt; &lt; &#61; </p> 
    </div>

  <div id="foot">
    <img  class="valid" src="../immagini/valid-xhtml10.png" alt="logo html valido"/>
    <img class="valid" src="../immagini/vcss.gif" alt="logo css valido"/>  
    <img class="valid" src="../immagini/wcag2AAA.gif" alt="logo sito accessibile in tripla A"/>
    <p class="continua">NewVision</p>

  </div>
  
  </div>
</body>
</html>
EOF
;
