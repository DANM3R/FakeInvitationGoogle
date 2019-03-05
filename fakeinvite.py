import smtplib, os, sys

def main(gmail_user, gmail_password, to):
	sent_from = gmail_user
	from_name = input("Enter FROM NAME recipient will see in his email (press enter for default from name): \n")
	if from_name == '':
		from_name = 'Google CEO'

	subject = input("\nEnter subject of email (press enter for default subject): \n")
	if subject == '':
		subject = 'Invite to Google'

	body = input("\nEnter message body (press enter for default message): \n")

	if body == '':
		body = 'Hey man! Have you ever wanted to work in Google?\nGoogle invites you to meeting for a job at Mountain View CA at April 8.\nAll the costs for a plane and moving to hotel are on us. More information will be going soon.\nSee you in Google!'

	os.system('cls')

	msg = "\r\n".join([
		"From: " + from_name,
		"To: " + to,
		"Subject: " + subject,
		"",
		body
	])

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, msg)
		server.close()

		print('[*] Email sent!')
	except:
		os.system('cls')
		print('[*] Wrong email address or password...')
		sys.exit()


if __name__ == "__main__":
	os.system('cls')
	gmail_user = input('Enter your email address: \n')
	gmail_password = input('\n\nEnter your password: \n')
	to = input('\n\nEnter recipient address: \n')
	os.system('cls')

	main(gmail_user, gmail_password, to)