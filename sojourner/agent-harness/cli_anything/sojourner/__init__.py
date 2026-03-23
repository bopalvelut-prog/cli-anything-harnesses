import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sojourner running')
@cli.command()
def start(): click.echo('sojourner started')
if __name__ == '__main__': cli()
