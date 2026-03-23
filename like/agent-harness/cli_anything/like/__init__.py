import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('like running')
@cli.command()
def start(): click.echo('like started')
if __name__ == '__main__': cli()
