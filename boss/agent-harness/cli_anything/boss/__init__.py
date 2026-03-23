import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boss running')
@cli.command()
def start(): click.echo('boss started')
if __name__ == '__main__': cli()
