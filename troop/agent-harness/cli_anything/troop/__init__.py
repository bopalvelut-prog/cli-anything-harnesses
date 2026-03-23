import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('troop running')
@cli.command()
def start(): click.echo('troop started')
if __name__ == '__main__': cli()
