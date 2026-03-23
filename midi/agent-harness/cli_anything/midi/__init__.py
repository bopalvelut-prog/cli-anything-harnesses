import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('midi running')
@cli.command()
def start(): click.echo('midi started')
if __name__ == '__main__': cli()
