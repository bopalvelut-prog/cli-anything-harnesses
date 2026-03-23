import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('season running')
@cli.command()
def start(): click.echo('season started')
if __name__ == '__main__': cli()
