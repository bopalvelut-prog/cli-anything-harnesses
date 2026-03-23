import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('identify running')
@cli.command()
def start(): click.echo('identify started')
if __name__ == '__main__': cli()
