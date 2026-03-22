import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Contao running')
@cli.command()
def pages(): click.echo('Contao pages')
if __name__ == '__main__': cli()
