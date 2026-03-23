import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('linear running')
@cli.command()
def start(): click.echo('linear started')
if __name__ == '__main__': cli()
