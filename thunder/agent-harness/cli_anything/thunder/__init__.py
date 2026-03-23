import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thunder running')
@cli.command()
def start(): click.echo('thunder started')
if __name__ == '__main__': cli()
