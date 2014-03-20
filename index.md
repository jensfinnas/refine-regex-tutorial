__Reguljära uttryck__ (regular expression, regex, regexp) är en syntax för att göra __avancerade mönstersökningar i textsträngar__. Vi kan till exempel söka efter alla personnummer, webbadresser, akademiska titlar och så vidare. Reguljära uttyck går att tillämpa i de flesta programmeringsspråk.


### Steg 1: Definiera tecknet
<table>
	<tr><td><code>^</code></td><td>Början av en sträng</td></tr>
	<tr><td><code>$</code></td><td>Slutet av en sträng</td></tr>
	<tr><td><code>.</code></td><td>Vilket tecken som helst</td></tr>
	<tr><td><code>[ ]</code></td><td>Matchar något av tecknen inom klammern. Till exempel <code>[aoueiyåäö]</code> matchar en vokal, <code>[a-ö]</code> en liten bokstav mellan a och ö och <code>E-H</code> en stor bokstav mellan E och H.</td></tr>
	<tr><td><code>\s</code></td><td>Mellanslag</td></tr>
	<tr><td><code>\S</code></td><td>Icke-mellanslag</td></tr>
	<tr><td><code>\d</code></td><td>Siffra</td></tr>
	<tr><td><code>\D</code></td><td>Icke-siffra</td></tr>

</table>

### Definiera antal tecken 
<table>
	<tr><td><code>*</code></td><td>Hur många tecken som helst av föregående.</td></tr>
	<tr><td><code>{3}</code></td><td>Matchar exakt tre tecken. </td></tr>
	<tr><td><code>{3,5}</code></td><td>Matchar exakt tre-fem tecken. </td></tr>
	<tr><td><code>{3,}</code></td><td>Matchar tre tecken eller fler. </td></tr>
</table>

__Komplett lista över funktioner:__ http://www.tutorialspoint.com/python/python_reg_expressions.htm

### Exempel
__Exempeltext:__

> Carl Bildt, 64, (M), Fredrik Reinfeldt, 48, (M) och Annie Lööf, 30, (C) möttes i Rosenbad den 12.3.2014.

> – Jag är mycket nöjd över våra samtal, säger Bildt. 

<table>
	<tr>
		<td>Sök årtal</td>
		<td><code>\d{4}</code> eller <code>\d\d\d\d</code></td>
		<td>Carl Bildt, 64, (M), Fredrik Reinfeldt, 48, (M) och Annie Lööf, 30, (C) möttes i Rosenbad den 12.3.<code>2014</code>.</td>
	</tr>
	<tr>
		<td>Sök ålder</td>
		<td><code>, (\d{1,2}),</code></td>
		<td>Carl Bildt, <code>64</code>, (M), Fredrik Reinfeldt, <code>48</code>, (M) och Annie Lööf, <code>30</code>, (C) möttes i Rosenbad den 12.3.2014.</td>
	</tr>
	<tr>
		<td>Sök citat</td>
		<td><code>–.*$</code></td>
		<td>
			Carl Bildt, 64, (M), Fredrik Reinfeldt, 48, (M) och Annie Lööf, 30, (C) möttes i Rosenbad den 12.3.2014.
		
			<code>– Jag är mycket nöjd över våra samtal, säger Bildt.</code>
		</td>
	</tr>
	<tr>
		<td>Sök partiförkortningar</td>
		<td><code>\([A-Ö]{1,2}\)</code></td>
		<td>
			Carl Bildt, 64, <code>(M)</code>, Fredrik Reinfeldt, 48, <code>(M)</code> och Annie Lööf, 30, <code>(C)</code> möttes i Rosenbad den 12.3.2014.
		</td>
	</tr>
</table>

### Övning: 
![Regex101](http://jensfinnas.github.io/refine-regex-tutorial/images/01regex101.png)
Gå till http://regex101.com/#python

Klistra in texten från http://jensfinnas.github.io/refine-regex-tutorial/tweets.txt

- Hitta alla siffror
- Hitta alla Twitter-namn (@jensfinnas)
- Hitta alla hashtaggar (#XXXXX).
- Hitta alla url:ar (http://).


# Open Refine
Open Refine (som tidigare hette Google Refine) är att gratisverktyg för att __tvätta och bearbeta data__. Med Open Refine kan du bland annat:
- Identifiera och harmonisera __stavningsvariationer__ (till exempel "Ericsson Ab", "Ericsson", "Ericson" => "Ericsson")
- Använda externa API:er för att komplettera ditt dataset. Till exempel genom att anropa en __geokodare__ som gör om adresser till longituder och latituder.
- Köra __reguljära uttryck__.
- Jobba med __stora mängder data__.

Open Refine är framför allt användbart när man jobbar med __textdata__. Om du har numerisk data och vill göra beräkningar är det vanligen enklare att använda Excel eller något annat kalkylprogram.

Varje databearbetning i Refine består av två steg:
1) Välj vilken dela av datan du vill jobba med genom att applicera ett __facet__ (filter).
2) Applicera en funktion (ofta genom att klicka på en kolumnrubrik och välj __Edit column__).

### Importera data
Öppna Open Refine, välj <code>Create Project > Web Addresses (URLs)</code> och klistra in följande url: <code>http://jensfinnas.github.io/refine-regex-tutorial/data/anföranden_2013-2014.xml</code>.
![Välj fil](http://jensfinnas.github.io/refine-regex-tutorial/images/02xml.png)
__Källa:__ http://data.riksdagen.se/Data/Anforanden/
![Granska data](http://jensfinnas.github.io/refine-regex-tutorial/images/03import.png)


### Formatera datum korrekt
Klicka på kolumnen __anforande - dok_datum__ och välj sedan  __Edit column > Add column based on this column__.
![Formatera datum korrekt](http://jensfinnas.github.io/refine-regex-tutorial/images/04parsedate.png)

Applicera följande kod: <code>value.toDate()</code>.

Vi kan nu filtrera på datum. Klicka på den nya kolumnen __Datum__ (eller vad du valde att kalla den) och välj __Facet > Timeline facet__.
![Filtrera på datum](http://jensfinnas.github.io/refine-regex-tutorial/images/05filterdate.png)

### Filtrera på ett parti eller annan kategori
Klicka på __anforande - parti__ och välj __Facet > Text facet__.
![Filtrera på parti](http://jensfinnas.github.io/refine-regex-tutorial/images/06filterparty.png)

Vi kan nu välja att endast visa anföranden från ett visst parti från en viss tid.

### Reguljära uttryck
Se till att du inte har några aktiva facets. Klicka på __anforande - anforandetext__ och välj __Edit column > Add column based on this column__. Applicera följande kod. Välj __Jython__ som språk den här gången.

![Skriv regex](http://jensfinnas.github.io/refine-regex-tutorial/images/07regex.png)

<pre><code>import re
return re.search("([Ll]andsbygd)",value).group(0)
</code></pre>
Vi har nu skapat en ny kolumn som innehåller ordet "landsbygd" eller "Landsbygd" om det ingick i anförandet. Vi kan nu applicera ett __text facet__ på den här kolumnen och på partikolumnen för att se vilka partier som använder det här ordet mest.

![Partifilter](http://jensfinnas.github.io/refine-regex-tutorial/images/08regexfilter.png)

Här är ett exempel på ett lite mera avancerat reguljärt uttryck.
<pre><code>import re
return re.search("^(\S{3,4}) talman",value).group(1)
</code></pre>

Här söker vi efter

1. <code>^</code> början på en rad
2. <code>\S{3,4}</code> tre eller fyra tecken som inte är mellanslag.
3. <code> talman</code> följt av mellanslag talman.
4. <code>()</code> anger att det är bara ordet inom parentesen som vi vill fånga in.
