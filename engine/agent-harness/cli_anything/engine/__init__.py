import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('engine running')
@cli.command()
def start(): click.echo('engine started')
if __name__ == '__main__': cli()
