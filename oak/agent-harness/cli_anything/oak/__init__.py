import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oak running')
@cli.command()
def start(): click.echo('oak started')
if __name__ == '__main__': cli()
