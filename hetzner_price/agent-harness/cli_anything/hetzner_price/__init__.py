import click
@click.group()
def cli(): pass
@cli.command()
def servers(): click.echo('Server prices')
@cli.command()
def volumes(): click.echo('Volume prices')
if __name__ == '__main__': cli()
