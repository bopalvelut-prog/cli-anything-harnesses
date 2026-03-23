import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sparse running')
@cli.command()
def start(): click.echo('sparse started')
if __name__ == '__main__': cli()
