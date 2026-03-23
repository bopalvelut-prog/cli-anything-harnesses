import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('foundation running')
@cli.command()
def start(): click.echo('foundation started')
if __name__ == '__main__': cli()
