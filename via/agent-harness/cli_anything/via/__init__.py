import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('via running')
@cli.command()
def start(): click.echo('via started')
if __name__ == '__main__': cli()
