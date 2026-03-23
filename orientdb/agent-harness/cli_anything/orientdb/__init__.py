import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('orientdb running')
@cli.command()
def start(): click.echo('orientdb started')
if __name__ == '__main__': cli()
