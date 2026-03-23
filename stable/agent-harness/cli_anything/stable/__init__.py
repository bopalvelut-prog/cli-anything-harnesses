import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stable running')
@cli.command()
def start(): click.echo('stable started')
if __name__ == '__main__': cli()
