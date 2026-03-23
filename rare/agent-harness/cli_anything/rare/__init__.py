import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rare running')
@cli.command()
def start(): click.echo('rare started')
if __name__ == '__main__': cli()
