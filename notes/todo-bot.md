

# Next - ingest.py
* stub out extract unit tests

* add file processing for

	* xls (skip)
	* plug back in (pdf ext)
		* refactor to test?
		* refactor to types?
	* filter to text
	* pdf meta data from es_pdf_meta data
		* msg /text and generic - 
		* word
		* pdf
		* pdf ocr (config)
	* TODO - extract other meta data
	* TODO - add to index

* core file and unit test
* add python types / safety

* Add
	* read skip list for confi.ini´
	* extract topics (using ) and index topics `
		* * sentiment etc from calc_sentiment.py



* Pull overwrite example back into normal example (for config files and sample data)

# Later
	* update promot
		* add topics
		* remove dear sir / signed bot
	* [later] map topics to emails / areas of interest
		* decide how to list topics
	* read info from key excel files (like questions or topics)

* Final Decide folderstruture
	* some sort of .ini file
		* keywords / topics
		* name of owner ?? or keep that in 


# NEXT - bot.py

* move to unit testable 
	* define method

* prepare for save back into excel
	* data gather (response, links, question used)
	* unit test prope

* get topics from emails

* create excel loop
	* put in random timer

# NEXT CYA on copilot
	* Get multple copilot keys
	* save to pickle
	* randomly use


# Next - Infrastructure
	# link to improvement form
	# how part of power automate flow


# Improvements - later priority
* move Textract to appraoch that will work on windows
* NTH - identify topci
* Prompts
* email templates
* links in email templates
* langchain
* more filtering based on updated xl
* categorisation of emails (to person best able to answer them)
* loop and see if we can improve (langchain)

# Improvements - later NTH
* Llama 3
* named entities
* Topic analysis
* ?? Misfiled emails
* ?? unanswered emails
* POS tagging (counties but other keywords)
* Postive or negative sentiment
* LEO / County


## next Problems I want to solve
* get list of attached filenames
* Emails without a response
* Emails filed in the wrong folder
* link email in chain (and recognize text)
* suggest best email response (to draft?)
* tag based on last person to answer client

* identify most relevant colleauges
* Save attachments / call rules?
* identify topics / keywords






