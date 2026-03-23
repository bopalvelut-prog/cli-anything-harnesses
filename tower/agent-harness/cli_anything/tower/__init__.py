import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tower running')
@cli.command()
def start(): click.echo('tower started')
if __name__ == '__main__': cli()
