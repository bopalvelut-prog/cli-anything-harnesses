import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rocks running')
@cli.command()
def start(): click.echo('rocks started')
if __name__ == '__main__': cli()
