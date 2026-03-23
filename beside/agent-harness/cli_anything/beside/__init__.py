import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beside running')
@cli.command()
def start(): click.echo('beside started')
if __name__ == '__main__': cli()
