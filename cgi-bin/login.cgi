#!/usr/bin/perl -w
use XML::LibXML;

use CGI;
use CGI::Cookie qw();
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

#Creo oggetto CGI
$page = CGI->new;

if($page->param('login') eq "Accedi"){
	$user = $page->param('User');
	$passw = $page->param('Pass');

	#Controllo cosa contiene login
	if($user!~/^([a-zA-Z0-9])/){
		$erroreb=1;
	}
	if($passw!~/^([a-zA-Z0-9])/){
		$erroreb=1;
	}

	if(!$erroreb){
		my $parser = XML::LibXML->new();
		my $doc = $parser->parse_file('../data/login.xml');
		my $root = $doc->getDocumentElement;
		my @users = $root->getElementsByTagName('utente');
		foreach $nod (@users) {
			$dbuser=$nod->getElementsByTagName('username');
			if("$dbuser" eq "$user"){
				$dbpass=$nod->getElementsByTagName('password');
				if("$dbpass" eq "$passw"){
                    $cookie = $page->cookie(
                    -name=>'utente',
                    -value=>'utente',  
                    -expires=>'+10h');
                 	print redirect(-cookie=>$cookie, -url=>"admin.cgi");	
				}
			} 

		}

	}
	$erroreb=1;
}
#Stampa pagina contenente form
	print "Content-type: text/html\n\n";
	print <<EOF;
	<?xml version='1.0' encoding='UTF-8'?>
    <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
    <html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
		<head>
			<title>Login amm..-Scout Porto conte 1</title>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
	       	<meta name="description" content="login per nuove news"/>
			<meta name="keywords" content="login, accesso,Porto conte, scout, Agesci"/> 
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
		      <a tabindex="1" href="../home.xml"><img src="../immagini/agesci.png" class="HeaderIMG" alt="logo Associazione Guide e Scaut Cattolici Italiani"/></a>
         	  <h1>Porto Conte 1</h1>
		      <h2>Gruppo <span xml:lang="en">Scout </span>Nautico</h2>
			</div>
		    
		    <div id="container">
		        <div id="subhead">
		        <h3>Pannello di amministrazione</h3>
		    </div>
		    
		    <div id="corpo">
EOF
;
			if($erroreb){#Segnalo errore se presente
				print "<h3>ERRORE LOGIN: <span xml:lang='en'> Username/Password</span> errate</h3>";	
			}

print <<EOF;
			<form method="post" action="../cgi-bin/login.cgi">
				<fieldset>
				  <legend>Inserire dati utente</legend>
				  <label title="utente">Utente:
				    <input title="utente" type="text" name="User" tabindex="2"/>
				  </label>
				  <label title="password"><span xml:lang="en">Password</span>:
				    <input title="password" type="password" name="Pass" tabindex="3"/>
				  </label>
				  <input id="submit" name="login" class="margineSinistro"  value="Accedi" type="submit" tabindex="4"/>
				</fieldset>  
			</form>
		        </div>
		        <div id="foot">
		          <img  class="valid" src="../immagini/valid-xhtml10.png" alt="logo html valido"/>
				  <img class="valid" src="../immagini/vcss.gif" alt="logo css valido"/>  
				  <img class="valid" src="../immagini/wcag2AAA.gif" alt="logo sito accessibile in tripla A"/>
        		  <p class="continua"><span xml:lang="en">NewVision</span></p>
		        </div>
		    </div>
		</body></html>
EOF
;