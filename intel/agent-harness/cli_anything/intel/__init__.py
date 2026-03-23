import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('intel running')
@cli.command()
def start(): click.echo('intel started')
if __name__ == '__main__': cli()
