import click
@click.group()
def cli(): pass
@cli.command()
def upload(): click.echo('R2 upload')
@cli.command()
def list(): click.echo('R2 list')
if __name__ == '__main__': cli()
