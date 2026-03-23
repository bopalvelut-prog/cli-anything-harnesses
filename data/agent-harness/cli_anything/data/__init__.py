import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('data running')
@cli.command()
def start(): click.echo('data started')
if __name__ == '__main__': cli()
