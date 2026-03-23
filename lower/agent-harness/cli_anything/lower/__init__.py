import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lower running')
@cli.command()
def start(): click.echo('lower started')
if __name__ == '__main__': cli()
