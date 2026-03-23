import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appbase running')
@cli.command()
def start(): click.echo('appbase started')
if __name__ == '__main__': cli()
