import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lima running')
@cli.command()
def start(): click.echo('lima started')
if __name__ == '__main__': cli()
