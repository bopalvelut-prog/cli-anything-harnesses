import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crop running')
@cli.command()
def start(): click.echo('crop started')
if __name__ == '__main__': cli()
