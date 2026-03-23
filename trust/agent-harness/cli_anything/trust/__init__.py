import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trust running')
@cli.command()
def start(): click.echo('trust started')
if __name__ == '__main__': cli()
