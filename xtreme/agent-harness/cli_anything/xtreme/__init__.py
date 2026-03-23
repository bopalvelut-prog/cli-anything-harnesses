import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xtreme running')
@cli.command()
def start(): click.echo('xtreme started')
if __name__ == '__main__': cli()
