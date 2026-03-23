import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('breed running')
@cli.command()
def start(): click.echo('breed started')
if __name__ == '__main__': cli()
