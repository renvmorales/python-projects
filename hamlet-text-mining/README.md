# hamlet-text-mining

This is a simple text mining and analysis of Shakespeare's **Hamlet** using `python3`. In here, I used this [online open version](http://erdani.com/tdpl/hamlet.txt) where the whole play in English version is available in `txt` format. In order to download the full text, I connected the `requests` module to the url address.




## Text preprocessing

A very brief preprocessing was applied to the full text: all punctuation characters were removed, and abbreviation names were converted back to real names. Consequently, abbreviations such as **_Ham._** or **_Oph._** are converted to **_Hamlet_** and **_Ophelia_** for instance. This is an important step, since abbreviations can be appears several times announcing each character lines (specially true for Hamlet!), and therefore, the total counts for the respective name can be miscounted.

Once preprocessing is complete, a total number of **31953 words** was found.



## Word Counts
All words in upper case mode were counted. The following table list in descending order the top 10 most frequent used words.


Word   | Word_Count
:------: | :---------:
THE        | 1090
AND        |  964
TO         |  742
OF         |  675
I          |  577
A          |  558
YOU        |  554
MY         |  520
HAMLET     |  465
IN         |  434
