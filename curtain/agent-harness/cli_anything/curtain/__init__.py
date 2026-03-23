import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('curtain running')
@cli.command()
def start(): click.echo('curtain started')
if __name__ == '__main__': cli()
