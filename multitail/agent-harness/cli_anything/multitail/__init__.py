import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('multitail running')
@cli.command()
def start(): click.echo('multitail started')
if __name__ == '__main__': cli()
