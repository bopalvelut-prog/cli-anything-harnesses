import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scientist running')
@cli.command()
def start(): click.echo('scientist started')
if __name__ == '__main__': cli()
