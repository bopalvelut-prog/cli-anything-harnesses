import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bullet running')
@cli.command()
def start(): click.echo('bullet started')
if __name__ == '__main__': cli()
