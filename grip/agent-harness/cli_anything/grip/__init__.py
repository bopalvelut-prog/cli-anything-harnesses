import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grip running')
@cli.command()
def start(): click.echo('grip started')
if __name__ == '__main__': cli()
