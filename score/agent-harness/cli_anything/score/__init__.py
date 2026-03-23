import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('score running')
@cli.command()
def start(): click.echo('score started')
if __name__ == '__main__': cli()
