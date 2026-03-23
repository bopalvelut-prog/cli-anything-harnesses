import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thousand running')
@cli.command()
def start(): click.echo('thousand started')
if __name__ == '__main__': cli()
