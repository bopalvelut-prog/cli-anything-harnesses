import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dance running')
@cli.command()
def start(): click.echo('dance started')
if __name__ == '__main__': cli()
