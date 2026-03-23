import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('edit running')
@cli.command()
def start(): click.echo('edit started')
if __name__ == '__main__': cli()
