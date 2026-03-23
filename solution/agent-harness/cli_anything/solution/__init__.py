import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('solution running')
@cli.command()
def start(): click.echo('solution started')
if __name__ == '__main__': cli()
