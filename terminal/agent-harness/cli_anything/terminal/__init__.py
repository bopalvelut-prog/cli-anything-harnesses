import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terminal running')
@cli.command()
def start(): click.echo('terminal started')
if __name__ == '__main__': cli()
