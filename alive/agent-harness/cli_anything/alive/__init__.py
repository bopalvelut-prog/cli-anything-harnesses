import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alive running')
@cli.command()
def start(): click.echo('alive started')
if __name__ == '__main__': cli()
