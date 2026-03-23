import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('opinion running')
@cli.command()
def start(): click.echo('opinion started')
if __name__ == '__main__': cli()
