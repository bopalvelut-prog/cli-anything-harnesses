import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crowd running')
@cli.command()
def start(): click.echo('crowd started')
if __name__ == '__main__': cli()
