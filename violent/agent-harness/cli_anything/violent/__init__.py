import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('violent running')
@cli.command()
def start(): click.echo('violent started')
if __name__ == '__main__': cli()
