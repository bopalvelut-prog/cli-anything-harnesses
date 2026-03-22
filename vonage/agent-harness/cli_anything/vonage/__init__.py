import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sms(): click.echo('Vonage SMS sent')
@cli.command()
def verify(): click.echo('Vonage verify')
if __name__ == '__main__': cli()
