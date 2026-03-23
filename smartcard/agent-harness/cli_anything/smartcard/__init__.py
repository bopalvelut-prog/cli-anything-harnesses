import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smartcard running')
@cli.command()
def start(): click.echo('smartcard started')
if __name__ == '__main__': cli()
