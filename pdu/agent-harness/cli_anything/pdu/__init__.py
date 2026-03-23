import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pdu running')
@cli.command()
def start(): click.echo('pdu started')
if __name__ == '__main__': cli()
