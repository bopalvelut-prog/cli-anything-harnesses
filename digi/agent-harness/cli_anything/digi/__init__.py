import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('digi running')
@cli.command()
def start(): click.echo('digi started')
if __name__ == '__main__': cli()
