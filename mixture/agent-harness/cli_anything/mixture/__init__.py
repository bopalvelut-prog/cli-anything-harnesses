import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mixture running')
@cli.command()
def start(): click.echo('mixture started')
if __name__ == '__main__': cli()
