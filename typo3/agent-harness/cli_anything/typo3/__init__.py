import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('TYPO3 running')
@cli.command()
def pages(): click.echo('TYPO3 pages')
if __name__ == '__main__': cli()
