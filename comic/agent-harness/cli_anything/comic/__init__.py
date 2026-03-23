import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('comic running')
@cli.command()
def start(): click.echo('comic started')
if __name__ == '__main__': cli()
