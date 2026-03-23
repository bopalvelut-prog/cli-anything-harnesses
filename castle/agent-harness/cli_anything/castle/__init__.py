import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('castle running')
@cli.command()
def start(): click.echo('castle started')
if __name__ == '__main__': cli()
