import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pywikibot running')
@cli.command()
def start(): click.echo('pywikibot started')
if __name__ == '__main__': cli()
