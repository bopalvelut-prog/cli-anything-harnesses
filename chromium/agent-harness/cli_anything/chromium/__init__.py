import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chromium running')
@cli.command()
def start(): click.echo('chromium started')
if __name__ == '__main__': cli()
