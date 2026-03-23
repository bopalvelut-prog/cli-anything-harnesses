import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('StackBlitz start')
@cli.command()
def deploy(): click.echo('StackBlitz deploy')
if __name__ == '__main__': cli()
