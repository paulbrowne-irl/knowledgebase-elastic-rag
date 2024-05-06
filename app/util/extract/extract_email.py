import extract_msg


def extract_text_email(filename: str) -> str:
    '''
    extract information from email body
    '''

    # extract the info
    msg = extract_msg.Message(filename)

    # build up text - bringing the most useful info through first

    text = msg.subject
    text +=msg.body

    #close file before return
    msg.close()

    return text