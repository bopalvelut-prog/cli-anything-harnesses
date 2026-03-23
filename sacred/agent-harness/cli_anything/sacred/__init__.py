import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sacred running')
@cli.command()
def start(): click.echo('sacred started')
if __name__ == '__main__': cli()
