import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Curve swap')
@cli.command()
def pool(): click.echo('Curve pool')
if __name__ == '__main__': cli()
