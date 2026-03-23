import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('injury running')
@cli.command()
def start(): click.echo('injury started')
if __name__ == '__main__': cli()
