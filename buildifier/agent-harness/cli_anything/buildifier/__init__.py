import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildifier running')
@cli.command()
def start(): click.echo('buildifier started')
if __name__ == '__main__': cli()
