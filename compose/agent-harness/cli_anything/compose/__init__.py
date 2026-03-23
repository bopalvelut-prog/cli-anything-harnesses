import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('compose running')
@cli.command()
def start(): click.echo('compose started')
if __name__ == '__main__': cli()
