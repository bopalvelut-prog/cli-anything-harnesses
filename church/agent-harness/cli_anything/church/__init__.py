import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('church running')
@cli.command()
def start(): click.echo('church started')
if __name__ == '__main__': cli()
