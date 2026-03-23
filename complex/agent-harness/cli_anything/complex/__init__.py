import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('complex running')
@cli.command()
def start(): click.echo('complex started')
if __name__ == '__main__': cli()
