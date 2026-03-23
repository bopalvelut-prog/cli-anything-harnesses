import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gather running')
@cli.command()
def start(): click.echo('gather started')
if __name__ == '__main__': cli()
