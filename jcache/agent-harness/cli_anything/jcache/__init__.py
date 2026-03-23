import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jcache running')
@cli.command()
def start(): click.echo('jcache started')
if __name__ == '__main__': cli()
