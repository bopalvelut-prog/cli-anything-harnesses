import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peace running')
@cli.command()
def start(): click.echo('peace started')
if __name__ == '__main__': cli()
