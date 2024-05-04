

# Next - ingest.py

* unit tests
	* stub out simple tests for each (call main convertor, test text, print text)

* add file processing for

	* pdf multiple pages (based on es_pdf_meta_data)
	* meta data all files
		* based on  from es_pdf_meta_data
		* anything we can add for msg/text/generic, word, pdf ?
	* TODO - sentiment etc from calc_sentiment.py
	* TODO - add to index
		* main
		* sentiment etc


* Comopare work and normal example (for config files and sample data)
* run and review index

# NEXT - bot.py

* upgrade and tidy
* 	* move to unit testable 
	* define method
	* add (more) python types / safety (like on injest)

* get topics from emails using injest method

* write better questions
	* sample
	* real folder (mounted onedrive)

* create excel loop
	* put in random timer

* prepare for save back into excel
	* data gather (response, links, question used)
	* unit test prope

# NEXT CYA on copilot
	* Get multple copilot keys
	* save to pickle
	* randomly use


# Next - Infrastructure
	# link to improvement form
	# how part of power automate flow


# Later - Iterate
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






