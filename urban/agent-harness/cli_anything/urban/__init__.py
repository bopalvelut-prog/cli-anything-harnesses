import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('urban running')
@cli.command()
def start(): click.echo('urban started')
if __name__ == '__main__': cli()
