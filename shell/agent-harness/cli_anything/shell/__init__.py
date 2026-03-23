import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shell running')
@cli.command()
def start(): click.echo('shell started')
if __name__ == '__main__': cli()
