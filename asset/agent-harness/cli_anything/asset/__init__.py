import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asset running')
@cli.command()
def start(): click.echo('asset started')
if __name__ == '__main__': cli()
