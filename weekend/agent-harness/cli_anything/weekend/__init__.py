import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weekend running')
@cli.command()
def start(): click.echo('weekend started')
if __name__ == '__main__': cli()
