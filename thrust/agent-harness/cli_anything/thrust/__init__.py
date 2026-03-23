import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thrust running')
@cli.command()
def start(): click.echo('thrust started')
if __name__ == '__main__': cli()
