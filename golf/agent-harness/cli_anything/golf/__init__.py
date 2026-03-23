import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('golf running')
@cli.command()
def start(): click.echo('golf started')
if __name__ == '__main__': cli()
