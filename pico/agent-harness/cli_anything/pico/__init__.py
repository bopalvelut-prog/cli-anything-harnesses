import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pico running')
@cli.command()
def start(): click.echo('pico started')
if __name__ == '__main__': cli()
