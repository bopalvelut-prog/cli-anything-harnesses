import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('central running')
@cli.command()
def start(): click.echo('central started')
if __name__ == '__main__': cli()
