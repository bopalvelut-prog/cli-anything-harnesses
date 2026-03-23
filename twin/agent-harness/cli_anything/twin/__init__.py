import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twin running')
@cli.command()
def start(): click.echo('twin started')
if __name__ == '__main__': cli()
