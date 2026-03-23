import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bomb running')
@cli.command()
def start(): click.echo('bomb started')
if __name__ == '__main__': cli()
