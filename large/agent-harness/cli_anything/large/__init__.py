import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('large running')
@cli.command()
def start(): click.echo('large started')
if __name__ == '__main__': cli()
