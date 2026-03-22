import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sms(): click.echo('Plivo SMS sent')
@cli.command()
def call(): click.echo('Plivo call')
if __name__ == '__main__': cli()
