import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('infrastructure running')
@cli.command()
def start(): click.echo('infrastructure started')
if __name__ == '__main__': cli()
