#!/usr/bin/perl -w
use XML::LibXML;
use XML::XPath;
use CGI::Cookie qw();
use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;

use CGI;
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

$page = CGI->new;

	if(	!($page->cookie('utente') )) {
		print redirect(-uri=>'login.cgi');
	}

	#Controllo pagina che chiama lo script
	if($ENV{'HTTP_REFERER'}!~/admin.cgi$|cnews.cgi$/){
	  print redirect(-uri=>'login.cgi');
	}

	$parser = XML::LibXML->new();
	
	#prendo xml
	$doc = $parser->parse_file("../public_html/news.xml");
	$doch = $parser->parse_file("../public_html/home.xml");
		
	#Prendo radice riferimento
	$root = $doc->getDocumentElement;
	@news = $root->getElementsByTagName('notizia');
		
	#Indico namespace 
	$doc->documentElement->setNamespace("http://www.portoconte1.it","d");
	$doch->documentElement->setNamespace("http://www.portoconte1.it","h");
		
	#Scarco in Array paralleli id e titoli					
	$cont;
	foreach $nod (@news){#prendo id e titoli news in xml
		$Tnews[$cont]=$nod->getElementsByTagName('titolo');
		$TnewsID[$cont]=$nod->getElementsByTagName('id');
	$cont++;
	}

	if(($page->param("Eliminatore") eq 'Elimina')){
		$id=0;#contattore per eliminare file html

		foreach $nod (@TnewsID){
			#Controllo se parametro Id va eliminato
			if($page->param($nod) eq 'Elimina'){
				$Elim=$doc->findnodes("/d:notizie/d:notizia[d:id=$nod]")->get_node(1);
				$padre=$Elim->parentNode;
				$padre->removeChild($Elim);
						
				$Elim=$doch->findnodes("/h:notizie/h:notizia[h:id=$nod]")->get_node(1);
				$padre=$Elim->parentNode;
				$padre->removeChild($Elim);
						
				#elimino file "Titolo".html
		  		unlink("../public_html/$Tnews[$id].html");
			}
			$id++;
		}

		#Salvo modifiche
		#news.xml
		open (OUT,">../public_html/news.xml")
	             	or die "Errore news.xml";
	  		print OUT $doc->toString;
	  	close (OUT);
	  		
	  	#home.xml
	  	open (OUT,">../public_html/home.xml")
	             	or die "Errore home.xml";
	  		print OUT $doch->toString;
	  	close (OUT);
	  		
	  	#reindirizzo (devo ricaricare xml)
	  	print redirect (-url=>"cnews.cgi");
	}
		
	#Stampo Pagina--------------------------------------------------------------------------
	print "Content-type: text/html\n\n";
print <<EOF;

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<title>Elimina N..-Scout Porto conte 1</title>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
			<meta name="description" content="Elimina news da porto conte"/>
			<meta name="keywords" content="Porto conte, elimina news, scout, Agesci"/> 
			<meta name="language" content="italian it"/> 
			<meta name="author" content="Serena Pattaro,David Tessaro, Riccardo Rizzo"/>
			<meta name="viewport" content="width=device-width"/> 
			<meta name="X-UA-compatible" content="IE=edge, crome=1"/> 
			<link rel="stylesheet" type="text/css" href="../css/standard.css" media="screen" /> 
			<link rel="stylesheet" type="text/css" media="handheld, screen and (max-width:39em), only screen and(max-device-width:30em)" href="../css/mobile.css"/> 
			<link rel="stylesheet" type="text/css" media="print" href="../css/print.css"/>
			<script type="text/javascript" src="jscript/c_browser.js"></script>
		</head>
		<body>
			  
			<div id="header">
			    <a tabindex="1" href="../home.xml"><img src="../immagini/agesci.png" class="HeaderIMG" alt="logo Associazione Guide e Scaut Cattolici Italiani"/></a>
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
				  	<li><a tabindex="2" href="admin.cgi">Nuovo Articolo</a></li>
				    <li class="currentlink">Cancella Articolo</li>
				</ul>
			</div>

			<div id="corpo">    
				<form method="post" action="cnews.cgi">	
EOF
;
			#Stampo Lista News presenti in xml--------------------------

			$Id=0;#utile per estrarre TnewsID
			foreach $nod (@Tnews) {
				print "<fieldset>
				<p><input id='' class='' name=@TnewsID[$Id] value='Elimina' 
							type='checkbox'>Titolo: @Tnews[$Id] </p></fieldset>";
				$Id++;
				}

			#Continuo a stampare pagina
			print <<EOF;
			<p><input id="submit" onclick="" name="Eliminatore" class="" value="Elimina" type="submit" tabindex="3"/></p>
				</form>
			</div>
			    <div id="foot">
			        <img  class="valid" src="../immagini/valid-xhtml10.png" alt="logo html valido"/>
					<img class="valid" src="../immagini/vcss.gif" alt="logo css valido"/>  
					<img class="valid" src="../immagini/wcag2AAA.gif" alt="logo sito accessibile in tripla A"/>
			        <p class="continua"><span xml:lang="en">NewVision</span></p>
			    </div>
			</div>
		</body>
	</html>
EOF
;