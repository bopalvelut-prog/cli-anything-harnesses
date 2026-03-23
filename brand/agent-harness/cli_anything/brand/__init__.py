import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brand running')
@cli.command()
def start(): click.echo('brand started')
if __name__ == '__main__': cli()
