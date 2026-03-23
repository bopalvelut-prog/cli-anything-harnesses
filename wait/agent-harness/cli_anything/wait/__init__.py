import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wait running')
@cli.command()
def start(): click.echo('wait started')
if __name__ == '__main__': cli()
