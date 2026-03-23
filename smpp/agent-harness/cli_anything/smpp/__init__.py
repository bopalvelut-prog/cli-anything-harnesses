import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smpp running')
@cli.command()
def start(): click.echo('smpp started')
if __name__ == '__main__': cli()
