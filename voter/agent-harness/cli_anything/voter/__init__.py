import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('voter running')
@cli.command()
def start(): click.echo('voter started')
if __name__ == '__main__': cli()
