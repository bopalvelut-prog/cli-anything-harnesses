import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('heavy running')
@cli.command()
def start(): click.echo('heavy started')
if __name__ == '__main__': cli()
