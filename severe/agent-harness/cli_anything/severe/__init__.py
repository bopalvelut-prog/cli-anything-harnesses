import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('severe running')
@cli.command()
def start(): click.echo('severe started')
if __name__ == '__main__': cli()
