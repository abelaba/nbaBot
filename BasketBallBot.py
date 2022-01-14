import requests
import json
from datetime import datetime,timedelta
import emoji

class BasketBallBot:

    TOKEN = "5038117973:AAHl4kD1cZQ1FF6lGpcprH0X41qaK01i1qs"
    CHANNEL_CHAT_ID = "-1001737011581"
    URL = "https://balldontlie.io/api/v1/games"

    def getData(self, URL ,date):
        response = requests.get(f"{URL}?dates[]={date}")
        data = json.loads(response.content)
        return data["data"]


    def getTodaysGames(self, update, context):
        today = datetime.today().strftime('%Y-%m-%d')
        data = self.getData(URL,today)

        value = ""
        for datum in data:
            value += (f":basketball: {datum['home_team']['name']} vs  {datum['visitor_team']['name']} at {datum['status']}\n")
        
        update.message.reply_text(emoji.emojize(value))
        context.bot.sendMessage(chat_id=self.CHANNEL_CHAT_ID, text=emoji.emojize(value))

    def getYesterdaysGames(self, update, context):

        yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
        data = self.getData(URL,yesterday)
        value = ""
        for datum in data:
            value += (f":loudspeaker: {datum['status']} => {datum['home_team']['name']} {datum['home_team_score']} - {datum['visitor_team_score']}  {datum['visitor_team']['name']}\n")
        
        update.message.reply_text(emoji.emojize(value))
        context.bot.sendMessage(chat_id=self.CHANNEL_CHAT_ID, text=emoji.emojize(value))

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)
