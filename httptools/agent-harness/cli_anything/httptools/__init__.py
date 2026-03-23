import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('httptools running')
@cli.command()
def start(): click.echo('httptools started')
if __name__ == '__main__': cli()
