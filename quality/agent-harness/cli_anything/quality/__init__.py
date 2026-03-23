import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quality running')
@cli.command()
def start(): click.echo('quality started')
if __name__ == '__main__': cli()
