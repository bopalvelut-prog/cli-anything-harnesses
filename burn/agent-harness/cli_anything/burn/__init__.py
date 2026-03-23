import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('burn running')
@cli.command()
def start(): click.echo('burn started')
if __name__ == '__main__': cli()
