import click
@click.group()
def cli(): pass
@cli.command()
def servers(): click.echo('Server prices v2')
if __name__ == '__main__': cli()
