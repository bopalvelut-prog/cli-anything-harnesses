import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yard running')
@cli.command()
def start(): click.echo('yard started')
if __name__ == '__main__': cli()
