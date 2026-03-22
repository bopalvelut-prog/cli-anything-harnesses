import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('MODX running')
@cli.command()
def resources(): click.echo('MODX resources')
if __name__ == '__main__': cli()
