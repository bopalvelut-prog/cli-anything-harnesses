import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kickstart running')
@cli.command()
def start(): click.echo('kickstart started')
if __name__ == '__main__': cli()
