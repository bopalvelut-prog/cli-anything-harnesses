import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('define running')
@cli.command()
def start(): click.echo('define started')
if __name__ == '__main__': cli()
