
# NEXT - bot.py

* move to unit testable 
	* define method

* prepare for save back into excel
	* data gather (response, links, question used)
	* unit test prope

* create excel loop
	* 
	* put in random timer

* CYA on copilot
	*  Get multple copilot keys
	* save to pickle
	* randomly

# Next - injust.py
* stub out main class - walker
	* link in with pdf
	* updgrade / repeat for other types of files
		* word - using last weeks project
		* pdf
		* text
		* email	
	* core file and unit test

* stub out data folderstruture
	* some sort of .ini file
		* keywords / topics
		* name of owner ?? or keep that in 
		[later] do I index emails?

* current data examine




# Gather data
* GS
* Sharepoint
* SMR
* rememver bits form emails send

# Next index data
* better ingestion app - using existing pdf and other readers
* pull together sample data from public - for use on blacktlaop
* tests of different scenarios

# add todo
* update notes below on what script does
* NTH - iden

# Improvements - later
* Prompts
* email templates
* links in email templates
* langchain
* more filtering based on updated xl
* categorisation of emails (to person best able to answer them)
* loop and see if we can improve (langchain)



# Next - ingestion scripts
	# name of root folder to ingest from

# Next - Infrastructure
	# link to improvement form
	# how part of power automate flow
==

# constants
	# name of inbox / sharepoint list
	# name of follow up person
	# name of folder to move completed emails to
	# standard email template(s)
		# in process
		# “things that I know about”
		# we monitor the email inbox – keep it professional 
	# name of knowledgebase

# Open Sharepoint list

	# loop through all messages

		# filter based on internal emails only
		# filter based if there is an “auto response” text (i.e. don’t get stuck in loop)
		# RAG 1 Find x amount of relevant documents
		# RAG 2 Pass to AI to generate email
		# Generate Email , save to draft


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




