import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('MediaWiki status')
@cli.command()
def pages(): click.echo('MediaWiki pages')
if __name__ == '__main__': cli()
