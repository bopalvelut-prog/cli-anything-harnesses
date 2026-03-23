import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bundler running')
@cli.command()
def start(): click.echo('bundler started')
if __name__ == '__main__': cli()
