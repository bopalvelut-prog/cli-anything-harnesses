import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('genexus running')
@cli.command()
def start(): click.echo('genexus started')
if __name__ == '__main__': cli()
