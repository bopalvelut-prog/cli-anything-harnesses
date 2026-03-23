import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hsqldb running')
@cli.command()
def start(): click.echo('hsqldb started')
if __name__ == '__main__': cli()
