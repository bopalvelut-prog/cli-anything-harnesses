import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stepping running')
@cli.command()
def start(): click.echo('stepping started')
if __name__ == '__main__': cli()
