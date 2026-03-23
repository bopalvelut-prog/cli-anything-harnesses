import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('excellent running')
@cli.command()
def start(): click.echo('excellent started')
if __name__ == '__main__': cli()
