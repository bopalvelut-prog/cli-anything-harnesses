import click
@click.group()
def cli(): pass
@cli.command()
def create(): click.echo('Codespaces create')
@cli.command()
def list(): click.echo('Codespaces list')
if __name__ == '__main__': cli()
