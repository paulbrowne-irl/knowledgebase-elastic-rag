import logging
import traceback
from pandas.core.frame import DataFrame

import pandas as pd

import win32com.client
import os.path

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

import settings

counter=0

'''
Save Dataframe to disk
'''
def _save_email(data_frame):

    print("Saving Dataframe size:"+str(data_frame.size))
    try:
        with pd.ExcelWriter(settings.EMAIL_DATA_DUMP,mode='a',if_sheet_exists="replace") as writer:  
            data_frame.to_excel(writer, sheet_name='Sheet1')
            print("Flushed Cache to disk")
        
            
    except Exception as err:
        
        print ("Error when saving data")
        print (print(traceback.format_exc()))
        print ("\n Was attempting to save")
        print(data_frame.tail(settings.FLUSH_AFTER_X_MAILS))

    return data_frame


'''
Walk folder recursively
'''
def _walk_folder(data_frame,parent_folder,this_folder):
    
    global counter
    
    # Walk and print folders
    for folder in this_folder.Folders:
        print (folder.Name)
        
        #Do recursive call to walk sub folder
        data_frame = _walk_folder(data_frame,parent_folder+"::"+folder.Name,folder)

    #Print folder items
    folderItems = this_folder.Items
 
    for mail in folderItems:

        try:
            #Increment the counter and test if we need to break
            counter+=1

            print("Counter:"+str(counter))
            if(settings.BREAK_AFTER_X_MAILS>0 and counter>settings.BREAK_AFTER_X_MAILS):
                print("Breaking ...")
                return data_frame
            
            #do we need to flush cache to disk?
            if(counter%settings.FLUSH_AFTER_X_MAILS==0):
                data_frame = _save_email(data_frame)

            #Filter on mail items only
            if(mail.Class!=43):
                print("Skipping item type:"+str(mail.Class))

            else:
            
                ## get multiple values


                new_row = pd.DataFrame( {'Parent':[parent_folder],
                        'Subject':[""+str(mail.Subject)],
                        'To':[""+str(mail.To)],
                        'CC':[""+str(mail.CC)],
                        'Recipients':[""+str(mail.Recipients)],
                        'RecievedByName':[""+str(mail.ReceivedByName)],
                        'ConversationTopic':[""+str(mail.ConversationTopic)],
                        'ConversationID':[""+str(mail.ConversationID)],
                        'Sender':[""+str(mail.Sender)],
                        'SenderName':[""+str(mail.SenderName)],
                        'SenderEmailAddress':[""+str(mail.SenderEmailAddress)],
                        'attachments.Count':[""+str(mail.attachments.Count)],
                        'Size':[""+str(mail.Size)],
                        'ConversationIndex':[""+str(mail.ConversationIndex)],
                        'EntryID':[""+str(mail.EntryID)],
                        'Parent':[""+str(mail.Parent)],
                        'CreationTime':[""+str(mail.CreationTime)],
                        'ReceivedTime':[""+str(mail.ReceivedTime)],
                        'LastModificationTime':[""+str(mail.LastModificationTime)],
                        'Categories':[""+str(mail.Categories)],
                        'Body':[""+ILLEGAL_CHARACTERS_RE.sub(r'',str(mail.Body))]       #try to resolve erros

                        })
                
               
                data_frame= data_frame.append(new_row,ignore_index=True)
                #data_frame = pd.merge([data_frame,new_row])

        except Exception as e:
            print("error when processing item - will continue")
            print(e)

            
            #HTMLBody
            #RTFBody


    return data_frame
           
        

'''
Output from Outlook Into Excel
'''
def export_email_to_excel(OUTLOOK):
    
    
    #debugging
    #root_folder = .Folders.Item(1)
    print("Getting handle to outlook");
    root_folder = OUTLOOK.Folders.Item(settings.INBOX_NAME)

    #Create data frame and save to disk to wipe any previous values
    df = pd.DataFrame()
    df.to_excel(settings.EMAIL_DATA_DUMP)


    #Walk folders
    print("About to walk folder");
    new_data = _walk_folder(df,"",root_folder)

    #Save the final batch of new data
    _save_email(new_data)

    #Print a sample of the data
    print("complete - sample data")
    print(new_data)



# simple code to run from command line
if __name__ == '__main__':
    
    ## Module level variables
    counter=0

    #Handle TO Outlook, Logs and other objects we will need later
    OUTLOOK = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    logging.basicConfig(filename=settings.LOG_FILE, encoding='utf-8', level=logging.DEBUG)

    #Set the working directory
    os.chdir(settings.WORKING_DIRECTORY)
    print ("\nSet working directory to: "+os.getcwd())

    # Carry out the steps to sync excel adn outlook
    # ear_excel.clear_excel_output_file()
    export_email_to_excel(OUTLOOK)
    





