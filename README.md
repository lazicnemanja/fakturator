# Fakturator
Invoice generator

Generete Word .docx invoice with placeholders.

Current placeholders:

* **{invoice-no}**
* **{completion-date}** 
* **{issued-date}** 
* **{deadline-date}**
* **{from-date}**
* **{to-date}**
* **{nbs}** *official middle rsd exchange rate* 
* **{nbs-date}** *date when middle rsd exchange rate is formed*
* **{eur}** *user input*
* **{rsd}** *conversion to rsd by exchange rate*

## run
> python main.py n (n=float)
