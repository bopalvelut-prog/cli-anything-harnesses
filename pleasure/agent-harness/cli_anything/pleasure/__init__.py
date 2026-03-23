import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pleasure running')
@cli.command()
def start(): click.echo('pleasure started')
if __name__ == '__main__': cli()
