import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('barrel running')
@cli.command()
def start(): click.echo('barrel started')
if __name__ == '__main__': cli()
