import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dtach running')
@cli.command()
def start(): click.echo('dtach started')
if __name__ == '__main__': cli()
