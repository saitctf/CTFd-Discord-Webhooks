from os import environ

def _str_to_bool(value):
    """Convert string environment variable to boolean."""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ('true', '1', 'yes', 'on')
    return False

def config(app):
    '''
    Discord webhook URL to send data to. Set to None to disable plugin entirely.
    '''
    app.config['DISCORD_WEBHOOK_URL'] = environ.get('DISCORD_WEBHOOK_URL')

    '''
    Limit on number of solves for challenge to trigger webhook for. Set to 0 to send a message for every solve.
    '''
    app.config['DISCORD_WEBHOOK_LIMIT'] = environ.get('DISCORD_WEBHOOK_LIMIT', '1')

    '''
    Webhook flag submission format string. Valid vars: team, user, solves, fsolves (formatted solves), challenge, category, team_id, user_id, challenge_slug, value
    '''
    app.config['DISCORD_WEBHOOK_MESSAGE'] = environ.get('DISCORD_WEBHOOK_MESSAGE', 'Wastelanders, our first test subject has triumphed! {user} from {team} is the first to complete {challenge}. Please remain calm while morale is adjusted accordingly.')

    '''
    Post webhook message when challenge is changed (published, hidden or updated)
    '''
    app.config['DISCORD_WEBHOOK_CHALL'] = _str_to_bool(environ.get('DISCORD_WEBHOOK_CHALL', False))

    '''
    Post webhook message when challenge is updated (otherwise only published or hidden)
    '''
    app.config['DISCORD_WEBHOOK_CHALL_UPDATE'] = _str_to_bool(environ.get('DISCORD_WEBHOOK_CHALL_UPDATE', False))

    '''
    Post webhook message even if challenge has not yet been published (only relevant when update is enabled)
    '''
    app.config['DISCORD_WEBHOOK_CHALL_UNPUBLISHED'] = _str_to_bool(environ.get('DISCORD_WEBHOOK_CHALL_UNPUBLISHED', False))

    '''
    Webhook challenge change format string. Valid vars: challenge, category, action (published, hidden or updated)
    '''
    app.config['DISCORD_WEBHOOK_CHALL_MESSAGE'] = environ.get('DISCORD_WEBHOOK_CHALL_MESSAGE', 'Challenge {challenge} has been {action}!')

    '''
    Turning this on turns your DISCORD_WEBHOOK_CHALL_MESSAGE into a f-string. Values can be accessed with data.<field>

    This allows conditional formatting: e.g. {'FIRST BLOOD' if data.solves == 1 else ''}
    '''
    app.config['DISCORD_WEBHOOK_FSTRING'] = _str_to_bool(environ.get('DISCORD_WEBHOOK_FSTRING', False))