import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('justice running')
@cli.command()
def start(): click.echo('justice started')
if __name__ == '__main__': cli()
