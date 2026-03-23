import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apprise running')
@cli.command()
def start(): click.echo('apprise started')
if __name__ == '__main__': cli()
