import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ccache running')
@cli.command()
def start(): click.echo('ccache started')
if __name__ == '__main__': cli()
