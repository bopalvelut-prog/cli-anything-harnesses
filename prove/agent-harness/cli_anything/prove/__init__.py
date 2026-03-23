import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prove running')
@cli.command()
def start(): click.echo('prove started')
if __name__ == '__main__': cli()
