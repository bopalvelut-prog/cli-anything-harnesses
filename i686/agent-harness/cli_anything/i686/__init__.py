import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('i686 running')
@cli.command()
def start(): click.echo('i686 started')
if __name__ == '__main__': cli()
