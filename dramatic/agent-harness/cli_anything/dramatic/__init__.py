import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dramatic running')
@cli.command()
def start(): click.echo('dramatic started')
if __name__ == '__main__': cli()
