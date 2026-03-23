import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scarf running')
@cli.command()
def start(): click.echo('scarf started')
if __name__ == '__main__': cli()
