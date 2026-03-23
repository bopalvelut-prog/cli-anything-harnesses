import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drug running')
@cli.command()
def start(): click.echo('drug started')
if __name__ == '__main__': cli()
