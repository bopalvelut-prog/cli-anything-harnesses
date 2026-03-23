import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warrant running')
@cli.command()
def start(): click.echo('warrant started')
if __name__ == '__main__': cli()
