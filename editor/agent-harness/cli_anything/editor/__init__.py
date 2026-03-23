import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('editor running')
@cli.command()
def start(): click.echo('editor started')
if __name__ == '__main__': cli()
