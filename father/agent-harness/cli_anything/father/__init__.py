import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('father running')
@cli.command()
def start(): click.echo('father started')
if __name__ == '__main__': cli()
