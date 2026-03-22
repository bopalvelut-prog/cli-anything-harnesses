import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def upload(): click.echo('Sia upload')
@cli.command()
def download(): click.echo('Sia download')
if __name__ == '__main__': cli()
