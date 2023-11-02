## Info
The key goal of project to get the user ID of giveaway participants from Telegram and store it into Google Sheets

## Get started

### Installation
```shell
pip install -r requirements.txt
```

### Setting up
create .env file
and fill up required fields

```
SPREADSHEET_ID="targeted_spreadsheet_id"
RANGE_NAME="targeted_range"
TELEGRAM_API_TOKEN="telegram_api_token"
CHANNEL_ID="telegram_channel_id"
```


## Using
1. Add the bot as administrator of telegram channel
2. The bility to send messages is required
3. Post the /init message on the channel to trigger the bot (This message can be deleted right after bot has started)

All the key data is stored in folder 'data'