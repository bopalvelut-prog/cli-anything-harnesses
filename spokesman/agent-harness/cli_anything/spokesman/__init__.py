import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spokesman running')
@cli.command()
def start(): click.echo('spokesman started')
if __name__ == '__main__': cli()
