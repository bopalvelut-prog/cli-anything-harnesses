import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('key running')
@cli.command()
def start(): click.echo('key started')
if __name__ == '__main__': cli()
