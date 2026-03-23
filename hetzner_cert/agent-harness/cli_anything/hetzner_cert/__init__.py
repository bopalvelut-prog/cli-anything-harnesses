import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Certificates')
@cli.command()
def create(): click.echo('Create certificate')
if __name__ == '__main__': cli()
