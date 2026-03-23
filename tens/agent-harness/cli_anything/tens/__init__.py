import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tens running')
@cli.command()
def start(): click.echo('tens started')
if __name__ == '__main__': cli()
