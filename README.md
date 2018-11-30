#Daily inventory check and email update

This script checks inventory form manually updated .xlsx file and sends predefined email to headquarters with updated stocks. Ideally the won't be needed to edit the email sketch, but in case of unexpected situations there is an option to edit the mail or add something.

#How it works

Program will first load the file with Pandas and search for current date, as the mail is being sent at closing the store. Then, the specific row will be added to predefind .txt file with the rest of the message and sent. If there will be need, there will be an option to edit the message before sending.
