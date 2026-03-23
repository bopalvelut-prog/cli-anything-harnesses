import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hit running')
@cli.command()
def start(): click.echo('hit started')
if __name__ == '__main__': cli()
