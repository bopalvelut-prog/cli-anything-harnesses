import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emerge running')
@cli.command()
def start(): click.echo('emerge started')
if __name__ == '__main__': cli()
