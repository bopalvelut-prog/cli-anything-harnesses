import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vital running')
@cli.command()
def start(): click.echo('vital started')
if __name__ == '__main__': cli()
