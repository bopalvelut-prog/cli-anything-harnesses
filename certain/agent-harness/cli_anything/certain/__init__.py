import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('certain running')
@cli.command()
def start(): click.echo('certain started')
if __name__ == '__main__': cli()
