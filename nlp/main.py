from beautifulsoup import bs_time
from spacy_time import spacy_time


html_doc = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="author" content="Jacopo Urbani">
        <link rel="icon" href="data:,">

        <title>Jacopo Urbani</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        <link href="/css/style.css" rel="stylesheet">
    </head>

    <body class="d-flex flex-column min-vh-100">


            
<p><img alt="me" class="img-thumbnail rounded float-end" style="width: 200px" src="img/me.jpg"/> I am an assistant professor in Computer
Science at the <a href="http://www.cs.vu.nl">Vrije Universiteit Amsterdam</a>
(VUA) and a guest researcher at <a href="http://www.cwi.nl/">CWI</a>.</p>

<p>My research focuses on how to extract <em>new (and interesting)
knowledge</em> from large datasets which are primarily available on the Web. If
you are interested, please check out my publication list on <a
href="https://scholar.google.ca/citations?user=5o88MDIAAAAJ&hl=en"
target="_blank">Google Scholar</a> or <a
href="http://dblp.uni-trier.de/pers/hd/u/Urbani:Jacopo"
target="_blank">DBLP</a> to have a better idea of my research area.</p>

<p>I received a number of awards for my research. A few papers that I
co-authored have received either a honorable mention or a best paper award at
top conferences. In 2010, my work on forward inference with MapReduce has won
the IEEE SCALE challenge. In 2012, the <a
href="http://www.networkinstitute.nl">Network Institute</a> awarded me the
prize &#8220;Most Promising Young Researcher Award&#8221;. In 2013, my PhD was
awarded with the qualification <em>cum laude</em>, which was given only to 5%
of the theses in our department. In 2014, my PhD work received an <a
href="http://www.christiaanhuygensprijs.nl/index.php?D=112">honourable
mention</a> as best PhD thesis in Computer Science in the country. The award
was given by the Christiaan Huygens society, after a selection performed by
KNAW (Royal Netherlands Academy of Arts and Sciences).</p> 

    </body>
</html>
"""

doc = bs_time(html_doc)
# print('Stripped of HTML: \n', doc)
spacy_time(doc)
