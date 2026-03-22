import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Episerver running')
@cli.command()
def content(): click.echo('Episerver content')
if __name__ == '__main__': cli()
