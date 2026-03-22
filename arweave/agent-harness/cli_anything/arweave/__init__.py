import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def upload(): click.echo('Arweave upload')
@cli.command()
def download(): click.echo('Arweave download')
if __name__ == '__main__': cli()
