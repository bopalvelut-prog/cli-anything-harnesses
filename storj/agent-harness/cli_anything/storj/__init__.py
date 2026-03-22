import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def upload(): click.echo('Storj upload')
@cli.command()
def download(): click.echo('Storj download')
if __name__ == '__main__': cli()
