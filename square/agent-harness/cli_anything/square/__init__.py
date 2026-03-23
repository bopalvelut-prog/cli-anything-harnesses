import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('square running')
@cli.command()
def start(): click.echo('square started')
if __name__ == '__main__': cli()
