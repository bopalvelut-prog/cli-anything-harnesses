import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def pages(): click.echo('Confluence pages')
@cli.command()
def spaces(): click.echo('Confluence spaces')
if __name__ == '__main__': cli()
