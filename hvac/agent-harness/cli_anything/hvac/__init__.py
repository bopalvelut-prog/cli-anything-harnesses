import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hvac running')
@cli.command()
def start(): click.echo('hvac started')
if __name__ == '__main__': cli()
