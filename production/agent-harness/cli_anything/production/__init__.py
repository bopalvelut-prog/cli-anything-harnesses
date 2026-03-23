import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('production running')
@cli.command()
def start(): click.echo('production started')
if __name__ == '__main__': cli()
