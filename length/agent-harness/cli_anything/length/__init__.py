import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('length running')
@cli.command()
def start(): click.echo('length started')
if __name__ == '__main__': cli()
