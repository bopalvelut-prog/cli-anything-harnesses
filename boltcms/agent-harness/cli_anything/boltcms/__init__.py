import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boltcms running')
@cli.command()
def start(): click.echo('boltcms started')
if __name__ == '__main__': cli()
