import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('building running')
@cli.command()
def start(): click.echo('building started')
if __name__ == '__main__': cli()
