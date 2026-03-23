import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arm running')
@cli.command()
def start(): click.echo('arm started')
if __name__ == '__main__': cli()
