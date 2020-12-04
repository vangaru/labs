emails = ['ivanenko0607@gmail.com', 'svanfilets@g.bstu.by', 'iigladkiy@tut.by']
domens = []
for email in emails:
	domens.append(email[email.find('@') + 1::])
print(domens)