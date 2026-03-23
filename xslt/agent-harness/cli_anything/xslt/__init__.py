import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xslt running')
@cli.command()
def start(): click.echo('xslt started')
if __name__ == '__main__': cli()
