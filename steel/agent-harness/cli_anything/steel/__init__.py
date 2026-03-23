import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('steel running')
@cli.command()
def start(): click.echo('steel started')
if __name__ == '__main__': cli()
