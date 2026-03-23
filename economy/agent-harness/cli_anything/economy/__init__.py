import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('economy running')
@cli.command()
def start(): click.echo('economy started')
if __name__ == '__main__': cli()
