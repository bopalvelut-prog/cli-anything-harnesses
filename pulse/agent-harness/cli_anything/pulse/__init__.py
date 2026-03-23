import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pulse running')
@cli.command()
def start(): click.echo('pulse started')
if __name__ == '__main__': cli()
