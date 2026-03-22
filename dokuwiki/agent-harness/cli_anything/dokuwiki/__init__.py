import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('DokuWiki status')
@cli.command()
def pages(): click.echo('DokuWiki pages')
if __name__ == '__main__': cli()
