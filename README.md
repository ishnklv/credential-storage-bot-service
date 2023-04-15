# Bot Service - Credential Storage service
### Author: Aktan Ishenkulov

### Stack technologies
Language: Python 3.11

Libraries:
    <ul>
        <li><b>aiogram</b> - Bot api managing</li>
        <li><b>redis</b> - Cache manager</li>
        <li><b>pymongo</b> - Storage data in mongodb</li>
        <li><b>python-dotenv</b> - Loading env variables</li>
    </ul>

### installation
Create virtual environment
```bash
$ python -m venv env
```
Install all dependencies
```bash
$ pip install -r requirements.txt
```
Create new bot in Telegram bot father.
You can create bot, enter by this url: [@BotFather](https://t.me/BotFather)
Then after created new bot, you should copy api token and paste to .env => `BOT_API_TOKEN`

### Configuration
Copy env variables from example
```bash
$ cp example.env .env && vim .env
```