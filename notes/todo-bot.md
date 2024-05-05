

* NEXT 
* work through setup (textract and make notes)

* get tests working again
	* first pass tidy at both
	* unit tests calling AND/ OR main method test


# Next - DATA CAPTURE INTO INDEX

* ?? create dictionary of meta data to be added

* add file processing for

	* pdf and for txt (or just text)

	* write up both
		* text - add file meta data
		* pdf - add ?? from text
	* ensure we have a link back to source
	* unit test both (Ccomplete)
	* link in both to indjext


	* meta data all files -> index
		* based on  from es_pdf_meta_data
		* anything we can add for msg/text/generic, word, pdf ?
		
	* TODO - from calc_sentiment.py
		* get topics from emails using injest method
		* sentiment etc f
	* TODO - add to index
		* main
		* sentiment etc


* Comopare work and normal example (for config files and sample data)
* run and review index

# NEXT
* Examine indexing results
* Iterate


# NEXT - BOT SEARCHING AGAINST INDEX

* upgrade and tidy
* 	* move to unit testable 
	* define method
	* add (more) python types / safety (like on injest)



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

* Get unit tests working agiain

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






