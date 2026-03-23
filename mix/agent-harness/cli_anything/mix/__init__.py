import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mix running')
@cli.command()
def start(): click.echo('mix started')
if __name__ == '__main__': cli()
