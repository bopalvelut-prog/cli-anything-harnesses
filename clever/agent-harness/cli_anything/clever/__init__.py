import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clever running')
@cli.command()
def start(): click.echo('clever started')
if __name__ == '__main__': cli()
