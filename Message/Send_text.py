from twilio import rest

account_sid = "AC1f0d9952f4674335f4d037f41caa7e20" # Your Account SID from www.twilio.com/console
auth_token  = "0b43f0d38b3f4cb7b65739d4f59f87bb"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="chodu",
    to="+19733421336",    # Replace with your phone number
    from_="+12016133394 ") # Replace with your Twilio number

print(message.sid)
