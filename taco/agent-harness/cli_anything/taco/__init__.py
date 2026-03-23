import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('taco running')
@cli.command()
def start(): click.echo('taco started')
if __name__ == '__main__': cli()
