from helga.plugins import command
from requests import get

@command('bipol', help='listen to what he has to say')
def bipol(client, channel, nick, message, cmd, args):
    response = get('http://bipolasaservice.herokuapp.com/bipol')
    return response.text

