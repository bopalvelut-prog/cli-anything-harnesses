import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wireless running')
@cli.command()
def start(): click.echo('wireless started')
if __name__ == '__main__': cli()
