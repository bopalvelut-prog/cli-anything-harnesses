import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flesh running')
@cli.command()
def start(): click.echo('flesh started')
if __name__ == '__main__': cli()
