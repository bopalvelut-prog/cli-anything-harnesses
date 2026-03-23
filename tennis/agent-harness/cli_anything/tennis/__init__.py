import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tennis running')
@cli.command()
def start(): click.echo('tennis started')
if __name__ == '__main__': cli()
