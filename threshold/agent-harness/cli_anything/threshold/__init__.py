import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('threshold running')
@cli.command()
def start(): click.echo('threshold started')
if __name__ == '__main__': cli()
