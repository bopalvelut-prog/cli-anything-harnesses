import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stimulus running')
@cli.command()
def start(): click.echo('stimulus started')
if __name__ == '__main__': cli()
