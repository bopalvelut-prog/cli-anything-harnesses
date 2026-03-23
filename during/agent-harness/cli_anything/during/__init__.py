import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('during running')
@cli.command()
def start(): click.echo('during started')
if __name__ == '__main__': cli()
