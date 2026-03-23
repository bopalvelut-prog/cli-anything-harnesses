import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rich running')
@cli.command()
def start(): click.echo('rich started')
if __name__ == '__main__': cli()
