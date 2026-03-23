import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elastic running')
@cli.command()
def start(): click.echo('elastic started')
if __name__ == '__main__': cli()
