import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('angelfish running')
@cli.command()
def start(): click.echo('angelfish started')
if __name__ == '__main__': cli()
