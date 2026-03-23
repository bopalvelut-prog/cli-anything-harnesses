import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('queue running')
@cli.command()
def start(): click.echo('queue started')
if __name__ == '__main__': cli()
