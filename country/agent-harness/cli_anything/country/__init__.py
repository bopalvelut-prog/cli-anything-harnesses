import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('country running')
@cli.command()
def start(): click.echo('country started')
if __name__ == '__main__': cli()
