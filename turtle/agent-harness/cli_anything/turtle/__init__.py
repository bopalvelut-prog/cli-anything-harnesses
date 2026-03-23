import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('turtle running')
@cli.command()
def start(): click.echo('turtle started')
if __name__ == '__main__': cli()
