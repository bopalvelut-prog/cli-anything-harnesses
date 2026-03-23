import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visibility running')
@cli.command()
def start(): click.echo('visibility started')
if __name__ == '__main__': cli()
