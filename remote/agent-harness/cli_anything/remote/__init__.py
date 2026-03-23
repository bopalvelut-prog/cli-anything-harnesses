import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('remote running')
@cli.command()
def start(): click.echo('remote started')
if __name__ == '__main__': cli()
