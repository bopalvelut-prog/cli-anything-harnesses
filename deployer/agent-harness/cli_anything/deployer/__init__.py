import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deployer running')
@cli.command()
def start(): click.echo('deployer started')
if __name__ == '__main__': cli()
