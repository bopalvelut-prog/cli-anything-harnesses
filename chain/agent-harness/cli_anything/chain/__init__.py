import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chain running')
@cli.command()
def start(): click.echo('chain started')
if __name__ == '__main__': cli()
