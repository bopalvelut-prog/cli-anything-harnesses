import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Wiki.js status')
@cli.command()
def pages(): click.echo('Wiki.js pages')
if __name__ == '__main__': cli()
