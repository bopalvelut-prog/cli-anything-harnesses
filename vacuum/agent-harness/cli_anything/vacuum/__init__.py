import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vacuum running')
@cli.command()
def start(): click.echo('vacuum started')
if __name__ == '__main__': cli()
