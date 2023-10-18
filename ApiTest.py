import irc.bot
import re
import os

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        server = 'irc.chat.twitch.tv'
        port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)
        self.channel = '#' + channel
        self.questions = []

    def on_welcome(self, connection, event):
        connection.join(self.channel)
        print(f"Connected to {self.channel}!")  # Print message when connected

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        if self.is_question(message):
            self.questions.append(message)
            print(f"Added question: {message}")  # Print the question to console

            # Respond to the question (100% chance)
            question = self.questions.pop()  # Remove and get the last question
            connection.privmsg(self.channel, f"Answering question: {question}")

    @staticmethod
    def is_question(message):
        return bool(re.search(r'\?$', message))

def main():
    username = 'rockochamp'
    token = os.getenv("TWITCH_OAUTH_TOKEN")
    channel = 'Rockochamp'

    bot = TwitchBot(username, token, channel)
    bot.start()

if __name__ == "__main__":
    main()
