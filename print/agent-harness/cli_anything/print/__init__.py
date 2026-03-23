import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('print running')
@cli.command()
def start(): click.echo('print started')
if __name__ == '__main__': cli()
