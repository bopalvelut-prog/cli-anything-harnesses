import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wobble running')
@cli.command()
def start(): click.echo('wobble started')
if __name__ == '__main__': cli()
