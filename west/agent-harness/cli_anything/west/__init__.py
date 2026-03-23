import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('west running')
@cli.command()
def start(): click.echo('west started')
if __name__ == '__main__': cli()
