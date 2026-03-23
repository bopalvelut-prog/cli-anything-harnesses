import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wave running')
@cli.command()
def start(): click.echo('wave started')
if __name__ == '__main__': cli()
