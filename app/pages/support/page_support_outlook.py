import logging

import pandas as pd
import pythoncom
import settings.config as config
import win32com.client
import pages.support.rest_client as rest_client

'''
Supporting Outlook functionality for pages in Streamlit

Done this way as support helper (and not service) as it needs to run on Windows clinet to access Outlook
'''

# Load config on startup
BREAK_AFTER_X_MAILS = config.read_int("BREAK_AFTER_X_MAILS")
MAILBOX_NAME = config.read("MAILBOX_NAME")
FOLDER_NAME = config.read("FOLDER_NAME")

#Other constants
DEFAULT_EMAIL_RESPONSE = "Default - email not generated yet"

# Module level variables
counter = 0

'''
Gather email information from Outlook Into Data frame

'''
def loop_through_outlook_emails(call_llm=True,outlook_draft_email=False)->pd.DataFrame:

    # Create data frame and save to disk to wipe any previous values
    df = pd.DataFrame()

    # reset counter to 0 for this loop
    global counter
    counter =0

    # Get Handle To Outlook
    logging.info(f"Getting handle to Outlook, will try to open Mailbox {MAILBOX_NAME}")
    logging.info(f"Will Break after email number {BREAK_AFTER_X_MAILS}")
    
    OUTLOOK_HANDLE = win32com.client.Dispatch(
        "Outlook.Application", pythoncom.CoInitialize()).GetNamespace("MAPI")
    OUTLOOK_ROOT_FOLDER = OUTLOOK_HANDLE.Folders.Item(MAILBOX_NAME)

    # Walk folders
    logging.debug("About to walk folder")
    email_data = _walk_folder_gather_email_values(OUTLOOK_HANDLE,df, "", OUTLOOK_ROOT_FOLDER,call_llm,outlook_draft_email)
    
    # release COM Objects
    OUTLOOK_ROOT_FOLDER = None
    OUTLOOK_HANDLE = None

    # filter the acutal columns we want to display
    #filtered_frame = email_data[['Subject', 'Sender','To','CC','Categories','Body','New Email Text','Outlook Generated Email']]
    filtered_frame = email_data

    logging.info("\nComplete\n")

    return filtered_frame


'''
Walk Outlook folder recursively and extract information into a dataframe
'''
def _walk_folder_gather_email_values(OUTLOOK_HANDLE,data_frame:pd.DataFrame, parent_folder:str, this_folder:str,call_llm:bool,outlook_draft_email:bool)->pd.DataFrame:

    global counter

    # Walk and print folders
    for folder in this_folder.Folders:
        logging.debug(folder.Name)

        # Do recursive call to walk sub folder if matches
        if (folder.Name == FOLDER_NAME):
            logging.debug(f"Processing folder {folder.Name}")
            data_frame = _walk_folder_gather_email_values(OUTLOOK_HANDLE,data_frame, parent_folder+"::"+folder.Name, folder,call_llm,outlook_draft_email)
        else:
            logging.debug(f"Skipping folder {folder.Name}")

    # Print folder items
    folderItems = this_folder.Items

    for mail in folderItems:

        # try:
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

                # generate email response if requested
                if call_llm==True:
                    new_email_text=rest_client.call_rest_to_get_email_draft(str(mail.Body))
                    
                else:
                    new_email_text=DEFAULT_EMAIL_RESPONSE

                # request outlook drafts email if requested
                if outlook_draft_email==True:
                    outlook_success= _generate_outlook_draft(OUTLOOK_HANDLE,mail,new_email_text)
                else:
                    outlook_success = False




                # get list of emails

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
                                        'Body': [""+str(mail.Body)],
                                        'New Email Text': [new_email_text],
                                        'Outlook Generated Email':[outlook_success]

                                        })



                

                data_frame = pd.concat([data_frame, new_row], ignore_index=True)


        # except Exception as e:
        #      logging.error("error when processing item - will continue")
        #      logging.error(e)

    print(f"Data_frame size before return: {data_frame.size}")    

    return data_frame


def _generate_outlook_draft(OUTLOOK_HANDLE,mail,suggested_new_email_text)->bool:
    logging.info("Would generate email in outlook")
    reply_draft= mail.ReplyAll() # was reply
    reply_draft.HTMLBody = suggested_new_email_text+ reply_draft.HTMLBody #was bodycls
    #reply_draft.From ="someotheremail@destiny.com"


    #move to drafts
    OUTLOOK_ROOT_FOLDER = OUTLOOK_HANDLE.Folders.Item(MAILBOX_NAME)
    drafts = OUTLOOK_ROOT_FOLDER.folders("Drafts") #if necessary

    
    reply_draft.Move(drafts)

    return True





