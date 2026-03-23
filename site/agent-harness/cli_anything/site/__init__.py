import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('site running')
@cli.command()
def start(): click.echo('site started')
if __name__ == '__main__': cli()
