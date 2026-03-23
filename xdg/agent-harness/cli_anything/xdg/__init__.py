import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xdg running')
@cli.command()
def start(): click.echo('xdg started')
if __name__ == '__main__': cli()
