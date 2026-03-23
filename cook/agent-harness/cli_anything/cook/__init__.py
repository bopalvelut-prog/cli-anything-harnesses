import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cook running')
@cli.command()
def start(): click.echo('cook started')
if __name__ == '__main__': cli()
