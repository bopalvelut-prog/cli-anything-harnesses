import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mydns running')
@cli.command()
def start(): click.echo('mydns started')
if __name__ == '__main__': cli()
