import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('external running')
@cli.command()
def start(): click.echo('external started')
if __name__ == '__main__': cli()
