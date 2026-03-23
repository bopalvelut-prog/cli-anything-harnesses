import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grass running')
@cli.command()
def start(): click.echo('grass started')
if __name__ == '__main__': cli()
