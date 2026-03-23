import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sequence running')
@cli.command()
def start(): click.echo('sequence started')
if __name__ == '__main__': cli()
