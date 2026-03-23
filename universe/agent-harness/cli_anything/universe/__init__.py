import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('universe running')
@cli.command()
def start(): click.echo('universe started')
if __name__ == '__main__': cli()
