import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bite running')
@cli.command()
def start(): click.echo('bite started')
if __name__ == '__main__': cli()
