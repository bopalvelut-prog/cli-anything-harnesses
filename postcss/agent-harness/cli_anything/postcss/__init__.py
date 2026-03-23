import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('postcss running')
@cli.command()
def start(): click.echo('postcss started')
if __name__ == '__main__': cli()
