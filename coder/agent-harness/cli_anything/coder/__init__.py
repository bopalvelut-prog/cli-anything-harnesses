import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coder running')
@cli.command()
def start(): click.echo('coder started')
if __name__ == '__main__': cli()
