import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wing running')
@cli.command()
def start(): click.echo('wing started')
if __name__ == '__main__': cli()
