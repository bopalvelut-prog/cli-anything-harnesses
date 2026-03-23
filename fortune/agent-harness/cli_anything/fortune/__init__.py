import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fortune running')
@cli.command()
def start(): click.echo('fortune started')
if __name__ == '__main__': cli()
