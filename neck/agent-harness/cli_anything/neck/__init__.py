import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('neck running')
@cli.command()
def start(): click.echo('neck started')
if __name__ == '__main__': cli()
