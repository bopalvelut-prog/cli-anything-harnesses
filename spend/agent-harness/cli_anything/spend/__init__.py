import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spend running')
@cli.command()
def start(): click.echo('spend started')
if __name__ == '__main__': cli()
