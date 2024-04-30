import logging

'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

[later]
* identify topics
* idetnify best person to answe
* loop and see if we can improve (langchain)

[indexing]
* grab 

'''

# read excel file

# read email and prompt templates



# identify unprcessed email

# Loop


    # call via chain

    # upate sheet

    # on to next

'''
==.

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

'''


