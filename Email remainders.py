def calculate_emails_to_send(total_participants, opted_out):
    emails_to_send = total_participants - opted_out
    return emails_to_send
total_participants=int(input("enter a total participants:"))
opted_out=int(input("enter a opted out:"))
emails_to_send = calculate_emails_to_send(total_participants, opted_out)
print(" emails to send:", emails_to_send)
