import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pal running')
@cli.command()
def start(): click.echo('pal started')
if __name__ == '__main__': cli()
