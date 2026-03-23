import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shake running')
@cli.command()
def start(): click.echo('shake started')
if __name__ == '__main__': cli()
