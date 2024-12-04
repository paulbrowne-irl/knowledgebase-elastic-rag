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

# Module level variables
counter = 0


'''
Gather email information from Outlook Into Data frame
'''


def loop_through_outlook_emails()->pd.DataFrame:

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
    print(f"Data_frame size after walk: {new_data.size}")

    # Print a sample of the data
    logging.debug("complete - sample data")
    logging.debug(new_data)

    # release COM Object
    OUTLOOK = None

    logging.info("\nComplete\n")

    return new_data


'''
Walk Outlook  folder recursively and extract information into a dataframe
'''
def _walk_folder_gather_email_values(data_frame, parent_folder, this_folder)->pd.DataFrame:

    print(f"Data_frame size on entry: {data_frame.size}")

    global counter

    # Walk and print folders
    for folder in this_folder.Folders:
        logging.debug(folder.Name)

        # Do recursive call to walk sub folder
        data_frame = _walk_folder_gather_email_values(
            data_frame, parent_folder+"::"+folder.Name, folder)

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

            # do we need to flush cache to disk?
            # if(counter%settings.FLUSH_AFTER_X_MAILS==0):
            #     data_frame = _save_email(data_frame)

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
                print(f"Data_frame size: {data_frame.size}")
                # data_frame = data_frame.append(new_row, ignore_index=True)
                # data_frame = pd.merge([data_frame,new_row])

        # except Exception as e:
        #     logging.error("error when processing item - will continue")
        #     logging.error(e)

    print(f"Data_frame size before return: {data_frame.size}")    

    return data_frame
