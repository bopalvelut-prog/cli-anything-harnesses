import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rump running')
@cli.command()
def start(): click.echo('rump started')
if __name__ == '__main__': cli()
