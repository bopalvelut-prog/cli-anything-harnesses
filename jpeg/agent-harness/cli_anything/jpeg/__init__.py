import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jpeg running')
@cli.command()
def start(): click.echo('jpeg started')
if __name__ == '__main__': cli()
