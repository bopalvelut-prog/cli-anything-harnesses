import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('opponent running')
@cli.command()
def start(): click.echo('opponent started')
if __name__ == '__main__': cli()
