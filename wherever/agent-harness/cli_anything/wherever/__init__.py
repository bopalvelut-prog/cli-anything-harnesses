import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wherever running')
@cli.command()
def start(): click.echo('wherever started')
if __name__ == '__main__': cli()
