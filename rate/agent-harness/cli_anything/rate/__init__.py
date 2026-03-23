import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rate running')
@cli.command()
def start(): click.echo('rate started')
if __name__ == '__main__': cli()
