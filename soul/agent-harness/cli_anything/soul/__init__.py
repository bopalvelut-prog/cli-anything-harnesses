import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soul running')
@cli.command()
def start(): click.echo('soul started')
if __name__ == '__main__': cli()
