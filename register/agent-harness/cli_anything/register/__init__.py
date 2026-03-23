import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('register running')
@cli.command()
def start(): click.echo('register started')
if __name__ == '__main__': cli()
