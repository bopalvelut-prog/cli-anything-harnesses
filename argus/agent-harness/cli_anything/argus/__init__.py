import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('argus running')
@cli.command()
def start(): click.echo('argus started')
if __name__ == '__main__': cli()
