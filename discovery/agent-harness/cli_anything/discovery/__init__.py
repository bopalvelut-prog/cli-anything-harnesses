import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('discovery running')
@cli.command()
def start(): click.echo('discovery started')
if __name__ == '__main__': cli()
