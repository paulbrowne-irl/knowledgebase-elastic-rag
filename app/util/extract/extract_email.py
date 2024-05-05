import extract_msg


def extract_text_email(filename: str) -> str:
    '''
    Catch all method for extracting info using textract
    '''

    f = r'MS_Outlook_file.msg'  # Replace with yours
    msg = extract_msg.Message(f)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = msg.body
    msg.close()

    print('Sender: {}'.format(msg_sender))
    print('Sent On: {}'.format(msg_date))
    print('Subject: {}'.format(msg_subj))
    print('Body: {}'.format(msg_message))
    
    return msg_message