import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kinvolk running')
@cli.command()
def start(): click.echo('kinvolk started')
if __name__ == '__main__': cli()
