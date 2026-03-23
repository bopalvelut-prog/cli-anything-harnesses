import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('command running')
@cli.command()
def start(): click.echo('command started')
if __name__ == '__main__': cli()
