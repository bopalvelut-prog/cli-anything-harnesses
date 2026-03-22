import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sms(): click.echo('Twilio SMS sent')
@cli.command()
def call(): click.echo('Twilio call')
if __name__ == '__main__': cli()
