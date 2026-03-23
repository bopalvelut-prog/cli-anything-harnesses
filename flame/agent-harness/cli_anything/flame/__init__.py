import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flame running')
@cli.command()
def start(): click.echo('flame started')
if __name__ == '__main__': cli()
