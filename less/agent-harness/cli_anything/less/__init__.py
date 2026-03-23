import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('less running')
@cli.command()
def start(): click.echo('less started')
if __name__ == '__main__': cli()
