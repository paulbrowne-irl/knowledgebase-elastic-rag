

# Next - ingest.py

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

* Decide folderstruture
	* some sort of .ini file
		* keywords / topics
		* name of owner ?? or keep that in 

* Pull overwrite example back into normal example (for config files and sample data)

# Later
	* [later] map topics to emails / areas of interest
	* read info from key excel files (like questions or topics)


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


# add todo
* move Textract to appraoch that will work on windows
* NTH - iden

# Improvements - later
* Prompts
* email templates
* links in email templates
* langchain
* more filtering based on updated xl
* categorisation of emails (to person best able to answer them)
* loop and see if we can improve (langchain)
* Llama 3


# Next - Infrastructure
	# link to improvement form
	# how part of power automate flow
==


## play

* named entities
* Topic analysis

## Now problems I want to solve

* Misfiled emails
* unanswered emails
* POS tagging (counties)

## Tidy

* failing when trying to output non email tasks


## next Problems I want to solve
* get list of attached filenames
* Emails without a response
* Emails filed in the wrong folder
* link email in chain (and recognize text)
* suggest best email response (to draft?)
* tag based on last person to answer client
* Postive or negative sentiment
* LEO / County
* identify DA
* Save attachments / call rules?
* identify topics / keywords

## Open Questions and Features

* Anywhere to run other than laptop
* Incremental v full run tasks
* Configure filter out of email
* remove boiler plate email

## Notes

* Possible use Graph Library instead: https://github.com/O365/python-o365#mailbox




