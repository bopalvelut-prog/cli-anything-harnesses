import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nsd running')
@cli.command()
def start(): click.echo('nsd started')
if __name__ == '__main__': cli()
