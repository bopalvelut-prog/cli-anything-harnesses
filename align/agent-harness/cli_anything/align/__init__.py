import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('align running')
@cli.command()
def start(): click.echo('align started')
if __name__ == '__main__': cli()
