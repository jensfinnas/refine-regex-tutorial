Tutorial: Regular Expressions in Open Refine
===============================


__Data:__ http://data.riksdagen.se/Data/Ledamoter/

<pre><code>import re
return re.search("(Herr) talman", value).group(1)
</code></pre>
