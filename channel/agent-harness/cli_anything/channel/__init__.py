import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('channel running')
@cli.command()
def start(): click.echo('channel started')
if __name__ == '__main__': cli()
