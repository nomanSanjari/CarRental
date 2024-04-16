import aiosmtplib
from email.mime.text import MIMEText


async def send_acceptance_email(recipient, subject, body):
	message = MIMEText(body)
	message['Subject'] = subject
	message['From'] = 'nomansanjari2001@gmail.com'
	message['To'] = recipient

	async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587) as server:
		await server.login('nomansanjari2001@gmail.com', 'ttfgnbtjykxedjzp')
		await server.send_message(message)


async def send_rejection_email(recipient, subject, body):
	message = MIMEText(body)
	message['Subject'] = subject
	message['From'] = 'nomansanjari2001@gmail.com'
	message['To'] = recipient

	async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587) as server:
		await server.login('nomansanjari2001@gmail.com', 'ttfgnbtjykxedjzp')
		await server.send_message(message)
