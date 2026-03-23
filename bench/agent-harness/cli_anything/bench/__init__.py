import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bench running')
@cli.command()
def start(): click.echo('bench started')
if __name__ == '__main__': cli()
