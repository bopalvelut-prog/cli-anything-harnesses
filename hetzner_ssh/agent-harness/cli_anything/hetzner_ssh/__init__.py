import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('SSH keys')
@cli.command()
def create(): click.echo('Create SSH key')
if __name__ == '__main__': cli()
