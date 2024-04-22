# Sync Outlook Tasks with Excel

Synchronize Outlook Tasks folder with an Excel file.

## Why would I want to do this?

[GTD (Getting things done)](https://en.wikipedia.org/wiki/Getting_Things_Done) and other time / task / personal productivity approaches underline the importance of a Single Todo List, not your email inbox, that is easy to add to and is accessible anywhere.

The tasks screen of Outlook allows you to do this very well, but is tied to your PC. The mobile version (Microsoft Todo app) syncs well, but does not bring all the information through - e.g. does not allow you to categorize your tasks.

Since this script synchonizes Outlook Tasks with an Excel file, it allows you to do the following things:

1. Bulk update of tasks using Excel, easier to edit than the Outlook Interface.
1. Allows you to backup Tasks if you accidentally delete them in Outlook.
1. By saving to OneDrive, Google Drive or similar, it makes one tasklist available across multiple devices.

## What this Python Script does

Given a typical Outlook Task folder like this:

![Outlook Tasks Screenshot](images/outlook-tasks.png)

The script synchronizes (2 way) with an Excel file like the one below. Of course a typical todo / task list could have a hundred (or more items).

![Excel Tasks Screenshot](images/excel-tasks.png)

## 2 Way Synchonization - Safety first

By "2 Way" we mean that edits in Outlook or the Excel file get synchonized with each other, back and forward. But for safety first, we treat the Outlook Task list as the 'gold' copy. 

### Synchronisation process

* Script loops through Tasks in Outlook, checking the unique EntryID
  * Script searches the Excel file (normally ``task-data.xls`` ) for any Tasks matching this ID
  * Script tries to update the Outlook task __only if__ a matching task in Excel has __Modified set to Y__
* Script makes a backup copy of any previous Excel file. e.g. copy ``task-data.xls`` to ``1task-data.xls``, etc
* Script makes a template from the previous Excel sheet (``task-data.xls``) - deletes out all data except the first row, keeping  formatting, filters etc.
* For all Outlook Tasks, the Script outputs selected fields to this Excel file.
* Following the 'Outlook is Gold' approach, this script
  * Does not delete in Outlook any task deleted in Excel - since we could mistakenly delete a new Outlook task, created after the Excel List was exported.
  * Does not add to Outlook, and task added to Excel - since we could mistakenly add back a task we decided to delete in Outlook
  * Script only updates from Excel into Outlook if the Modified Column in the Excel spreadsheet has been set to Y.

## How to Install and Use

1. Make sure you have Outlook on your machine -(doh!)
1. [Install Python](https://www.python.org/downloads/) on your machine.
1. Make sure you have the required libraries - typically this will be something like ``pip install pandas openpyxl pywin32`` in a terminal.
1. Download the two files you need into a directory, listed at the top of the page
    * ``outlook.py`` - the actual sync script
    * ``task-data.xlsx`` - the Excel file that syncs with outlook
1. Run the script in a terminal using a command similar to ``python outlook.py``
   * By Default - the script will look for the template (task-data.xls) in the same directory as it is run. Log files and backups will also by placed in this directory.
   * Outlook.bat is there for convenience.

## Modifying the Script

The comments in the ``outlook.py`` script should make it pretty clear what is going on. The Excel file names, the log file names and backups are all set as constants at the top of the file (e.g. if you want change the Excel task file location).

If you want to extract / upload different properties from the Outlook tasks (e.g. percent complete), the pattern should be very familiar. The names used in code may differ in the Outlook object model from what you use in the Outlook Desktop interface. A link is given below to the Microsoft reference to help you.

## More Technical Information

The approach taken is to use the API provided by Outlook's COM model, rather than the newer Microsoft Graph API. The reason for this is that (currently) not all Task information is exposed by the Graph API - it appears to be limited to the few fields used in the Microsoft Todo app.

There is a lot of information on the Web describing PyWin32 - the library used to connect Python to Windows Applications like Outlook. There is less information on the Object Model within Outlook - and mostly it is intended for VBA and C# users (athough the method calls and params are very similar). Some good starting points used in creating this script:

* [Blogpost describing Outlook task manipulation in C#](https://www.add-in-express.com/creating-addins-blog/2013/06/12/outlook-tasks-create-get-delete/)
* [Microsoft Docs describing the Outlook Com Object model](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.outlook.mapifolder?view=outlook-pia)
