# hamlet-text-mining

This is a simple text mining and analysis of Shakespeare's **Hamlet** using `python3`. In here, I used this [online open version](http://erdani.com/tdpl/hamlet.txt) where the whole play is available in `txt` format. In order to download the full text, I connected the `requests` to the url address.



## Preprocessing

A very brief preprocessing was applied to the full text: all punctuation characters were removed, and abbreviation names were converted back to real names. Consequently, abbreviations such as **Ham.** or **Oph.** are converted to **Hamlet** and **Ophelia** for instance. This is an important step, since abbreviations can be appears several times announcing each character lines (specially true for Hamlet!), and therefore, the total counts of the respective name can be miscounted.


