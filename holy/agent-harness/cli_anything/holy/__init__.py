import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('holy running')
@cli.command()
def start(): click.echo('holy started')
if __name__ == '__main__': cli()
