import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('household running')
@cli.command()
def start(): click.echo('household started')
if __name__ == '__main__': cli()
