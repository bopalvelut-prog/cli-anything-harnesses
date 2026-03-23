import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('temporary running')
@cli.command()
def start(): click.echo('temporary started')
if __name__ == '__main__': cli()
