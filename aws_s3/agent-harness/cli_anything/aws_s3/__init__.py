import click
@click.group()
def cli(): pass
@cli.command()
def ls(): click.echo('S3 ls')
@cli.command()
def cp(): click.echo('S3 cp')
if __name__ == '__main__': cli()
