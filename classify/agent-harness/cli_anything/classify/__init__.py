import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('classify running')
@cli.command()
def start(): click.echo('classify started')
if __name__ == '__main__': cli()
