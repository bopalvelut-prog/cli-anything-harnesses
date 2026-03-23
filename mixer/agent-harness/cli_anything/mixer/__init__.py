import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mixer running')
@cli.command()
def start(): click.echo('mixer started')
if __name__ == '__main__': cli()
