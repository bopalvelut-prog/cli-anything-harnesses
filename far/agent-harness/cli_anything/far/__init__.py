import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('far running')
@cli.command()
def start(): click.echo('far started')
if __name__ == '__main__': cli()
