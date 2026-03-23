import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('silence running')
@cli.command()
def start(): click.echo('silence started')
if __name__ == '__main__': cli()
