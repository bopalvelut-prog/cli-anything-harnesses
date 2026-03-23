import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flag running')
@cli.command()
def start(): click.echo('flag started')
if __name__ == '__main__': cli()
