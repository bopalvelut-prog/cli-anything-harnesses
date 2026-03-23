import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reaction running')
@cli.command()
def start(): click.echo('reaction started')
if __name__ == '__main__': cli()
