import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('armor running')
@cli.command()
def start(): click.echo('armor started')
if __name__ == '__main__': cli()
