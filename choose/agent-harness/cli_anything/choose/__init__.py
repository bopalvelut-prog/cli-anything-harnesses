import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('choose running')
@cli.command()
def start(): click.echo('choose started')
if __name__ == '__main__': cli()
