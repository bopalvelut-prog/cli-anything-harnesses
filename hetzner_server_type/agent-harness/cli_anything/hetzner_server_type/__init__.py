import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Server types')
if __name__ == '__main__': cli()
