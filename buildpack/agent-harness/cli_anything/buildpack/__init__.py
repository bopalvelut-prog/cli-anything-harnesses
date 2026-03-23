import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildpack running')
@cli.command()
def start(): click.echo('buildpack started')
if __name__ == '__main__': cli()
