import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('design running')
@cli.command()
def start(): click.echo('design started')
if __name__ == '__main__': cli()
