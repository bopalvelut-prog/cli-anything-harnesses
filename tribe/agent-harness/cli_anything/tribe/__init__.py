import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tribe running')
@cli.command()
def start(): click.echo('tribe started')
if __name__ == '__main__': cli()
