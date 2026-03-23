import click
@click.group()
def cli(): pass
@cli.command()
def deploy(): click.echo('Functions deploy')
@cli.command()
def list(): click.echo('Functions list')
if __name__ == '__main__': cli()
