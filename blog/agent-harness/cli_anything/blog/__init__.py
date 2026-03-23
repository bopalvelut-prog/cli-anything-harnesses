import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blog running')
@cli.command()
def start(): click.echo('blog started')
if __name__ == '__main__': cli()
