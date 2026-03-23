import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beat running')
@cli.command()
def start(): click.echo('beat started')
if __name__ == '__main__': cli()
