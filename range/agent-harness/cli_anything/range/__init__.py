import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('range running')
@cli.command()
def start(): click.echo('range started')
if __name__ == '__main__': cli()
