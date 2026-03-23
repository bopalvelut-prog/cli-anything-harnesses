import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('college running')
@cli.command()
def start(): click.echo('college started')
if __name__ == '__main__': cli()
