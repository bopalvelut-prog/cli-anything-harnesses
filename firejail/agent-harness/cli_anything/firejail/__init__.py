import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('firejail running')
@cli.command()
def start(): click.echo('firejail started')
if __name__ == '__main__': cli()
