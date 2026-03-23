import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('archiva running')
@cli.command()
def start(): click.echo('archiva started')
if __name__ == '__main__': cli()
