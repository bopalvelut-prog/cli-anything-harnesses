import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adapter running')
@cli.command()
def start(): click.echo('adapter started')
if __name__ == '__main__': cli()
