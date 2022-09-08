# Arbetsflöde för AI-projekt

## Hämta datan ##

På [Hemnet.se](https://www.hemnet.se/salda/bostader?) kan man hitta slutpriser på alla bostäder som sålts. Man kan med urlopen hämta HTML för söksidan och sedan med BeautifulSoup konvertera informationen i HTML till LXML [[1]]. Genom LXML kan man i sin tur enklare extrahera informationen man söker. Ett sätt att samla in alla features (rum, yta, region o.s.v.) är att köra flera sökningar på Hemnet med filters för de features man vill titta på, och sen spara slutpriser från sökningen i separata listor. Problemet är att man då måste skapa massivs av listor manuellt för att täcka alla features.

Ett smartare tillvägagångssätt är att inte alls filtrera i slutpriserna på Hemnet utan istället göra filtreringen direkt i python genom att kombinera formatet LXML med regular expressions [[1]].

## Visualisera datan ##

Man kan visualisera datan med Matplotlib i python.

För kontinuerliga features kan man skapa separata scatter plots. Då har man alltså slutpris på en axel och feature (exempelvis yta) på andra axeln, vilket ger en bild av dess samband. Man skulle också kunna lägga till en kategorisk feature (exempelvis antalet rum) genom infärgning av punkter [[2]].

För kategoriska utfall kan man använda boxplots [[3]]. I en boxplots får man en bild av fördelningen av värden i en kategori, och skillnader mellan kategorier.

Genom att visualiera datan på detta sätt kan man observera de samband man vill explorera, men det kan också vara ett bra sett att identifiera outliers eller eventuella problem i datan.

## Bearbeta datan ##

När vi inspekterar datan kan vi upptäcka felaktigheter, outliers eller att features saknas saknas i vissa objekt. Dessa problem måste lösas genom att korrigera felaktigheter och imputera missing features om det kan göras på ett bra sätt [[1]]. Alternativt får man exkludera dessa objekt från vissa analyser.

När steget att hämta datan (med urlopen + BeautifulSoup + regular expressions) är klart har vi den i form av listor. Ett bättre format för analys är att ha all data summerad i en dataframe. Med Pandas kan de insamlade listorna konverteras till en dataframe [[1]]. Slutligen kan dataframe exporteras till CSV- eller excel-fil för att underlätta hanteringen av datan [[4]].

## Linjär regression ##

Linjär regression är en typ av supervised learning då man tränar en modell med data där "utfallet" är känt. Metoden försöker hitta ett linjärt samband mellan en dependent variable (y) och en independent variables (x). På så vis kan den erhållda modellen sedan användas för att predicera nya utfall, givet variabeln som använts för att träna modellen.

Sambandet hittas genom att minimera en cost function med gradient descent för att hitta koefficienten som ger "best fit line" [[5]].

## Implementering ##

Med multiple linear regression kan modellen inkludera flera independent variables (x1, x2, ..., xn). Detta gör att samband mer komplexa än en linje kan exploreras. Med två eller fler features representeras sambandet istället av ett hyperlane [[6]].

Multiple linear regression kan tränas och utvärderas med funktioner från Scikit-Learn och NumPy [[6]]. Datan delas in i träning- och test-data. Modellen skapas genom att anpassas till träningsdatan, beskrivet ovan, och utvärderas sedan genom prediktion av utfall i testdatan.

Slutligen implementerar man modellen genom att hämta features från Hemnet för objekt som ännu inte är sålda. Genom att sortera objekten efter skillnad mellan utgångspris och predicerat slutpris kan man hitta prisvärda objekt. Man bör dock påpeka att det finns mängder av variabler med påverkan på pris, som inte kan utrönas från bara annonser.

## Källor ##

[[1]]: https://www.xbyte.io/how-to-use-python-to-scrape-real-estate-website-data-using-web-scraping-and-making-data-wrangling.php

[1]: https://www.xbyte.io/how-to-use-python-to-scrape-real-estate-website-data-using-web-scraping-and-making-data-wrangling.php

[[2]]: https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/

[2]: https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/

[[3]]: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/

[3]: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/

[[4]]: https://www.geeksforgeeks.org/how-to-export-pandas-dataframe-to-a-csv-file/

[4]: https://www.geeksforgeeks.org/how-to-export-pandas-dataframe-to-a-csv-file/

[[5]]: https://www.geeksforgeeks.org/ml-linear-regression/

[5]: https://www.geeksforgeeks.org/ml-linear-regression/

[[6]]: https://www.machinelearningworks.com/tutorials/multiple-linear-regression

[6]: https://www.machinelearningworks.com/tutorials/multiple-linear-regression
