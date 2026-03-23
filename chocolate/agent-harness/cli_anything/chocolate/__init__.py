import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chocolate running')
@cli.command()
def start(): click.echo('chocolate started')
if __name__ == '__main__': cli()
