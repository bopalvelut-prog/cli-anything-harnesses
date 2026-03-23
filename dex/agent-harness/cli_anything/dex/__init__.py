import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dex running')
@cli.command()
def start(): click.echo('dex started')
if __name__ == '__main__': cli()
