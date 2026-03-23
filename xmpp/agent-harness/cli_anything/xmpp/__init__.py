import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xmpp running')
@cli.command()
def start(): click.echo('xmpp started')
if __name__ == '__main__': cli()
