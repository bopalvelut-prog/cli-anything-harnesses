import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('western running')
@cli.command()
def start(): click.echo('western started')
if __name__ == '__main__': cli()
