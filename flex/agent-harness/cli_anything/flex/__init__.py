import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flex running')
@cli.command()
def start(): click.echo('flex started')
if __name__ == '__main__': cli()
