import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nest running')
@cli.command()
def start(): click.echo('nest started')
if __name__ == '__main__': cli()
