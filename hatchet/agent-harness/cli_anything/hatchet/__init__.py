import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hatchet running')
@cli.command()
def start(): click.echo('hatchet started')
if __name__ == '__main__': cli()
