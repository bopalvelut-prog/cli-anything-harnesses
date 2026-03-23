import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tourist running')
@cli.command()
def start(): click.echo('tourist started')
if __name__ == '__main__': cli()
