from helga.plugins import command

@command('bipol', help='listen to what he has to say')
def bipol(client, channel, nick, message, cmd, args):
    words = requests.get('https://bipolasaservice.herokuapp.com/bipol')
    return words.text
