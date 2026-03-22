import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def pages(): click.echo('Notion pages')
@cli.command()
def search(): click.echo('Search Notion')
if __name__ == '__main__': cli()
