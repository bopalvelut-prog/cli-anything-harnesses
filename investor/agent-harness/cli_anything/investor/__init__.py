import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('investor running')
@cli.command()
def start(): click.echo('investor started')
if __name__ == '__main__': cli()
