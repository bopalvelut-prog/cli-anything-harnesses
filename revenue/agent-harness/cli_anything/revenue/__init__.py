import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('revenue running')
@cli.command()
def start(): click.echo('revenue started')
if __name__ == '__main__': cli()
