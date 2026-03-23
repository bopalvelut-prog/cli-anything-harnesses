import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cannon running')
@cli.command()
def start(): click.echo('cannon started')
if __name__ == '__main__': cli()
