import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('avd running')
@cli.command()
def start(): click.echo('avd started')
if __name__ == '__main__': cli()
