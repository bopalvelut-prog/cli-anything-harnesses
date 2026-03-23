import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('without running')
@cli.command()
def start(): click.echo('without started')
if __name__ == '__main__': cli()
