import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('volatile running')
@cli.command()
def start(): click.echo('volatile started')
if __name__ == '__main__': cli()
