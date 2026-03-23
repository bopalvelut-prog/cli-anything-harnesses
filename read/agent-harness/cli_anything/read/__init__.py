import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('read running')
@cli.command()
def start(): click.echo('read started')
if __name__ == '__main__': cli()
