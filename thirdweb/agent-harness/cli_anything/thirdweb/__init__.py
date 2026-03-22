import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deploy(): click.echo('Thirdweb deploy')
@cli.command()
def create(): click.echo('Thirdweb create')
if __name__ == '__main__': cli()
