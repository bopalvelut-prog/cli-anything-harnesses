import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xsd running')
@cli.command()
def start(): click.echo('xsd started')
if __name__ == '__main__': cli()
