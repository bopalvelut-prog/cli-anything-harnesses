import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('word running')
@cli.command()
def start(): click.echo('word started')
if __name__ == '__main__': cli()
