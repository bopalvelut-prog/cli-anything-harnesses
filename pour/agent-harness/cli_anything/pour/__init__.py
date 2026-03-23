import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pour running')
@cli.command()
def start(): click.echo('pour started')
if __name__ == '__main__': cli()
