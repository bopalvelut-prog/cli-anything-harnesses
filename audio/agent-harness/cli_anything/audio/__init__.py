import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('audio running')
@cli.command()
def start(): click.echo('audio started')
if __name__ == '__main__': cli()
