import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('charity running')
@cli.command()
def start(): click.echo('charity started')
if __name__ == '__main__': cli()
