import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('printer running')
@cli.command()
def start(): click.echo('printer started')
if __name__ == '__main__': cli()
