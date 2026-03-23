import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('murder running')
@cli.command()
def start(): click.echo('murder started')
if __name__ == '__main__': cli()
