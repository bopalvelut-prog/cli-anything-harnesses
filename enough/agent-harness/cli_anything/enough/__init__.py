import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enough running')
@cli.command()
def start(): click.echo('enough started')
if __name__ == '__main__': cli()
