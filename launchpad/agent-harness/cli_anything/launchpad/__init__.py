import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('launchpad running')
@cli.command()
def start(): click.echo('launchpad started')
if __name__ == '__main__': cli()
