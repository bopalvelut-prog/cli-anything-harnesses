import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildkit running')
@cli.command()
def start(): click.echo('buildkit started')
if __name__ == '__main__': cli()
