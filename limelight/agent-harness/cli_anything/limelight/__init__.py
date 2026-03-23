import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('Limelight purge')
@cli.command()
def list(): click.echo('Limelight list')
if __name__ == '__main__': cli()
