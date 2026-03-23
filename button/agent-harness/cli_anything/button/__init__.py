import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('button running')
@cli.command()
def start(): click.echo('button started')
if __name__ == '__main__': cli()
