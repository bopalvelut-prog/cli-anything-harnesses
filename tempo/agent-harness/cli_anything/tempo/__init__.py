import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tempo running')
@cli.command()
def start(): click.echo('tempo started')
if __name__ == '__main__': cli()
