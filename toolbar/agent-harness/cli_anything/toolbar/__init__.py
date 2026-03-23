import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toolbar running')
@cli.command()
def start(): click.echo('toolbar started')
if __name__ == '__main__': cli()
