import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seller running')
@cli.command()
def start(): click.echo('seller started')
if __name__ == '__main__': cli()
