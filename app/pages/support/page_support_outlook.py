import logging

import pandas as pd
import pythoncom
import settings.config as config
import win32com.client

'''
Supporting Outlook functionality for pages in Streamlit

Done this way as support helper (and not service) as it needs to run on Windows clinet to access Outlook
'''

# Load config on startup
BREAK_AFTER_X_MAILS = config.read_int("BREAK_AFTER_X_MAILS")
MAILBOX_NAME = config.read("MAILBOX_NAME")
FOLDER_NAME = config.read("FOLDER_NAME")

#Other constants
DEFAULT_EMAIL_RESPONSE = "This is a default email response while we generate a more appropriate answer"

# Module level variables
counter = 0


'''
Gather email information from Outlook Into Data frame

'''
def loop_through_outlook_emails(call_llm=True,draft_email=False)->pd.DataFrame:

    # Create data frame and save to disk to wipe any previous values
    df = pd.DataFrame()

    # Get Handle To Outlook
    logging.info(f"Getting handle to Outlook, will try to open Mailbox {MAILBOX_NAME}")
    logging.info(f"Will Break after email number {BREAK_AFTER_X_MAILS}")
    
    OUTLOOK = win32com.client.Dispatch(
        "Outlook.Application", pythoncom.CoInitialize()).GetNamespace("MAPI")
    root_folder = OUTLOOK.Folders.Item(MAILBOX_NAME)

    # Walk folders
    logging.debug("About to walk folder")
    new_data = _walk_folder_gather_email_values(df, "", root_folder)
    
    # release COM Object
    OUTLOOK = None

    logging.info("\nComplete\n")

    return new_data


'''
Walk Outlook  folder recursively and extract information into a dataframe
'''
def _walk_folder_gather_email_values(data_frame, parent_folder, this_folder)->pd.DataFrame:

    global counter

    # Walk and print folders
    for folder in this_folder.Folders:
        logging.debug(folder.Name)

        # Do recursive call to walk sub folder if matches
        if (folder.Name == FOLDER_NAME):
            logging.debug(f"Processing folder {folder.Name}")
            data_frame = _walk_folder_gather_email_values(
                data_frame, parent_folder+"::"+folder.Name, folder)
        else:
            logging.debug(f"Skipping folder {folder.Name}")

    # Print folder items
    folderItems = this_folder.Items

    for mail in folderItems:

        try:
            # Increment the counter and test if we need to break
            counter += 1

            logging.debug("Counter:"+str(counter))
            if (BREAK_AFTER_X_MAILS > 0 and counter > BREAK_AFTER_X_MAILS):
                logging.info(f"Breaking after {counter} emails ...")
                return data_frame


            # Filter on mail items only
            if (mail.Class != 43):
                logging.debug("Skipping item type:"+str(mail.Class))

            else:

                # get multiple values

                new_row = pd.DataFrame({'Parent': [parent_folder],
                                        'Subject': [""+str(mail.Subject)],
                                        'To': [""+str(mail.To)],
                                        'CC': [""+str(mail.CC)],
                                        'Recipients': [""+str(mail.Recipients)],
                                        'RecievedByName': [""+str(mail.ReceivedByName)],
                                        'ConversationTopic': [""+str(mail.ConversationTopic)],
                                        'ConversationID': [""+str(mail.ConversationID)],
                                        'Sender': [""+str(mail.Sender)],
                                        'SenderName': [""+str(mail.SenderName)],
                                        'SenderEmailAddress': [""+str(mail.SenderEmailAddress)],
                                        'attachments.Count': [""+str(mail.attachments.Count)],
                                        'Size': [""+str(mail.Size)],
                                        'ConversationIndex': [""+str(mail.ConversationIndex)],
                                        'EntryID': [""+str(mail.EntryID)],
                                        'Parent': [""+str(mail.Parent)],
                                        'CreationTime': [""+str(mail.CreationTime)],
                                        'ReceivedTime': [""+str(mail.ReceivedTime)],
                                        'LastModificationTime': [""+str(mail.LastModificationTime)],
                                        'Categories': [""+str(mail.Categories)],
                                        # try to resolve erros
                                        'Body': [""+str(mail.Body)]

                                        })

                

                data_frame = pd.concat([data_frame, new_row], ignore_index=True)


        except Exception as e:
             logging.error("error when processing item - will continue")
             logging.error(e)

    print(f"Data_frame size before return: {data_frame.size}")    

    return data_frame

def _draft_response_to_single_email():
    pass


'''
 simple code to run from command line

 We include this since we *don't* have unit test (it would fail on non Windows non Outlook PC)

'''
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #call the main method in this module
    myBot = Bot_Static()
    myBot.loop_answer_questions_from_source()

