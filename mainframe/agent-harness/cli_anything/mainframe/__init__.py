import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mainframe running')
@cli.command()
def start(): click.echo('mainframe started')
if __name__ == '__main__': cli()
