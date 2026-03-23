import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('energy running')
@cli.command()
def start(): click.echo('energy started')
if __name__ == '__main__': cli()
