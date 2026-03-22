import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Outline status')
@cli.command()
def docs(): click.echo('Outline docs')
if __name__ == '__main__': cli()
