import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('counter running')
@cli.command()
def start(): click.echo('counter started')
if __name__ == '__main__': cli()
