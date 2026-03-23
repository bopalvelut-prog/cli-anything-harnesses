import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_filestore running')
@cli.command()
def start(): click.echo('gcp_filestore started')
if __name__ == '__main__': cli()
