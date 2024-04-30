

# NEXT

* allow for EI sepecif overwrite - impl 
* work throiugh comments in bot.py

# Next After this
* create pickle folder
* better ingestion app

# Next sample data
* pull together sample data from public - for use on blacktlaop
* tests of different scenarios

# add todo
* update notes below on what script does
* 


Power automate scripts neede

===.

# ingestion scripts
	# name of root folder to ingest from
# Infrastructure
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


# Also needed
*  Power Automate Scripts

===

Previous ideas emails - tidy 

# Structure

* Generate Data as table
* some reporting / training against table (Excel , Powerapp or other)
* some feedback loop on recommendations
* email draft suggestions (no install by other users)
* add powerapp trigger

## From "Unlocking Text Data with deep learning (Apress)

* Tidy these
**p38 convert data to lowercase
**p41 Remove punc
**p43 Remove stop words
**p47 ??tokenize text
**Opt: p47/50 Spelling/standardizing/stemming/lemmetizing


## Next
* try group by https://realpython.com/pandas-groupby/
* Try Sentiment analysis

## play

* named entities
Topic analysis

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


		