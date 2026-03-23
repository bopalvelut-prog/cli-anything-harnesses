import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildbot running')
@cli.command()
def start(): click.echo('buildbot started')
if __name__ == '__main__': cli()
