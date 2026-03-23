import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nocodb running')
@cli.command()
def start(): click.echo('nocodb started')
if __name__ == '__main__': cli()
