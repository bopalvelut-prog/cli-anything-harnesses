import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guard running')
@cli.command()
def start(): click.echo('guard started')
if __name__ == '__main__': cli()
